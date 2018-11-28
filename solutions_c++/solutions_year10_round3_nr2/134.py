#include <cstdio>
#include <memory>

int L,P,C;
int memo[1100][1100];


int rec(int a, int b)
{
	if (a >= b)
		return 0;
	if (memo[a][b] != -1)
		return memo[a][b];
	int res = 1000000000;
	if (a*C >= b)
	{
		memo[a][b] = 1;
		return 1;
	}
	for (int i=a; i<b; i++)
	{
		int r1 = rec(a,i)+1;
		int r2 = rec(i*C,b)+1;
		int r = r1;
		if (r2 > r1)
			r = r2;
		if (r < res)
			res = r;
	}
	memo[a][b] = res;
	return res;
}

int rec2(int a, int b)
{
	int res = 1000000000;
	int factor = C;
	int curRes = 1;
	while (true)
	{
		int A = a*factor;
		int k = 0;
		while (A < b)
		{
			A *= C;
			k++;
		}
		int localRes = curRes;
		if (k > localRes)
			localRes = k;
		if (res > localRes)
			res = localRes;
		if (k <= curRes)
		{
			return res;
		}
		curRes++;
		factor*=C;
	}
	return 0;
}

int rec3(long long a, long long b)
{
	long long factor = 1;
	int ccount = 0;
	while (a*factor < b)
	{
		ccount++;
		factor*=C;
	}
	int koef = 1;
	int res = 0;
	while (koef < ccount)
	{
		koef *= 2;
		res++;
	}
	return res;
}


int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large_out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++)
	{
		scanf("%d%d%d", &L, &P, &C);
		memset(memo,-1,sizeof(memo));
		int res = 0;
		if (L*C < P)
		{
			res = rec3(L,P);
		}
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}