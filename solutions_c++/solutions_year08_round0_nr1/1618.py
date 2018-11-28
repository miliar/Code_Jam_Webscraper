#include <cstdio>
#include <cstring>
#include <string>
#include <map>

#define REP(AA,BB) for(AA=0; AA<BB; ++AA)
#define FOR(AA,BB,CC) for(AA=BB; AA<CC; ++AA)

#define INF 2000

using namespace std;

char c[110]; int p[1010], dp[1010];

int main(void) {
	int t, n, m, i, j, k, x, res; string g;
	scanf("%d", &t);
	REP(x,t) {
		map<string, int> ma;
		scanf("%d", &n); gets(c);
		REP(i,n) {
			gets(c);
			ma[string(c)]=i;
		}
		scanf("%d", &m); gets(c);
		if(m==0) {
			printf("Case #%d: %d\n", x+1, 0);
			continue;
		}
		REP(i,m) {
			gets(c);
			p[i]=ma[string(c)];
		}
		memset(dp, 0, sizeof dp); dp[p[m-1]]=1;
		for(i=m-2; i>=0; --i) {
			k=INF;
			REP(j,p[i])
				k<?=dp[j];
			FOR(j,p[i]+1,n)
				k<?=dp[j];
			dp[p[i]]=k+1;
		}
		res=INF;
		REP(i,n)
			res<?=dp[i];
		printf("Case #%d: %d\n", x+1, res);
	}
	return 0;
}
