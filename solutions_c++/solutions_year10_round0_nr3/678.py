#include <stdio.h>
#include <string.h>

int r, k, n;

#define MAX (1<<10)

int v[MAX];
int p[MAX];
long long int l[MAX];
int q[MAX];
long long int lq[MAX];
int foi[MAX];

int main()
{
	int t, cas;
	int i, j;
	long long resp;
	int ac;

	scanf("%d", &t);

	for (cas=1; cas<=t; cas++)
	{
		scanf("%d %d %d", &r, &k, &n);
		for (i=0; i<n; i++)
		{
			scanf("%d", &v[i]);
		}

		memset(foi, 0, sizeof(foi));

		if (n == 1)
		{
		printf("Case #%d: %lld\n", cas, r*(long long)v[0]);
			continue;
		}

//		ac = v[0];
		for (i=0, j=0; i<n; i++)
		{
			if (i==j)
			{
				ac = v[i];
				j++;
				j%=n;
			}
			for ( ;j!=i && ac+v[(j)%n]<=k; )
			{
//				printf("{%d}",j);
				ac += v[(j)%n];
				j++;
				j%=n;
			}
			l[i] = ac;
			ac-=v[i];
			p[i] = j;
//			printf("[%d,%d,%d]",i,j,l[i]);
		}
		

		resp = 0;
		for (i=0, j=0; i<r; i++)
		{
			if (foi[j])
			{
				break;
			}

			lq[j] = resp;
			q[j] = i;

			foi[j] = 1;
			resp += l[j];
//			printf("[%lld,%d]", l[j],p[j]);

			j=p[j];
		}

		if (i==r)
		{
			printf("Case #%d: %lld\n", cas, resp);
			continue;
		}

		long long int aux = (r-q[j])/(i-q[j]);

//		printf("[%lld],resp=%lld,lq=%lld", aux, resp, lq[j]);

		resp = lq[j] + aux*(resp-lq[j]);

		i = (i-q[j])*aux + q[j];

		for (; i<r; i++)
		{
			resp += l[j];
			j=p[j];
		}

		printf("Case #%d: %lld\n", cas, resp);


	}
	return 0;
}
