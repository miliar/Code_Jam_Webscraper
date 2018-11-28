#include <iostream>

const int maxN = 1000;

int C, N;
int t[maxN+1], s[maxN+1];
int y, T;

int gcd(int p, int r)
{
	int a, b, t;

	a = p;
	b = r;
	
	while(a != 0)
	{
		t = a;
		a = b % a;
		b = t;
	}
	return b;
}

int non_neg(int p)
{
	if(p < 0) return -p;
	else return p;
}

void work(void)
{
	int a, b;

	if(N == 2)
	{
		a = gcd(t[1], t[2]);
		b = non_neg(t[1]-t[2]);
		if(a > b) T = a;
		else T = b;
	}
	if(N == 3)
	{
		a = non_neg(t[1]-t[2]);
		b = non_neg(t[2]-t[3]);
		T = gcd(a, b);
	}
	
}

int main()
{
	int i, j;

	freopen("warning.in", "r", stdin);
	freopen("warning.out", "w", stdout);
	scanf("%d", &C);
	for(i=1; i<=C; i++)
	{
		scanf("%d", &N);
		for(j=1; j<=N; j++)
			scanf("%d", &t[j]);
		work();
		if(t[1] % T == 0) y = 0;
		else y = T - t[1] % T;
		printf("Case #%d: %d\n", i, y);
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}