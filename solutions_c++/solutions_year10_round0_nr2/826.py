#include <stdio.h>
#include <stdlib.h>

int su;
__int64 data[11],work[11];

int comp(const void *a,const void *b)
{
	return *(int *)a-*(int *)b;
}

__int64 gcd(__int64 a,__int64 b)
{
	__int64 z;

	do {
		z=a%b;
		a=b; b=z;
	} while(z);
	return a;
}

int main()
{
	int i,C,t=0;
	__int64 l;

	freopen("B-small-attempt1.in","rt",stdin);
	freopen("output.txt","wt",stdout);
	for(scanf("%d",&C);C;C--) {
		scanf("%d",&su);
		for(i=1;i<=su;i++) scanf("%d",&data[i]);
		qsort(data+1,su,sizeof(data[1]),comp);
		for(i=1;i<su;i++) work[i]=data[i+1]-data[i];
		qsort(work+1,su-1,sizeof(work[1]),comp);
		i=1;
		while(work[i]==0 && i<=su-1) i++;
		
		l=work[i]; i++;
		while(i<=su-1) {
			l=gcd(l,work[i]);
			i++;
		}
		if(data[1]%l!=0) printf("Case #%d: %I64d\n",++t,(l-data[1]%l));
		else printf("Case #%d: %I64d\n",++t,0);
	}
	return 0;
}