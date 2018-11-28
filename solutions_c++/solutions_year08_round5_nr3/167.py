#include <stdio.h>
#include <math.h>
#include <memory.h>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <queue>

using namespace std;

#define MAX 2048
int mas[10][MAX];
bool matr[10][10];
int N, M;


bool isCorrect(int a, int row)
{
	int prev = -100;
	int k = 0;
	while (a > 0)
	{
		if (a % 2 == 1)
		{
			if (k - prev < 2)
			{
				return false;
			}
			if (!matr[row][k])
			{
				return false;
			}
			prev = k;
		}
		a /= 2;
		k++;
	}
	
	return true;
}

bool compatible(int next, int prev)
{
	int k = 0;
	while (next > 0)
	{
		if (next % 2 == 1)
		{
			int l = k-1;
			int r = k+1;
			if (l >= 0 && ((1 << l)&prev) > 0 ) 
				return false;
			if (r < M && ((1 << r)&prev) > 0 )
				return false;
		}
		next/=2;
		k++;
	}
	return true;
}

int cnt(int a)
{
//	if (cnts[a] != -1)
//		return cnts[a];
	int res = 0;
	while (a > 0)
	{
		res += a % 2;
		a /= 2;
	}
//	cnts[a] = res;
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
		scanf("%d%d", &N, &M);
		for (int i = 0; i < N; i++)
		{
			char s[100];
			scanf("%s", s);
			for (int j = 0; j < M; j++)
				matr[i][j] = (s[j] == '.');
		}


		int MM = 1 << M;

		for (int i = 0; i < 10; i++)
			for (int j = 0; j < MAX; j++)
				mas[i][j] = 0;

		for (int i = 0; i < MM; i++)
			if (isCorrect(i, 0))
				mas[0][i] = cnt(i);

		for (int i = 1; i < N; i++)
		{
			for (int j = 0; j < MM; j++)
				if (isCorrect(j, i-1))
				{
					for (int k = 0; k < MM; k++)
						if (isCorrect(k, i) && compatible(k, j))
							mas[i][k] = max(mas[i][k], mas[i-1][j] + cnt(k));
				}
		}

		int res = 0;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < MM; j++)
				res = max(res, mas[i][j]);

		printf("Case #%d: %d\n", t+1, res);
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}