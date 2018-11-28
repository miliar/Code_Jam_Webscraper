#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a,const void *b)
{
	return *(int *)a - *(int *)b;
}

int main()
{
	int n,i;
	int cas,asd;
	__int64 a[1002],b[1002],count;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&cas);
	for(asd=0;asd<cas;asd++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%I64d",&a[i]);
		for(i=0;i<n;i++)
			scanf("%I64d",&b[i]);
		qsort((void *)a,n,sizeof(a[0]),cmp);
		qsort((void *)b,n,sizeof(b[0]),cmp);
		count=0;
		for(i=0;i<n;i++)
			count += a[i] * b[n-i-1];
		printf("Case #%d: %I64d\n",asd+1,count);
	}
	return 0;
}