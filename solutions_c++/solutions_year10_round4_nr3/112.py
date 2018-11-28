#include <stdio.h>
#include <string.h>

int R;
bool bacteria[105][105], nbacteria[105][105];
bool alive;

int main()
{
//	freopen("C.in", "r", stdin);

	int C;
	scanf("%d", &C);

	for (int cas = 0; cas < C; ++cas)
	{
		scanf("%d", &R);

		memset(bacteria, false, sizeof(bacteria));
		alive = false;
		for (int i = 0; i < R; ++i)
		{
			int y1, x1, y2, x2;
			scanf("%d%d%d%d", &y1, &x1, &y2, &x2);
			for (int j = x1 - 1; j < x2; ++j)
				for (int k = y1 - 1; k < y2; ++k)
					bacteria[j][k] = alive = true;
		}

		int answer = 0;
	
		while (alive)
		{
			++answer;

			memset(nbacteria, false, sizeof(nbacteria));
			alive = false;

			for (int i = 0; i < 105; ++i)
				for (int j = 0; j < 105; ++j)
				{
					if (bacteria[i][j])
					{
						if ((i == 0 || !bacteria[i - 1][j]) && (j == 0 || !bacteria[i][j - 1]))
							nbacteria[i][j] = false;
						else
							nbacteria[i][j] = alive = true;
					}
					else
					{
						if (i > 0 && bacteria[i - 1][j] && j > 0 && bacteria[i][j - 1])
							nbacteria[i][j] = alive = true;
					}
				}
			memcpy(bacteria, nbacteria, sizeof(bacteria));
		}

		printf("Case #%d: %d\n", cas + 1, answer);
	}

	return 0;
}

