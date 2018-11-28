#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <string>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cctype>

using namespace std;
typedef long long int64;
const int inf = 0x3f3f3f3f;
typedef double real;
const real eps = 1e-6;
typedef pair<int,int> pip;
#define Eo(x) { cerr << #x << " = " << (x) << endl; }

inline int bit(int k){
	return ( 1 << k);
}

int a[1 << 20];
int b[1 << 20];
int p;
int q;
int fighs;
int c[1 << 12][1 << 12];

int go(int mask, int v, int miss){
	if (v >= fighs){
		int z = v-fighs;
		z = q-1-z;
		if (miss > a[z]) return inf;
		return 0;
	}
	int l = (v+1)*2-1;
	int  r = (v+1)*2;
	int res = 0;
	if (mask&bit(v)){
		res += b[v];
	} else {
		miss++;
	}
	int r1 = go(mask,l,miss);
	int r2 = go(mask,r,miss);
	if (r1 == inf || r2 == inf) return inf;
	return res + r1 + r2;
}

int main(){
	int T; cin >> T;
	for (int  _ = 0; _ < T; _++){
		printf("Case #%d: ",_+1);
		cin >> p;
//		p = 10;
		q = bit(p);
		fighs = q-1;
		Eo(p);Eo(q);
		Eo(fighs);
		for (int i = 0; i < q; i++){
//			a[i] = 0;
		cin >> a[i];
		}
		for (int i = 0; i < fighs; i++){
//			b[i] = 1;
			cin >> b[fighs-1-i];
		}

		memset(c,0x3f,sizeof(c));
		for (int i = 0; i < q; i++){
			int v = fighs+q-1-i;
			for (int j = 0; j <= a[i]; j++)
				c[v][j] = 0;
		}
		for (int i = fighs-1; i >= 0; i--){
			int l = 2*(i+1)-1;
			int r = 2*(i+1);
			for (int j = 0; j < fighs*2; j++){
				c[i][j] = min(c[i][j],c[l][j]+c[r][j]+b[i]);
				c[i][j] = min(c[i][j],c[l][j+1]+c[r][j+1]);
			}
		}
		int mx = c[0][0];

		printf("%d\n",mx);
	}
	return 0;
}

