#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <set>
using namespace std;
int cost[3000], dp[3000][13];
int main() {
	int T;
	scanf("%d",&T);
	for(int cn=1;cn<=T;++cn) {
		int P;
		scanf("%d",&P);
		for(int i=(1<<(P+1))-2;i>=0;--i) {
			scanf("%d",&cost[i]);
			if(i >= (1<<P)-1) {
				int req = P-cost[i];
				for(int j=0;j<req;++j) dp[i][j] = INT_MAX;
				for(int j=req;j<=P;++j) dp[i][j] = 0;
			}
			else {
				for(int j=0;j<=P;++j) {
					if(dp[i*2+1][j] == INT_MAX || dp[i*2+2][j] == INT_MAX) dp[i][j] = INT_MAX;
					else dp[i][j] = dp[i*2+1][j]+dp[i*2+2][j];
					if(j == P) continue;
					if(dp[i*2+1][j+1] != INT_MAX && dp[i*2+2][j+1] != INT_MAX)
						dp[i][j] = min(dp[i][j],dp[i*2+1][j+1]+dp[i*2+2][j+1]+cost[i]);
				}
			}
		}
		printf("Case #%d: %d\n",cn,dp[0][0]);
	}
}
