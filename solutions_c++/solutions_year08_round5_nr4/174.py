#include <stdio.h>
#include <math.h>
#include <memory.h>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <queue>

using namespace std;
#define MAX 110
long long matr[MAX][MAX];
bool allow[MAX][MAX];
int N, M, R;

#define MOD 10007

long long f(int x, int y)
{
	if (x < 1)
		return 0;
	if (y < 1)
		return 0;
	if (x == 1 && y == 1)
		return 1;
	if (matr[x][y] != -1)
		return matr[x][y];
	long long res = (f(x - 2, y - 1) + f(x - 1, y - 2))%MOD;
	matr[x][y] = res;
	return res;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		scanf("%d%d%d", &N, &M, &R);

		for (int i = 0; i < MAX; i++)
			for (int j = 0; j < MAX; j++)
			{
				allow[i][j] = true;
				matr[i][j] = -1;
			}

		for (int i = 0; i < R; i++)
		{
			int a, b;
			scanf("%d%d", &a, &b);
			matr[a][b] = false;
		}

		printf("Case #%d: %lld\n", t+1, f(N, M));

	}


	fclose(stdin);
	fclose(stdout);
	return 0;
}