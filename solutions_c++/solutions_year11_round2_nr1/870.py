#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std; 
char comp[110][110];
double WP[110], OWP[110], OOWP[110];
int main()
{
	int T, tcnt = 0;
	freopen("A-large.in", "r", stdin);
	freopen("a.txt", "w", stdout);
	scanf("%d", &T);
	while (T--)
	{
		int N;
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
		{
			scanf("%s", comp[i]);
			int loss = 0, win = 0;
			for (int j = 0; comp[i][j]; j++)
				if (comp[i][j] == '0')
					loss++;
				else if (comp[i][j] == '1')
					win++;
			WP[i] = (double)win / (loss + win);
		}
		for (int i = 0; i < N; i++)
		{
			double twp = 0;
			int cnt = 0;
			for (int j = 0; j < N; j++)
			{
				if (comp[i][j] != '.')
				{
					int loss = 0, win = 0;
					for (int k = 0; k < N; k++)
					{
						if (k != i)
						{
							if (comp[j][k] == '0')
								loss++;
							else if (comp[j][k] == '1')
								win++;
						}
					}
					cnt++;
					twp += (double)win / (loss + win);
				}
			}
			OWP[i] = twp / cnt;
		}
		for (int i = 0; i < N; i++)
		{
			double towp = 0;
			int cnt = 0;
			for (int j = 0; j < N; j++)
				if (comp[i][j] != '.')
				{
					towp += OWP[j];
					cnt++;
				}
			OOWP[i] = towp / cnt;
		}
		printf("Case #%d:\n", ++tcnt);
		for (int i = 0; i < N; i++)
		{
			printf("%.10lf\n", 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]);
		}
	}
	return 0;
}
