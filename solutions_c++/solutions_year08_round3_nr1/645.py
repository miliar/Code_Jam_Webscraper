#include<stdio.h>
#include<math.h>
#include<stdlib.h>

long n;
long p;
long k;
long l;
long freq[1001];
long res=0;

static int comp(const void *p, const void *q)
{
	if((*(int*)p)>(*(int*)q))
		return -1;
	
	return 1;
}

int main()
{
	int i,j,k;

	scanf("%ld", &n);

	for(i=0; i<n; i++)
	{
		res = 0;
		scanf("%ld%ld%ld", &p, &k, &l);
		for(j=0; j<l; j++)
		{
			scanf("%ld", &freq[j]);
		}
		qsort(freq, l, sizeof(long), comp);

		long ct=0;
		long actanz=1;
		for(j=0; j<l; j++)
		{
			if(ct<k)
			{
				res += freq[j]*actanz;
				ct++;
			}
			else
			{
				ct = 1;
				actanz++;
				res += freq[j]*actanz;
			}
		}
		printf("Case #%d: %ld\n", i+1, res);
	}

	return 0;
}
