#include <stdio.h>
#include <string.h>
#define MAX 1024
typedef int bignum_t[MAX+1];
bignum_t sum;
#define DEPTH	10000
#define DIGIT	4
void add(bignum_t a,const unsigned long b)
{
	unsigned long i=1;
	for (a[1]+=b;
		a[i]>=DEPTH&&i<a[0];
		a[i+1]+=a[i]/DEPTH,a[i]%=DEPTH,i++);
	for (;a[a[0]]>=DEPTH;a[a[0]+1]=a[a[0]]/DEPTH,a[a[0]]%=DEPTH,a[0]++);
}
void _add(bignum_t a,const bignum_t b)
{
	int i;
	for (i=1;i<=b[0];i++)
		if ((a[i]+=b[i])>=DEPTH)
			a[i]-=DEPTH,a[i+1]++;
		if (b[0]>=a[0])
			a[0]=b[0];
		else
			for (;a[i]>=DEPTH&&i<a[0];a[i]-=DEPTH,i++,a[i]++);
			a[0]+=(a[a[0]+1]>0);
}


void write(const bignum_t a)
{
 	int i,j;
 	for (printf("%d",a[i=a[0]]),i--;i;i--)
  		for (j=DEPTH/10;j;j/=10)
 			printf("%d",a[i]/j%10);
	printf("\n");
}

int main()
{
	unsigned long R,K,T,times;
	unsigned long a[MAX],N,i,j;
	unsigned long flag,once,he;
	freopen("C-small-attempt0(2).in","r",stdin);
	freopen("3.out","w",stdout);
	memset(a,0,sizeof(a));
	scanf("%ld",&T);
	for (times=1; times<=T ; ++times)
	{
		memset(sum,0,sizeof(sum));
		sum[0] = 1;
		once = 0;
		scanf("%ld%ld%ld",&R,&K,&N);
		for (i=0; i<N; ++i)
			scanf("%d",&a[i]);
		flag = 0;
		he = 0;
		for (i=0; i<N; ++i)
		{
			he += a[i];
		}
		for (i=0; i<R; ++i)
		{
			once = 0;
			if (he <= K)
			{
				once = he;
			}
			else
			{
				for (j=0;once + a[flag] <= K && j<N;j++,flag++,flag %= N)
				{
					once += a[flag];
				}
			}
			add(sum,once);
		}
		printf("Case #%d: ",times);
		write(sum);
	}
	return 0;
}