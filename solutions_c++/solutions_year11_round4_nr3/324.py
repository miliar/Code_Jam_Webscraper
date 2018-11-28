#include<stdio.h>
#include<math.h>
bool p[10000000];
bool q[10000000];
int prime[100000];
int r;
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.out","w",stdout);
	
	r=0;
	for(int i=2;i<=1000000;i++)
	{
		if(p[i]==0)
		{
			prime[r++]=i;
			for(int j=i+i;j<=1000000;j+=i) p[j]=1;
			for(long long j=i;j<=1000000;j*=i) q[j]=1;
		}
	}

	int tt;
	scanf("%d",&tt);
	for(int t=1;t<=tt;t++)
	{
		long long n;
		scanf("%I64d",&n);
		
		printf("Case #%d: ",t);
		if(n==1) printf("0\n");
		else
		{
			int a=0,b=1;
			for(int i=2;i<=n;i++) a+=(p[i]==0);
			for(int i=2;i<=n;i++)
			{b+=(q[i]==1);
//			printf("%d %d\n",i,q[i]);
		}
			
			printf("%d\n",b-a);
		}
	}

	return 0;
}
