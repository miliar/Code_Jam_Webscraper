#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

#define MAX (1<<20)

int v[MAX];
int a[MAX];

int fc (const void *e1, const void *e2)
{
	int a1, a2;
	
	a1 = *((int*)e1);
	a2 = *((int*)e2);
	
	return a2-a1;
}

int main()
{
	int cas, casos;
	int i, l, n, t, c, soma, j, r1, r2, somatot;
	
	scanf("%d", &casos);
	
	for (cas = 1; cas <= casos; cas++)
	{
		printf("Case #%d: ", cas);
		scanf("%d %d %d %d", &l, &t, &n, &c);
		
		for (i=0; i<c; i++)
		{
			scanf("%d", &a[i]);
		}
		
		somatot = 0;
		for (i=0; i<n; i++)
		{
			v[i] = a[i%c];
			somatot += v[i];
		}
		
		soma = 0;

		for (i=0; i<n; i++)
		{
			soma+= 2*v[i];
			if (soma >= t)
				break;
		}
		
		if (l == 0 || i==n)
		{
			printf("%d\n", 2*somatot);
			continue;
		}
		
		qsort(&v[i+1], n-i-1, sizeof(v[0]), fc);

		r1 = 2*somatot;
		for (j=0; j<l && i+j+1<n; j++)
		{
			r1 -= v[i+j+1];
		}

		r2 = 2*somatot;
		for (j=0; j<(l-1) && i+j+1<n; j++)
		{
			r2 -= v[i+j+1];
		}
		r2 -= (soma-t)/2;		

		if (r1 < r2)
		{
			printf("%d\n",r1);
		}
		else
			printf("%d\n",r2); 

	}
	
	
	return 0;
}
