#include <iostream>
#include <stdlib.h>
using namespace std;
int cmp(const void *a,const void *b)
{
	return *(long long *)b-*(long long  *)a;
}
int main()
{
	int aCase;
	long long sum;
	int i,j;
	long long a[3],b[1100];
	scanf("%d",&aCase);
	for(int tt=1;tt<=aCase;tt++)
	{
		scanf("%lld%lld%lld",&a[0],&a[1],&a[2]);
		sum=0;
		if(a[0]*a[1]<a[2])
		{
			printf("Impossible\n");
			continue;
		}
		for(int i=0;i<a[2];i++)
			scanf("%lld",&b[i]);
		qsort(b,a[2],sizeof(b[0]),cmp);
		for(int i=0;i<a[2];i++)
			sum+=(i/a[1]+1)*b[i];
		printf("Case #%d: %lld\n",tt,sum);
	}
	return 0;
}
