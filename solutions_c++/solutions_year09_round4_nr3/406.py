#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

bool gt(vector<int> a, vector<int> b) {
	for (int i=0; i<a.size(); i++)
		if (a[i]<=b[i])	return 0;
	return 1;
}
unsigned dp[16][1<<16];
int main() {
	int z;
	scanf("%d",&z);
	int g = 1;
	while (z--) {
		int m,n,x;
		scanf("%d%d",&m,&n);
		vector<int> a[m];
		for (int i=0;i<m;i++)
			for (int j=0;j<n;j++)
				scanf("%d", &x), a[i].push_back(x);
		sort(a,a+m);
		swap(m,n);
		memset(dp,-1,sizeof(dp));
		dp[0][1] = 1;
		for (int k=1; k<n; k++) {
			// Add 1 more "stack"
			for (int r=1; r<(1<<k); r++)
				if (dp[k-1][r]!=-1)
					dp[k][r|(1<<k)] = dp[k-1][r] + 1;
			// Place on other "stack"
			for (int r=1; r<(1<<k); r++) {
				if (dp[k-1][r]==-1)	continue;
				for (int j=0; j<k; j++)
					if (r&(1<<j))
						if ( gt(a[k], a[j]) )
							dp[k][r+(1<<k)-(1<<j)] = min(dp[k][r+(1<<k)-(1<<j)], dp[k-1][r]);
			}
		}
		unsigned ans = 1<<28;
		for (int r=0; !(r>>n); r++)
			ans = min(ans, dp[n-1][r]);
		printf("Case #%d: %u\n", g++, ans);
	}
}
