#include<cstdio>
#define max 1500

int main()
{


	long T,N,a[max],i,j,C,sum,lowest;
	
	freopen("C-small-attempt0.in","r",stdin);
	freopen("outC0.out","w",stdout);
	scanf("%ld",&T);

	C=0;
	while(T--)
	{
		scanf("%ld",&N);

		for(i=0;i<N;i++) scanf("%ld",&a[i]);

		lowest=10000000;

		sum=0;
		j=0;
		for(i=0;i<N;i++)
		{
			sum^=a[i];
			if(lowest>a[i])
				lowest=a[i];
			j+=a[i];
		}

		if(sum==0)
		{
			printf("Case #%ld: %ld\n",++C,j-lowest);
		}
		else
		{
			printf("Case #%ld: NO\n",++C);
		}

	}
	return 0;
}