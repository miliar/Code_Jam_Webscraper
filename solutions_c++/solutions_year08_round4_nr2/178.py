#include<stdio.h>

int n,m,a;

int top;
int p[10001];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int A,B;
	int T1,T,i,j,k;

	top=0;
	for(i=2;i<=10000;i++)
	{
		for(j=1;j<=top;j++)
		{
			if(i%p[j]==0) break;
		}
		if(j==top+1) p[++top]=i;
	}
	scanf("%d",&T);
	for(T1=1;T1<=T;T1++)
	{
		scanf("%d%d%d",&n,&m,&a);

		int found=0;
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)
			{
				if(i*j>=a)
				{
					int rest=i*j-a;

					if(rest==0)
					{
						A=0;
						B=j;
						found=1;
						break;
					}
					else 
					{
						for(k=1;k<=n;k++)
						{
							if(rest%k==0) break;
						}
						A=k;
						B=j-rest/k;
						found=1;
						break;
					}
				}
			}
			if(found) break;
		}
		if(found) printf("Case #%d: 0 0 %d %d %d %d\n",T1,A,j,i,j-B);
		else printf("Case #%d: IMPOSSIBLE\n",T1);
	}
	return 0;
}
