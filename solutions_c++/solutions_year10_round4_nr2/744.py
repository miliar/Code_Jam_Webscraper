#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<string>
#include<algorithm>
#include<fstream>
#include<sstream>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<deque>
#include<complex>
#include<numeric>
using namespace std;

const int MaxP = 11;
const int MaxN = (1 << 11) + 5;

int need[MaxN], mat[MaxP], cost[MaxN], tmp[MaxN], ind[MaxN];
int L[MaxP][MaxN], R[MaxP][MaxN];
int dp[MaxN][MaxP], g[MaxN], f[MaxN], C[MaxN];
int N, P, no, s;
inline int checkmn(int&a,int b){if(b>-1)if(a<0||b<a)a=b;}
inline int checkmx(int&a,int b){if(b>a)a=b;}
const int inf = 100000000;
int get(int k, int r) {
	if(k >= N) {
		if(r > need[k]) return inf;
		return 0;
	}
	int&ret = dp[k][r];
	if(ret>-1) return ret;
	ret = inf;
	for(int lp = r; lp <= P; ++ lp)
		for(int rp = r; rp <= P; ++ rp) {
			if(lp!=r&&rp!=r)continue;
			checkmn(ret, get(2*k,lp)+get(2*k+1,rp)+cost[k]); // buy
			if(lp<P&&rp<P) // not buy
				checkmn(ret,get(2*k,lp+1)+get(2*k+1,rp+1));
		}
	return ret;
}

int run() {
	scanf("%d", &P);
	N = 1 << P;
	
	for(int i=N;i<2*N;++i) scanf("%d",need+i);
	int n = N;
	int s = N;
	for(int r = 1; r <= P; ++ r) {
		s >>= 1;
		mat[r] = s;
		for(int j = 0; j < s; ++ j)
			scanf("%d", cost + --n);
		reverse(cost + (1 << r), cost + (1 << r + 1));
	}
	
	memset(dp, -1, sizeof(dp));
	
	int ret = -1;
	for(int i=0;i<=P;++i) checkmn(ret, get(1,i));
	return ret;
}

int main() {
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	
	int test;
	scanf("%d", &test);
	while(test--) 
		printf("Case #%d: %d\n",++no, run());
}
