#include <stdio.h>

int nfix[1024][1024], fact[1024];
double sol[1024];

void calcfact(int k)
{
	fact[0] = 1;
	for(int i = 1; i <= k; ++i)
	{
		fact[i] = i * fact[i - 1];
	}
}

int f(int k, int j)
{
	if(j < 0 || j > k)
	{
		return 0;
	}
	if(!nfix[k][j])
	{
		nfix[k][j] = f(k - 1, j - 1) + f(k - 1, j) * (k - 1 - j) + f(k - 1, j + 1) * (j + 1);
	}
	return nfix[k][j];
}

double s(int misplaced)
{
	double sum = fact[misplaced];
	if(!sol[misplaced])
	{
		for(int i = 1; i <= misplaced - 2; ++i) 
		{
			sum += nfix[misplaced][i] * s(misplaced - i); 
		}
		sol[misplaced] = sum / (fact[misplaced] - nfix[misplaced][0]);
	}
	return sol[misplaced];
}

int main()
{
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	/*calcfact(10);
	nfix[0][0] = 1;
	for(int i = 10; i >= 0; --i)
	{
		f(10, i);
	}

	printf("%d\n", nfix[4][0]);
	sol[2] = 2;
	s(10);
	for(int i = 2; i <= 10; ++i)
	{
		printf("%lf\n", sol[i]);
	}*/

	int t, n, a;
	scanf("%d", &t);

	for(int test = 1; test <= t; ++test)
	{
		scanf("%d", &n);
		double sol = 0;
		for(int i = 1; i <= n; ++i)
		{
			scanf("%d", &a);
			if(a != i)
			{
				++sol;
			}
		}
		printf("Case #%d: %.6lf\n", test, sol);
	}
	

	return 0;
}
