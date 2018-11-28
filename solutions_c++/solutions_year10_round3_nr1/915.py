#include <stdio.h>
void solve(int nCase)
{
	int i,j;
	long a[1000],b[1000];
	int n;
	__int64 sum=0;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d %d",&a[i],&b[i]);
	}

	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			if(i!=j)
			{
				if((a[i]-a[j])*(b[i]-b[j])<0)
				{
					sum++;
				}
			}
		}
	}
	sum/=2;
	printf("Case #%d: %lld\n",nCase,sum);
}
int main()
{
	int i,nCase;
	freopen("A-large.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&nCase);
	for(i=1;i<=nCase;i++)
	{
		solve(i);
	}
	return 0;
}
