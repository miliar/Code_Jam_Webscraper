#include <iostream>
#include <cstdio>
using namespace std;

const int N = 2000000;
int f[N+10][7];
int c[10];

void init()
{
	int i, j, k, x, y, l,  t1, t2;
    for (i=1; i<=N; i++)
	{
		l = 0;
		x = i;

		while (x) ++l, c[l]=x%10, x/=10;
		f[i][0] = 0;
		for (k=1; k<l; k++)
			if (c[k] > 0)
			{
				x = 0;
				for (t1=k; t1>0; t1--) x = x*10+c[t1];
				for (t2=l; t2>k; t2--) x = x*10+c[t2];
				if (x > i) f[i][++f[i][0]] = x;
			}
	}
/*
	for (i=1111; i<=1300; i++)
	{
		printf("%d   :   ", i);
		for (j=1; j<=f[i][0]; j++) printf("%d ", f[i][j]);
		printf("\n");
	}
	*/
}

void l_try()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int cs, a, b;
	scanf("%d", &cs);
	int now = 0;
	int ans, i, j;
	while (cs--)
	{
		scanf("%d%d", &a, &b);
		ans = 0;
		for (i=a; i<=b; i++)
			for (j=1; j<=f[i][0]; j++)
				if (f[i][j]<=b) ans++;
		printf("Case #%d: %d\n", ++now, ans);
	}
}



int main()
{
	init();
	l_try();
	return 0;
}