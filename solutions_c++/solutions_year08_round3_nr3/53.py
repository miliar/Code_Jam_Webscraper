#include<stdio.h>

int n,m,X,Y,Z;
int a[500001],b[500001];
int f[500001];

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);

	int T1,T,i,j;
	scanf("%d",&T);
	for(T1=1;T1<=T;T1++)
	{
		scanf("%d%d%d%d%d",&n,&m,&X,&Y,&Z);
		for(i=0;i<=m-1;i++)
		{
			scanf("%d",&b[i]);
		}

		for(i=0;i<=n-1;i++)
		{
			a[i]=b[i%m];
			b[i%m]=((__int64)X*b[i%m]+(__int64)Y*(i+1))%Z;
		}

		int ans;
		ans=0;

		for(i=0;i<=n-1;i++)
		{
			f[i]=1;
			for(j=0;j<=i-1;j++)
			{
				if(a[i]>a[j]) f[i]=(f[i]+f[j])%1000000007;
			}
			ans=(ans+f[i])%1000000007;
		}

		printf("Case #%d: %d\n",T1,ans);
	}
	return 0;
}