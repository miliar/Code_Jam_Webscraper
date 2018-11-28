#include <cstdio>
#include <algorithm>

using namespace std;

#define N 10010

int d[N], l[N], dp[N];

int main()
{
	int T;
    freopen ("A-large.in", "r", stdin);
    freopen ("outlarge.txt", "w", stdout);
	scanf(" %d", &T);
	for(int z = 0; z < T; z ++)
	{
		printf("Case #%d: ", z + 1);
		int n, D;
		scanf(" %d", &n);
		for(int i = 0; i < n; i ++)
			scanf(" %d %d", d + i, l + i), dp[i] = -1;
		scanf(" %d", &D);
		dp[0] = d[0];
		bool poss = false;
		if(dp[0] >= D - d[0])
            poss = true;
		for(int i = 1; i < n; i ++)
		{
			for(int j = i - 1; j >= 0; j --)
			{
				if(dp[j] >= d[i] - d[j])
					dp[i] = max(min(d[i] - d[j], l[i]), dp[i]);
			}
			if(dp[i] >= D - d[i])
				poss = true;
            for(int j = 0; j < i; j ++)
                if(dp[i] >= d[i] - d[j])
                    dp[j] = max(min(d[i] - d[j], l[j]), dp[j]);
		}
		if(poss)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}
