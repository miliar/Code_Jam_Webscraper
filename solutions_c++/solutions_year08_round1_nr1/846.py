#include<stdio.h>
#include<stdlib.h>

int v1[900],v2[900];

int cmp(const void* a,const void *b)
{
	return *(const int*)a - *(const int*)b;
}

int main()
{
	int T,n;
	int i,j;
	int sum;

	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);

	scanf("%d",&T);
	for(i=0;i<T;i++){
		scanf("%d",&n);
		for(j=0;j<n;j++){
			scanf("%d",&v1[j]);
		}
		for(j=0;j<n;j++){
			scanf("%d",&v2[j]);
		}
		qsort(v1,n,sizeof(int),cmp);
		qsort(v2,n,sizeof(int),cmp);

		sum = 0;
		for(j=0;j<n;j++){
			sum += v1[j]*v2[n-j-1];
		}
		printf("Case #%d: %d\n",i+1,sum);
	}
	return 0;
}