#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

int cmp_fun(const void *a, const void *b)	{
	return *(int*)a - *(int*)b;
}

int main()	{
	int T=0;
	int A[1000],S[1000];
	scanf("%d",&T);
	for(int i=0; i!=T; ++i)	{
		int N=0,j,K=0;
		scanf("%d",&N);
		for(j=0; j!=N; ++j)
			scanf("%d",A+j);
		memcpy(S,A,N*sizeof(int));
		qsort(S,N,sizeof(int),cmp_fun);
		for(j=0; j!=N; ++j)	{
			K += (A[j]==S[j]?0:1);
		}
		printf("Case #%d: %d.000000\n",i+1,K);
	}
	return 0;
}

