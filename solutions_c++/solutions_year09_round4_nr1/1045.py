#include <stdio.h>
#include <stdlib.h>
#define maxn 50

int n;
int a[maxn][maxn];

int solve()
{
	int i,j,k;
	int b[maxn];
	int ans=0;
	int tmp;
	int flag;
	
	for(i=1;i<=n;i++)
	{
		j=n;
		while(a[i][j]==0&&j>0)
			j--;
		b[i]=j;
	}
	/*
	printf("\n");
	for(i=1;i<=n;i++)
		printf("%d ",b[i]);
	printf("\n");
	*/		
	//flag=0;
	for(i=1;i<=n;i++)
	{
		if (b[i]>i)
		{
			flag=0;
			for(j=i+1;j<=n;j++)
			{
				if (b[j]<=i)
				{
					flag=j;
					break;
				}
			}
			
			//printf("flag %d\n",flag);
			
			for(j=flag;j>=i+1;j--)
			{
				tmp=b[j-1];
				b[j-1]=b[j];
				b[j]=tmp;
				ans++;
			}
		}
	}
	/*
	printf("\n");
	for(i=1;i<=n;i++)
		printf("%d ",b[i]);
	printf("\n");
	*/
	//printf("Ans:");
	
	printf("%d\n",ans);
	
	return 0;
}

int main()
{
	int kc,kn;
	char str[maxn];
	int i,j;
	
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	
	scanf("%d",&kc);
	for(kn=1;kn<=kc;kn++)
	{
		printf("Case #%d: ",kn);
		scanf("%d",&n);
		for(i=1;i<=n;i++)
		{
			scanf("%s",str);
			for(j=1;j<=n;j++)		
				a[i][j]=str[j-1]-'0';
		}
		solve();
	}
	
	return 0;
}