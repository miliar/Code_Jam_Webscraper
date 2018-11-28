#include <cstdio>

const int MAXN = 60;
char m[MAXN][MAXN];
char t[MAXN];

int N, K;

const int dx[] = {1, 0, 1, 1};
const int dy[] = {0, 1, 1, -1};

bool hasK(char piece)
{
	
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < N; ++j)
			for (int d = 0; d < 4; ++d)
				if (i + (K - 1) * dx[d] < N && j + (K - 1) * dy[d] < N && j + (K - 1) * dy[d] >= 0)
				{
					bool ok = true;
					for (int t = 0; t < K; ++t)
						if (m[i + dx[d] * t][j + dy[d] * t] != piece)
						{
							ok = false;
							break;
						}

					if (ok)
						return true;
				}

	return false;
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int tc = 0; tc < T; ++tc)
	{
		scanf("%d%d\n", &N, &K);
		for (int i = 0; i < N; ++i)
			scanf("%s\n", m[i]);

		for (int i = 0; i < N; ++i)
		{
			/*
			int count = 0;
			for (int j = N - 1; j >= 0; --j)
				if (m[i][j] == '.')
					++count;
				else
					break;
			for (int j = N - 1 - count; j >= 0; --j)
				m[i][j + count] = m[i][j];
			for (int j = 0; j < count; ++j)
				m[i][j] = '.';
			*/

			int n = 0;

			for (int j = 0; j < N; ++j)
			{
				if (m[i][j] != '.')
					t[n++] = m[i][j];
				m[i][j] = '.';
			}

			for (int j = 0; j < n; ++j)
				m[i][N - n + j] = t[j];
		}

		bool R = hasK('R');
		bool B = hasK('B');

		printf("Case #%d: ", tc + 1);
		if (R && B)
			printf("Both\n");
		else if (R)
			printf("Red\n");
		else if (B)
			printf("Blue\n");
		else
			printf("Neither\n");
		//for (int i = 0; i < N; ++i)
		//	printf("%s\n", m[i]);

		//for (int i = 0; i < N; ++i)
		//	printf("%s\n", m[i]);
	}


	return 0;
}
