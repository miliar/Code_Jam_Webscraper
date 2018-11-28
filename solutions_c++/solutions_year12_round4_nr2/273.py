#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
#define MAX 1000

int L, W;
int N;
pair<int, int> rs[MAX];
pair<int, int> points[MAX];
pair<int, int> result[MAX];

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		scanf("%d%d%d", &N, &W, &L);
		for (int i = 0; i < N; i++)
		{
			int a;
			scanf("%d", &a);
			rs[i].first = a;
			rs[i].second = i;
		}
		sort(rs, rs + N);
		reverse(rs, rs + N);
		int i = 0;
		int x = 0;
		int h = 0;
		while (i < N)
		{
			if (x == 0)
			{
				points[i].first = x;
				points[i].second = W;
				h = rs[i].first;
				x = rs[i].first;
				i++;
				continue;
			}
			else
			{
				if (x + rs[i].first > L)
				{
					W -= h + rs[i].first;
					x = 0;
					continue;
				}
				else
				{
					int xx = x + rs[i].first;
					points[i].first = xx;
					points[i].second = W;
					x = x + rs[i].first * 2;
					int y = rs[i].first;
					i++;					
					while (i < N && rs[i].first * 2 + y <= h && W - y - rs[i].first >= 0)
					{
						points[i].first = xx;
						points[i].second = W - y - rs[i].first;
						y = y + rs[i].first * 2;
						i++;
					}

				}
			}
		}
		for (int i = 0; i < N; i++)
		{
			result[rs[i].second] = points[i];
		}
		printf("Case #%d:", t+1);
		for (int i = 0; i < N; i++)
			printf(" %d %d", result[i].second, result[i].first);
		printf("\n");
	}



	fclose(stdin);
	fclose(stdout);

	return 0;
}