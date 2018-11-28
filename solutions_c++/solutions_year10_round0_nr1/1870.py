#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

const int max_n = 30;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);


	int T;
	scanf("%d", &T);
	int n;

	for (int i0 = 0; i0 < T; i0++)
	{
		int n, k;
		scanf("%d%d", &n, &k);
		int dp[50];
		dp[0] = 0;
		for (int i = 1; i <= n; i++)
			if (dp[i - 1] < k)
				dp[i] = 2 * dp[i - 1] + 1;
			else
			{
			    dp[n] = -1;
				break;
			}

        if (dp[n] == -1)
        {
            printf("Case #%d: OFF\n", i0 + 1);
            continue;
        }
		int W = dp[n];
		int w = W;
		while (w < k)
			w += W + 1;
		printf("Case #%d: ", i0 + 1);
		if (w == k) printf("ON\n");
			else printf("OFF\n");
	}
}
