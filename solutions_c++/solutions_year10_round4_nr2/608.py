#include <stdio.h>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

pair<int, int> del[10000];
pair<int, int> ins[10000];

#define MAX 1024

int costs[10][MAX];
int miss[MAX];
int P;

long long matr[12][12][MAX];

long long f(int start, int level, int buyed, int cnt, int current)
{
	if (level == P - 1)
	{
		if (miss[2*current] + buyed >= P && miss[2*current + 1] + buyed >= P)
			return 0;
		if (miss[2*current] + buyed + 1 >= P && miss[2*current + 1] + buyed + 1 >= P)
			return costs[level][current];
		return 1000000000;
	}

	bool ff = true;
	for (int i = start; i < start + cnt; i++)
	{		
		if (miss[i] + buyed < P)
		{
			ff = false;
			break;
		}
	}
	if (ff)
		return 0;

	if (matr[level][buyed][current] != -1)
		return matr[level][buyed][current];

	long long res1 = f(start, level + 1, buyed + 1, cnt / 2, current * 2) 
		+ f(start + cnt / 2, level + 1, buyed + 1, cnt / 2, current * 2 + 1) + costs[level][current];
	
	long long res2 = f(start, level + 1, buyed, cnt, current * 2) 
		+ f(start + cnt / 2, level + 1, buyed, cnt / 2, current * 2 + 1);

	long long res = min(res1, res2+1);
	matr[level][buyed][current] = res;
	return res;
}

int main()
{
	freopen("out.txt", "w", stdout);
	freopen("B-small-attempt2.in", "r", stdin);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		for (int i = 0; i < 12; i++)
			for (int k = 0; k < 12; k++)
			for (int j = 0; j < MAX; j++)
				matr[i][k][j] = -1;
		scanf("%d%", &P);
		int PP = 1 << P;
		for (int i = 0; i < PP; i++)
			scanf("%d", &miss[i]);
		for (int i = 0; i < P; i++)
		{
			int NN = 1 << (P - i - 1);
			for (int j = 0; j < NN; j++)
				scanf("%d", &costs[P - i - 1][j]);
		}
		long long res = f(0, 0, 0, 1 << P, 0);
		printf("Case #%d: %lld\n", t+1, res);
		
	}
	fclose(stdout);
	fclose(stdin);

	return 0;
}