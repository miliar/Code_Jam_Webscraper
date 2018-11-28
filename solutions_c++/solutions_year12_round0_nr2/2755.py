#include<stdio.h>

void solveB()
{
	int t;
	int res;
	int n, s, p;
	int score;
	int max_score;
	scanf("%d\n", &t);
	for(int i = 1; i <= t; i++)
	{
		res = 0;
		scanf("%d%d%d", &n, &s, &p);
		for(int j = 0; j < n; j++)
		{
			scanf("%d", &score);
			if(score == 0 || score == 1)
			{
				if(score >= p)
					res += 1;
				continue;
			}
			max_score = score / 3;
			if(score % 3 != 0)
			{
				max_score += 1;
			}
			if(max_score >= p)
			{
				res += 1;
				continue;
			}

			if(s > 0)
			{
				max_score += 1;
				if(max_score >= p)
				{
					res += 1;
					s -= 1;
				}
			}

		}
		printf("Case #%d: %d\n", i, res);
	}
}

int main()
{
	solveB();
	return 0;
}