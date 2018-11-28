#define _CRT_SECURE_NO_DEPRECATE
#include<vector>
#include<algorithm>
#include<iostream>
#include<sstream>
using namespace std;

#define sz(X) ((int)(X).size())
#define pb push_back
#define all(X) (X).begin(),(X).end()
#define FOR(I,S,N) for(int I=(S);I<(N);++I)
#define REP(I,N) FOR(I,0,N)

typedef vector<int> VI;

#define DIM 11000

int g[DIM],c[DIM],v[DIM];
int sav[DIM][2];

int m;

int dp(int u, int x) {
	if(2*u > m){
		if(v[u] == x) return 0;
		return -1;
	}
	if(sav[u][x] != -1) return sav[u][x] - 1;
	int ans=m+1;
	if(c[u] == 0) {
		if(g[u]==1) {
			REP(i,2) REP(j,2) if((i && j) == x) {
				if(dp(2*u,i) != -1 &&  dp(2*u + 1 , j) != -1) {
					ans = min(ans, dp(2*u,i) + dp(2*u + 1 , j));
				}
			}
		}
		else {
			REP(i,2) REP(j,2) if((i || j) == x) {
				if(dp(2*u,i) != -1 &&  dp(2*u + 1 , j) != -1) {
					ans = min(ans, dp(2*u,i) + dp(2*u + 1 , j) );
				}
			}
		}
		if(ans > m) ans = -1;
		sav[u][x] = ans + 1;
		return ans;
	}
	else {
		REP(i,2) REP(j,2) if((i && j) == x) {
			if(dp(2*u,i) != -1 &&  dp(2*u + 1 , j) != -1) {
				ans = min(ans, dp(2*u,i) + dp(2*u + 1 , j) + (g[u] != 1));
			}
		}
		REP(i,2) REP(j,2) if((i || j) == x) {
			if(dp(2*u,i) != -1 &&  dp(2*u + 1 , j) != -1) {
				ans = min(ans, dp(2*u,i) + dp(2*u + 1 , j) + (g[u] != 0));
			}
		}
		if(ans > m) ans = -1;
		sav[u][x] = ans + 1;
		return ans;
	}
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("a-large.out","w",stdout);
	int tc;
	scanf("%d",&tc);
	FOR(tn,1,tc+1) {
		int want;
		scanf("%d %d",&m,&want);
		FOR(i,1,(m-1)/2 + 1) {
			scanf("%d %d",&g[i],&c[i]);
		}
		FOR(i,(m-1)/2 + 1, m + 1) {
			scanf("%d",&v[i]);
		}
		memset(sav,-1,sizeof(sav));
		int ans = dp(1,want);
		
		if(ans == -1) {
			printf("Case #%d: IMPOSSIBLE\n",tn);
		}
		else {
			printf("Case #%d: %d\n",tn,ans);
		}
	}
	fflush(stdout);
	return 0;
}