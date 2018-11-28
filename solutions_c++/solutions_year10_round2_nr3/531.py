#include <cstdio>
#include <cstring>
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
using namespace std;
const int M = 100003, N = 505;
int f[N+20][N+20] = {0};
bool vis[N+20][N+20] = {0};

int g(int n, int m) {
	if (n < -1)	return 0;
	int &r = f[n+1][m];
	if (vis[n+1][m])
		return r;
	vis[n+1][m] = 1;
	if (n==0 && m>=0)	return r = 1;
	if (n<0)	return r = 0;
	if (n>0 && m==0)	return r = 0;
	r = 0;
	for (int i=n-m; i<=n-1; i++) {
		r += g(i, m);
		r %= M;
	}
	return r;
}

int main() {
	memset(vis,0,sizeof(vis));
	FOR(m,0,N)
		FOR(n,-1,N)
			g(n,m);
	int t, n;
	int ans[N] = {0};
	FOR(i,2,N)
		FOR(j,-1,i+1)
			ans[i] += g(j,i-j), ans[i] %= M;
	scanf("%d", &t);
	
	FOR(zz,1,t+1) {
		scanf("%d", &n);
		printf("Case #%d: %d\n", zz, n==2 ? 1 : ans[n-1]);
	}
}
