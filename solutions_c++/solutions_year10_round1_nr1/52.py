#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int N, K;
char Buf[100][100], Map[100][100];

void Work()
{
	scanf("%d%d", &N, &K);
	for (int i = 0; i < N; i ++)
		scanf("%s", &Buf[i]);
	memset(Map, 0, sizeof(Map));
	for (int i = 0; i < N; i ++)
		for (int j = 0; j < N; j ++)
			Map[j][N - 1 - i] = Buf[i][j];
	for (int i = N - 1; i >= 0; i --)
		for (int j = 0; j < N; j ++)
		{
			int k = i + 1;
			while (k < N && Map[k][j] == '.')
			{
				swap(Map[k][j], Map[k - 1][j]);
				k ++;
			}
		}
	int R = 0, B = 0;
	for (int i = 0; i + K - 1 < N; i ++)
		for (int j = 0; j < N; j ++)
		{
			int OK = 1;
			for (int k = 1; k < K; k ++)
				if (Map[i][j] != Map[i + k][j])
					OK = 0;
			if (OK)
			{
				if (Map[i][j] == 'R')
					R = 1;
				if (Map[i][j] == 'B')
					B = 1;
			}
		}
	for (int i = 0; i < N; i ++)
		for (int j = 0; j + K - 1 < N; j ++)
		{
			int OK = 1;
			for (int k = 1; k < K; k ++)
				if (Map[i][j] != Map[i][j + k])
					OK = 0;
			if (OK)
			{
				if (Map[i][j] == 'R')
					R = 1;
				if (Map[i][j] == 'B')
					B = 1;
			}
		}
	for (int i = 0; i + K - 1 < N; i ++)
		for (int j = 0; j + K - 1 < N; j ++)
		{
			int OK = 1;
			for (int k = 1; k < K; k ++)
				if (Map[i][j] != Map[i + k][j + k])
					OK = 0;
			if (OK)
			{
				if (Map[i][j] == 'R')
					R = 1;
				if (Map[i][j] == 'B')
					B = 1;
			}
		}
	for (int i = 0; i + K - 1 < N; i ++)
		for (int j = K - 1; j < N; j ++)
		{
			int OK = 1;
			for (int k = 1; k < K; k ++)
				if (Map[i][j] != Map[i + k][j - k])
					OK = 0;
			if (OK)
			{
				if (Map[i][j] == 'R')
					R = 1;
				if (Map[i][j] == 'B')
					B = 1;
			}
		}
	if (R && B)
		printf("Both\n");
	else if (R)
		printf("Red\n");
	else if (B)
		printf("Blue\n");
	else
		printf("Neither\n");
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
	{
		printf("Case #%d: ", Case);
		Work();
	}
	return 0;
}
