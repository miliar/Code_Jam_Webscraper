#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std; 
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("GCJ_B.txt", "w", stdout);
	int T, tcnt = 0;
	scanf("%d", &T);
	for (int tcnt = 1; tcnt <= T; tcnt++)
	{
		int C, D, N;
		scanf("%d", &C);
		char comb[40][5], oppo[40][5], invk[200];
		for (int i = 0; i < C; i++)
			scanf("%s", comb[i]);
		scanf("%d", &D);
		for (int i = 0; i < D; i++)
			scanf("%s", oppo[i]);
		scanf("%d", &N);
		scanf("%s", invk);
		char ans[200];
		int l = 0;
		for (int i = 0; i < N; i++)
		{
			ans[l] = invk[i];
			l++;
			if (l >= 2)
			{
				int j;
				for (j = 0; j < C; j++)
					if (ans[l - 1] == comb[j][0] && ans[l - 2] == comb[j][1]
						|| ans[l - 1] == comb[j][1] && ans[l - 2] == comb[j][0])
					{
						ans[l - 2] = comb[j][2];
						l--;
						break;
					}
				if (j == C)
				{
					int flag[300];
					memset(flag, 0, sizeof(flag));
					for (int k = 0; k < l - 1; k++)
						flag[ans[k]] = 1;
					for (int k = 0; k < D; k++)
					{
						if (ans[l - 1] == oppo[k][0] && flag[oppo[k][1]]
								|| ans[l - 1] == oppo[k][1] && flag[oppo[k][0]])
						{
							l = 0;
							break;
						}
					}
				}
			}
		}
		printf("Case #%d: [", tcnt);
		for (int i = 0; i < l; i++)
		{
			printf("%c", ans[i]);
			if (i < l - 1)
				printf(", ");
		}
		printf("]\n");
	}
	return 0;
}
