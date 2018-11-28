#include <cstdio>
#include <cstring>

bool Find (char map[52][52], int x, int y, int K)
{
	int p;
	int q;

	p = x;
	q = y;
	for (int i = 0; i < K; i++)
	{
		if (map[p][q] != map[x][y])
			break;
		q++;
		if (i == K - 1)
			return true;
	}

	p = x;
	q = y;
	for (int i = 0; i < K; i++)
	{
		if (map[p][q] != map[x][y])
			break;
		q++;
		p++;
		if (i == K - 1)
			return true;
	}
	
	p = x;
	q = y;
	for (int i = 0; i < K; i++)
	{
		if (map[p][q] != map[x][y])
			break;
		p++;
		if (i == K - 1)
			return true;
	}

	if (y >= K - 1)
	{
		p = x;
		q = y;
		for (int i = 0; i < K; i++)
		{
			if (map[p][q] != map[x][y])
				break;
			q--;
			p++;
			if (i == K - 1)
				return true;
		}
	}

	return false;
}

int main ()
{
	int T, N, K;
	char map[52][52];
	char rotated[52][52];
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf ("%d", &T);
	for (int cas = 1; cas <= T; cas++)
	{
		scanf ("%d%d", &N, &K);
		memset(map, 0, sizeof(map));
		memset(rotated, '.', sizeof(rotated));

		for (int i = 0; i < N; i++)
			scanf ("%s", map[i]);

		for (int i = 0; i < N; i++)
		{
			int rot = N - 1;
			for (int j = N - 1; j >= 0; j--)
			{
				if (map[i][j] != '.')
				{
					rotated[i][rot] = map[i][j];
					rot--;
				}
			}
		}

		bool b = false;
		bool r = false;
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				if (rotated[i][j] == 'R' && r == false)
				{
					if (Find(rotated, i, j, K) == true)
					{
						r = true;
					}
				}
				if (rotated[i][j] == 'B' && b == false)
				{
					if (Find(rotated, i, j, K) == true)
					{
						b = true;
					}
				}
			}
		}
		if (b == true && r == true)
			printf ("Case #%d: Both\n", cas);
		else if (b == true && r == false)
			printf ("Case #%d: Blue\n", cas);
		else if (b == false && r == true)
			printf ("Case #%d: Red\n", cas);
		else if (b == false && r == false)
			printf ("Case #%d: Neither\n", cas);
	}
}
