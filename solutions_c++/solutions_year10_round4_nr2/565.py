#include <stdio.h>
#include <cstring>
#include <assert.h>

#define MAX (1<<10)
#define INF (0x3f)

int p, v[MAX];
int c[10][MAX];

int min(int a, int b)
{
	if (a < b)
	{
		return a;
	}
	return b;
}

int mm[MAX][MAX][10];

int calc(int a, int b, int comprado, int compet)
{
	if (compet == 1)
	{
//		assert(v[a]-comprado <= 1 && v[b]-comprado <= 1);
		if (comprado < p-v[a] || comprado < p-v[b])
		{
			return c[p-1][a/2];
		}
		else
			return 0;
	}

	if (mm[a][b][comprado]!= -1)
	{
		return mm[a][b][comprado];
	}

	int i;
	int menor = p;

	for (i=a; i<=b; i++)
	{
		if (menor > v[i])
		{
			menor = v[i];
		}
	}

	if (p-menor == compet+comprado)// compra
	{
//		printf("comprei %d %d %d\n", a, b, comprado);
		mm[a][b][comprado] = c[p-compet][a/(1<<compet)] + calc(a,(a+b)/2, comprado+1, compet-1)
									+ calc((a+b)/2+1,b, comprado+1, compet-1);
		return mm[a][b][comprado];
	}

	mm[a][b][comprado] = min (c[p-compet][a/(1<<compet)] + calc(a,(a+b)/2, comprado+1, compet-1)
									+ calc((a+b)/2+1,b, comprado+1, compet-1),
								calc(a,(a+b)/2, comprado, compet-1)
									+ calc((a+b)/2+1,b, comprado, compet-1));
	return mm[a][b][comprado];

}

int main()
{
	int t, cas;

	scanf("%d", &t);
	for (cas=1; cas<=t; cas++)
	{
		memset(mm, -1, sizeof(mm));
		printf("Case #%d: ",cas);
		scanf("%d", &p);
		int i, j, m = p;
		for (i=0; i<(1<<p); i++)
		{
			scanf("%d", &v[i]);
			if (v[i] < m)
			{
				m = v[i];
			}
		}

		memset(c, INF, sizeof(c));

		for (j=p-1; j>=0; j--)
		{

			for (i=0; i<(1<<j); i++)
			{
				scanf("%d", &c[j][i]);
			}
		}


		printf("%d\n", calc(0, (1<<p)-1, 0, p));

	
	}
	return 0;
}
