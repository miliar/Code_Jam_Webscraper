#include<cstdio>
#include<cstring>

int R,C,D;
char w[600][600];
int S[600][600];
int B[600][600];

int DeltaX(int i, int j , int x, int y , int k)
{
	return B[i][j] * (i + i - x - x + 1 - k);
}

int DeltaY(int i, int j , int x, int y , int k)
{
	return B[i][j] * (j + j - y - y + 1 - k);
}

int SUM(int x1, int y1, int x2, int y2)
{
	if (x1 > x2 || y1 > y2) return 0;
	return S[x2][y2] - S[x2][y1 - 1] - S[x1 - 1][y2] + S[x1 - 1][y1 - 1];
}


int cal()
{
	int ans = -1;
	memset( S, 0 , sizeof(S));
	for (int i = 1; i <= R; ++i)
		for (int j = 1; j <= C; ++j)
		{
			B[i][j] = w[i][j] - '0';
			S[i][j] = S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1] + B[i][j];
		}
	for (int k = 3; k <= R && k <= C; ++k)
	{
		for (int x = 1; x + k - 1 <= R && ans < k; ++x)
		{
			int y = 1;
			if (y + k - 1 > C) break;
			int sumX = 0;
			int sumY = 0;
			for (int i = x; i <= x + k - 1; ++i)
				for (int j = y; j <= y + k - 1; ++j)
				{
					if ((i == x && j == y) || (i == x + k - 1 && j == y) || (i == x && j == y + k - 1) || (i == x + k - 1 && j == y + k - 1)) continue;
					sumX += DeltaX(i, j, x, y, k);
					sumY += DeltaY(i, j, x, y, k);
				}
			if (sumX == 0 && sumY == 0)
			{
				ans = k;
				break;
			}
			for (y = 2; y + k - 1 <= C; ++y)
			{
				sumX -= DeltaX(x, y, x, y - 1 , k) + DeltaX(x + k - 1, y, x , y - 1, k);
				sumY -= DeltaY(x, y, x, y - 1 , k) + DeltaY(x + k - 1, y, x , y - 1, k);
				sumX += DeltaX(x, y + k - 2, x, y , k) + DeltaX(x + k - 1, y + k - 2, x , y, k);
				sumY += DeltaY(x, y + k - 2, x, y , k) + DeltaY(x + k - 1, y + k - 2, x , y, k);

				sumY -= SUM(x + 1, y - 1 , x + k - 2, y - 1) * (1 - k);
				sumY += SUM(x + 1, y + k - 1 , x + k - 2, y + k - 1) * (k - 1);

				sumY -= SUM(x + 1, y , x + k - 2, y + k - 2) * 2;
				sumY -= SUM(x, y + 1 , x, y + k - 3) * 2;
				sumY -= SUM(x + k - 1, y + 1 , x + k - 1, y + k - 3) * 2;

				if (sumX == 0 && sumY == 0)
				{
//					printf("%d %d %d %d %d\n", sumX,sumY, x, y, k);
					ans = k;
					break;
				}
			}
		}

	}
	return ans;
}

int BruteForce()
{
	int ans = -1;
	for (int k = 3; k <= R && k <= C; ++k)
	{
		for (int x = 1; x + k - 1 <= R && ans < k; ++x)
		{
			for (int y = 1; y + k - 1 <= C && ans < k; ++y)
			{
				int sumX = 0;
				int sumY = 0;
				for (int i = x; i <= x + k - 1; ++i)
					for (int j = y; j <= y + k - 1; ++j)
					{
						if ((i == x && j == y) || (i == x + k - 1 && j == y) || (i == x && j == y + k - 1) || (i == x + k - 1 && j == y + k - 1)) continue;
						sumX += DeltaX(i, j, x, y, k);
						sumY += DeltaY(i, j, x, y, k);
					}
				if (sumX == 0 && sumY == 0)
				{
					ans = k;
					break;
				}

			}
		}
	}
	return ans;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt" ,"w", stdout);

	int cases;
	scanf("%d" , &cases);
	for (int ca = 1; ca <= cases; ++ca)
	{
		scanf("%d%d%d", &R, &C, &D);
		for (int i = 1; i <= R; ++i) scanf("%s" , w[i] + 1);

		int ans = cal();
		printf("Case #%d: ", ca );
//		if (ans == -1) puts("IMPOSSIBLE"); else printf("%d ",   ans);

		ans = BruteForce();
//		printf("%d\n",BruteForce());
		if (ans == -1) puts("IMPOSSIBLE"); else printf("%d\n",   ans);

	}
}
