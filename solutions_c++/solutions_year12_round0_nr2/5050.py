#include <iostream>
#include <string>
#define MAX_N 110
using namespace std;

int score[MAX_N];

int ans;
int N, S, P;

// get the max score
int GetMaxScore(int total, bool s)
{
	int maxPoint = 0;
	if (s)
	{
		maxPoint = total / 3 + 1;
		if (total % 3 == 2)
			++maxPoint;
		if (total < 2)
			maxPoint = -1;           //no solution
	}
	else
	{
		maxPoint = total / 3;
		if (total % 3)
			++maxPoint;
	}
	return maxPoint;
}

void Solve(int x, int s, int cnt)
{
	if (x == N)
	{
		if (cnt > ans && s == S)
			ans = cnt;
		return;
	}
	if (s > S)
		return;

	// not surprising
	int maxScore = GetMaxScore(score[x], false);
	if (maxScore != -1)
		Solve(x + 1, s, cnt + (maxScore >= P));

	maxScore = GetMaxScore(score[x], true);
	if (maxScore != -1)
		Solve(x + 1, s + 1, cnt + (maxScore >= P));
}


int main()
{
	int t;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	while (scanf("%d", &t) != EOF)
	{
		for (int i = 1; i <= t; ++i)
		{
			ans = 0;
			scanf("%d%d%d", &N, &S, &P);
			for (int j = 0; j < N; ++j)
			{
				scanf("%d", &score[j]);
			}
			Solve(0, 0, 0);
			printf("Case #%d: ", i);
			printf("%d\n", ans);
		}
	}

	return 0;
}


/*
Input
4
3 1 5 15 13 11
3 0 8 23 22 21
2 1 1 8 0
6 2 8 29 20 8 18 18 21



Output
Case #1: 3
Case #2: 2
Case #3: 1
Case #4: 3
*/