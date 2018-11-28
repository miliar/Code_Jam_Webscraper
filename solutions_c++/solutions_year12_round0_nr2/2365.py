#include <stdio.h>

bool ok[100][2];
int sum[100];

int main()
{
	int T;
	scanf("%d", &T);

	for (int i = 0; i < T; i++)
	{
		int N, S, p;
		scanf("%d %d %d", &N, &S, &p);
		for (int k = 0; k < N; k++)
		{
			scanf("%d", &sum[k]);
			ok[k][0] = false;
			ok[k][1] = false;
		}

		for (int mode = 0; mode < 2; mode++)
		{
			int step = mode + 1;

			for (int k = 0; k < N; k++)
			{
				for (int a = 0; a <= 10; a++)
				{
					for (int b = a; b <= 10 && b <= a + step; b++)
					{
						for (int c = p; c <= 10 && c <= a + step; c++)
						{
							if (a + b + c != sum[k]) continue;
							ok[k][mode] = true;
						}
					}
				}
			}
		}

		int ans = 0;

		for (int k = 0; k < N; k++)
		{
			if (ok[k][0])
			{
					ans++;
					continue;
			}

			if (ok[k][1] && S > 0)
			{
				ans++;
				S--;
			}
		}

		printf("Case #%d: %d\n", i + 1, ans);
	}
}