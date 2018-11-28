#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std; 

int R, C, D;
int num[510][510];
int main()
{
	freopen("B-small-attempt2.in","r",stdin);
	freopen("B.txt","w",stdout);
	int T, tcnt = 0;
	int r, c;
	scanf("%d", &T);
	while (T--)
	{
		
		scanf("%d%d%d", &R, &C, &D);
		for (int i = 0; i < R; i++)
		{
			char cmd[1000];
			scanf("%s", cmd);
			for (int j = 0; j < C; j++)
			{
				num[i][j] = cmd[j] - '0' + D;
			}
		}
		int l = 3, r = R, ans = 0;
		for (int i = 1; i < R - 1; i++)
		{
			for (int j = 1; j < C - 1; j++)
			{
				for (l = 3; l <= r; l++)
				{
					if (l % 2 == 1)
					{
						if (i - l / 2 >= 0 && i + l / 2 < R && j - l / 2 >= 0 && j + l / 2 < C)
						{
							int totR = 0, totC = 0;
							for (int k = i - l / 2; k <= i + l / 2; k++)
								for (int q = j - l / 2; q <= j + l / 2; q++)
								{
									if (k == i - l / 2 && q == j - l / 2
									|| k == i + l / 2 && q == j - l / 2
									|| k == i - l / 2 && q == j + l / 2
									|| k == i + l / 2 && q == j + l / 2)
										continue;
									totR += num[k][q] * (i - k);
									totC += num[k][q] * (j - q);
								}
							//printf("%d %d %d %d %d\n", i, j, l, totR, totC);
							if (totR == 0 && totC == 0)
								ans = ans > l ? ans : l;
						}
					}
					else
					{
						if (i - l / 2 >= 0 && i + l / 2 - 1 < R && j - l / 2 >= 0 && j + l / 2 - 1 < C)
						{
							int totR = 0, totC = 0;
							for (int k = i - l / 2; k < i + l / 2; k++)
								for (int q = j - l / 2; q < j + l / 2; q++)
								{
									if (k == i - l / 2 && q == j - l / 2
									|| k == i + l / 2 - 1 && q == j - l / 2
									|| k == i - l / 2 && q == j + l / 2 - 1
									|| k == i + l / 2 - 1 && q == j + l / 2 - 1)
										continue;
									totR += num[k][q] * ((i - k) * 2 - 1);
									totC += num[k][q] * ((j - q) * 2 - 1);
								}
							//printf("%d %d %d %d %d\n", i, j, l, totR, totC);
							if (totR == 0 && totC == 0)
								ans = ans > l ? ans : l;
						}
					}
				}
			}
		}
		if (ans == 0)
			printf("Case #%d: IMPOSSIBLE\n", ++tcnt);
		else
			printf("Case #%d: %d\n", ++tcnt, ans);
	}	
	return 0;
}
