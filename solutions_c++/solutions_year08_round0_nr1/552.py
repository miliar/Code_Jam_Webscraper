#include <iostream>
#include <string>
#include <map>
using namespace std;
int main()
{
	char s[128];
	int n, t, q;
	int dp[128][1024];
	scanf("%d\n", &t);
	for (int ic=1; ic<=t; ++ic) {
		scanf("%d\n", &n);
		map<string, int> id;
		for (int i=0; i<n; ++i) {
			gets(s);
			id[s]=i;
		}
		scanf("%d\n", &q);
		for (int i=0; i<n; ++i) dp[i][0]=0;
		for (int i=1; i<=q; ++i) {
			gets(s);
			for (int j=0; j<n; ++j) {
				dp[j][i]=dp[j][i-1];
				for (int k=0; k<n; ++k) dp[j][i]<?=dp[k][i-1]+1;
			}
			dp[id[s]][i]=1000000000;
		}
		int res=dp[0][q];
		for (int i=1; i<n; ++i) res<?=dp[i][q];
		printf("Case #%d: %d\n", ic, res);
	}
}
