#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <ctime>
#include <cassert>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <string>
#include <bitset>
#include <numeric>
#include <complex>
#include <utility>
#include <fstream>
#include <ostream>
#include <istream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <functional>
using namespace std;


#define CLR(a,v)	memset(a,v,sizeof(a))
#define MP(a,b)		make_pair(a,b)
#define SIZE(a)		((int)a.size())
#define LENGTH(a)	((int)a.length())
#define FOR(i,n)	for(i=0; i<(n); ++i)


template<class T>inline int cMin(T& a, T b) {return b<a ? a=b,1 : 0;}
template<class T>inline int cMax(T& a, T b) {return a<b ? a=b,1 : 0;}
template<class T>inline string to_str(T v) {ostringstream os; os<<v; return os.str();}


typedef int int32;
typedef unsigned int uint32;
typedef long long int64;
typedef unsigned long long uint64;


char *input_file = "E:/google/CodeJam/CodeJam/B-large.in";
char *output_file = "E:/google/CodeJam/CodeJam/B-large.out";
const bool zzzz = true;

int  f[128*128];
void clear() {CLR(f,-1);}
int find(int v) {return f[v]<0?v:f[v]=find(f[v]);}
void merge(int u, int v) {
	u = find(u);  v=find(v);
	if(u == v) return;
	if(f[u] < f[v]) f[v] = u;
	else {f[v]-=(f[u]==f[v]); f[u]=v;}
}

int  dx[] = {-1, 0, 0, 1};
int  dy[] = {0, -1, 1, 0};

int  h[128][128], idx[128][128];
int  N, M, K;

struct Node {
	int v, x, y;
	bool operator<(const Node& o)const{
		return v<o.v || v==o.v && (x<o.x || x==o.x && y<o.y);
	}
}A[128*128];
int  nA;

#define code(x,y) (((x)<<10) | (y))
void bfs(int sx, int sy) {
	queue<int> q;
	idx[sx][sy] = K;
	q.push(code(sx, sy));
	int  x, y, i, hv, c;
	while(!q.empty()) {
		sx = q.front();  q.pop();
		sy = sx&127;  sx >>= 10;
		hv = h[sx][sy];
		for(i=0; i<4; ++i) {
			x = sx+dx[i];  y = sy+dy[i];
			if(x<0 || y<0 || x>=N || y>=M) continue;
			if(h[x][y] >= hv) continue;
			hv = h[x][y];  c = code(x,y);
		}
		if(hv == h[sx][sy]) continue;
		x = c>>10;  y = c&127;
		if(idx[x][y]>=0) {
			merge(idx[x][y], K);
			continue;
		}
		idx[x][y] = K;
		q.push(code(x,y));
	}
	++K;
}

int main() {
	if(zzzz) {freopen(input_file, "r", stdin);freopen(output_file, "w", stdout);}
	
	int  ti, tn, i, j, k, cc;
	scanf("%d", &tn);
	for(ti=1; ti<=tn; ++ti) {

		scanf("%d%d", &N, &M);

		for(k=i=0; i<N; ++i) for(j=0; j<M; ++j, ++k) {
			scanf("%d", h[i]+j);
			A[k].v = h[i][j]; A[k].x = i; A[k].y=j;
		} nA = i*j;

		sort(A, A+nA);

		printf("Case #%d:\n", ti);

		CLR(idx, -1);
		clear();
		for(K=i=0; i<nA; ++i) if(idx[A[i].x][A[i].y] < 0)
			bfs(A[i].x, A[i].y);
		map<int, int> to;
		cc = 'a';
		FOR(i,N) {
			FOR(j,M) {
				k = find(idx[i][j]);
				if(!to.count(k)) to[k]=cc++;
				if(j) putchar(' ');
				putchar(to[k]);
			}
			putchar('\n');
		}
	}

	return 0;
}

