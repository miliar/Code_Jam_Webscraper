#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;
#define MAX 100

int mas[MAX];

int D, I, N, M;

int fm[MAX][256];
int f(int pos, int val)
{
	if (pos >= N)
		return 0;
	if (fm[pos][val] != -1)
		return fm[pos][val];
	else
	{
		int res = 2000000000;
		res = min(res, D + f(pos + 1, val));
		for (int i = 0; i < 256; i++)
			if (abs(val - i) <= M)
			{
				int a = abs(i - mas[pos]) + f(pos + 1, i);
				res = min(res, a);
			}
		if (M > 0)
		{
			for (int i = 0; i < 256; i++)
			{
				int q = abs(val - i);
				int k = q / M;
				if (q % M != 0)
					k++;
				k--;
				if (k < 0)
					k = 0;
				int a = k * I + abs(i - mas[pos]) + f(pos + 1, i);
				res = min(res, a);
			}
		}
		fm[pos][val] = res;
		return res;
	}
}

int main()
{
	freopen("B.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		for (int i = 0; i < MAX; i++)
			for (int j = 0; j < 256; j++)
				fm[i][j] = -1;
		scanf("%d%d%d%d", &D, &I, &M, &N);
		for (int i = 0; i < N; i++)
			scanf("%d", &mas[i]);
		int res = 2000000000;
		for (int i = 0; i < 256; i++)
		{
			res = min(res, f(0, i));
		}
		printf("Case #%d: %d\n", t+1, res);
	}
	fclose(stdout);
	return 0;
}