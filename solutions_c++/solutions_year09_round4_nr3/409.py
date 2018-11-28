#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <list>
#include <stack>
#include <utility>
#include <cstdlib>
#include <sstream>
#include <fcntl.h>

using namespace std;

const int INF=0x7fffffff;
const int N = 17;
const int K = 30;
const int M = 1<<N;
int dp[M];

int price[N][K];

bool g[N][N];

int main(int argc,char**argv) {
	int cs;
	scanf("%d",&cs);

	for (int csi=1; csi<=cs; ++csi) {
		int n,k;
		scanf("%d%d",&n,&k);
		for (int i=0; i<n; ++i) for (int j=0; j<k; ++j) scanf("%d",price[i]+j);

		for (int i=0; i<n; ++i) for (int j=0; j<n; ++j) {
			g[i][j] = true;
			bool l=false,r=false;
			for (int t=0; t<k; ++t) {
				if (price[i][t] <= price[j][t]) l = true;
				if (price[i][t] >= price[j][t]) r = true;
			}
			g[i][j] = (l && r);
		}
/*
		for (int i=0; i<n; ++i) {
			for (int j=0; j<n; ++j) printf("%d ",g[i][j]);
			printf("\n");
		}
*/
		dp[0] = dp[1] = 1;
		for (int m=1; m<(1<<n); ++m) {
			dp[m] = n+1;	
		}
		vector<int> one;
		for (int m=0; m<(1<<n); ++m) {
			if (m > 0 && dp[m] == 1) {
				one.push_back(m);
			}
			for (int t=0; t<n; ++t) {
				if ((1<<t)&m) continue;
				int x=0;
				for (int l=0; l<n; ++l) {
					if (!((1<<l)&m)) continue;
					if (g[t][l]) {
					       	x = 1;
						break;
					}
				}
				dp[m | (1<<t)] = min(dp[m|(1<<t)],dp[m]+x);
//				printf("d[%d] = %d  ---> d[%d] = %d\n",m,dp[m], (m|(1<<t)), dp[m|(1<<t)]);
			}
		}
		for (int m=0; m<(1<<n); ++m) {
			if (dp[m] < 3) continue;
			for (size_t i=0; i<one.size(); ++i) {
				if (one[i] > m) break;
				dp[m] = min(dp[m],1+dp[m&(~one[i])]);
			}
		}

		printf("Case #%d: %d\n",csi,dp[(1<<n)-1] );
	}

	return 0;
}
