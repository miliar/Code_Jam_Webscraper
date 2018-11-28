#include <stdio.h>
#include <string.h>
#define MAX 1024
int main()
{
	unsigned long R,K,T,times;
	unsigned long a[MAX],N,i,j;
	unsigned long once,flag;
	unsigned long sum;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("3.out","w",stdout);
	memset(a,0,sizeof(a));
	scanf("%ld",&T);
	for (times=1; times<=T ; ++times)
	{
		sum = 0;
		once = 0;
		scanf("%ld%ld%ld",&R,&K,&N);
		for (i=0; i<N; ++i)
			scanf("%d",&a[i]);
		flag = 0;
		for (i=0; i<R; ++i)
		{
			for (once=0,j=0;once + a[flag] <= K && j<N;j++,flag++,flag %= N)
			{
				once += a[flag];
			}
			sum += once;
		}
		printf("Case #%d: %d\n",times,sum);
	}
	return 0;
}