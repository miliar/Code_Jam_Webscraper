#include <iostream>
using namespace std;
int dp[26];
const int MOD = 100003;
bool vist[26];
int n;
int rank[26];
void dfs(int pos, int rk) {
	int i;
	if (pos == n) {
		int x = n;;
		while (1)
		{
			x = rank[x];
			if (x == 0) {
				break;
			}
			if (x == 1) {
				dp[n] = (dp[n] + 1) % 100003;
				break;
			}
		}
		return;
	}
	for (i = pos + 1; i <= n; ++i) {
		rank[i] = rk + 1;
		dfs(i, rk + 1);
		rank[i] = 0;
	}
}

int main() {
	int i,j;
	memset(rank,0,sizeof(rank));
	memset(dp,0,sizeof(dp));
	for (i = 2; i<=25;++i) {
		n = i;
		for (j = 2; j <= i;++j) {
			rank[j] = 1;
			dfs(j, 1);
			rank[j] = 0;
		}
	//	printf("%d : %d\n",i,dp[i]);
	}
	int T;

	freopen("C.in","r", stdin);
	freopen("C.out","w", stdout);
	scanf("%d",&T);

	int b = 1;
	while (T--)
	{
		scanf("%d",&n);
		printf("Case #%d: ", b++);
		printf("%d\n", dp[n]);
	}
	return 0;
}