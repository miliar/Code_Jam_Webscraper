#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
using namespace std;

#define FILEIO
const int MAXN = 1005;
set<pair<int, int> > rem;
int x[MAXN], y[MAXN];

int bit(int x, int i){return (x >> i) & 1;}
//int clrb(int x, int i){return x & (~(1 << i));}
//int setb(int x, int i){return x | (1 << i);}
int setb(int x, int i, int v){
	return (x & (~(1 << i))) | (v << i);
}

const int INF = 2000000000;
void fill(int x0, int y0, int W, int L, int wall){
	if(rem.empty()) return ;
	if(W <= 0 || L <= 0) return;
	int xw = x0 + W;
	int yl = y0 + L;
	
	int ww = INF;
	if(bit(wall, 0) == 0 || bit(wall, 0) == 0) ww = W;
	if(bit(wall, 0) == 0 && bit(wall, 1) == 0) ww /= 2;
	int ll = INF;
	if(bit(wall, 2) == 0 || bit(wall, 3) == 0) ll = L;
	if(bit(wall, 2) == 0 && bit(wall, 3) == 0) ll /= 2;
	int supr = min(ww, ll);
	
	set<pair<int, int> >::iterator it = rem.upper_bound(make_pair(supr, MAXN));
	if(it == rem.begin()) return;
	--it;
	int rad = it -> first;
	int id = it -> second;
	rem.erase(it);
	
	if(bit(wall, 0) == 1) x[id] = x0;
	else if(bit(wall, 1) == 1) x[id] = x0 + W;
	else x[id] = x0 + rad;
	
	if(bit(wall, 2) == 1) y[id] = y0;
	else if(bit(wall, 3) == 1) y[id] = y0 + L;
	else y[id] = y0 + rad;
	
	int x1, y1, w1, l1, wall1 = 0;
	int x2, y2, w2, l2, wall2 = 0;
	if(bit(wall, 0) == 1){
		x1 = x0;
		x2 = x0 + rad;
		w1 = rad;
		w2 = W - rad;
		wall1 = setb(wall1, 0, 1);
		wall2 = setb(wall2, 1, bit(wall, 1));
		if(w2 <= 0){
			w1 = W;
			wall1 = setb(wall1, 1, bit(wall, 1));
		}
	}
	else if(bit(wall, 1) == 1){
		x1 = x0 + W - rad;
		x2 = x0;
		w1 = rad;
		w2 = W - rad;
		wall1 = setb(wall1, 1, 1);
		if(w2 <= 0){
			w1 = W;
		}
	}
	else{
		x1 = x0;
		x2 = x0 + rad * 2;
		w1 = rad * 2;
		w2 = W - rad * 2;
	}
	
	
	if(bit(wall, 2) == 1){
		y1 = y0 + rad;
		y2 = y0;
		l1 = L - rad;
		l2 = L;
		wall1 = setb(wall1, 3, bit(wall, 3));
	}
	else if(bit(wall, 3) == 1){
		y1 = y0;
		y2 = y0;
		l1 = L - rad;
		l2 = L;
	}
	else{
		y1 = y0 + rad * 2;
		y2 = y0;
		l1 = L - rad * 2;
		l2 = L;
	}
	wall2 = setb(wall2, 2, bit(wall, 2));
	wall2 = setb(wall2, 3, bit(wall, 3));
	
	fill(x1, y1, w1, l1, wall1);
	fill(x2, y2, w2, l2, wall2);
	//fill(x0          , y0 + rad * 2, rad * 2    ,  L - 2 * rad);
	//fill(x0 + rad * 2, y0          , W - rad * 2, L);
}

int main(){
#ifdef FILEIO
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	freopen("error.txt","w", stderr);
#endif
	int TT;
	scanf("%d", &TT);
	for(int cas = 1; cas <= TT; ++cas){
		rem.clear();
		int N, W, L;
		scanf("%d %d %d", &N, &W, &L);
		for(int i = 0;i < N; ++i){
			int r;
			scanf("%d", &r);
			rem.insert(make_pair(r, i));
		}
		fill(0, 0, W, L, 15);
		if(!rem.empty()) fprintf(stderr, "case %d error!\n", cas);
		printf("Case #%d:", cas);
		for(int i = 0;i < N; ++i) printf(" %d %d", x[i], y[i]);
		puts("");
	}
	return 0;
}
