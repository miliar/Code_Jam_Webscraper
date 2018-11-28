#include<cstdio>
#include<cstring>

const int mx=110;

int n=102,r;
int a[mx][mx];

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("outC.txt","w",stdout);
	int i,j,k,t,ca=1;

	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&r);
		memset(a,0,sizeof(a));
		for(i=0;i<r;i++)
		{
			int p,q,c,d;
			scanf("%d%d%d%d",&p,&q,&c,&d);
			for(j=p;j<=c;j++)
			{
				for(k=q;k<=d;k++)
					a[k][j]=1;
			}
		}
		int cnt=0;
		while(1)
		{
			/*
			printf("in:\n");
			for(i=1;i<7;i++)
			{
				for(j=1;j<7;j++)
				{
					printf("%d ",a[i][j]);
				}printf("\n");
			}printf("\n");
			*/
			for(i=0;i<n;i++)
			{
				for(j=0;j<n;j++)
				{
					if(a[i][j]!=0)
						break;
				}
				if(j<n)break;
			}
			if(i>=n)break;
			cnt++;
			for(i=n-1;i>0;i--)
			{
				for(j=n-1;j>0;j--)
				{
					if(a[i-1][j]&&a[i][j-1])
						a[i][j]=1;
				}
			}
			for(i=n-1;i>0;i--)
			{
				for(j=n-1;j>0;j--)
				{
					bool flag=false;
					if(a[i-1][j])flag=true;
					if(a[i][j-1])flag=true;
					if(!flag)a[i][j]=0;
				}
			}
			/*
			printf("out\n");
			for(i=1;i<7;i++)
			{
				for(j=1;j<7;j++)
				{
					printf("%d ",a[i][j]);
				}printf("\n");
			}printf("\n");
			*/
		}
		printf("Case #%d: %d\n",ca++,cnt);
	}

	return 0;
}
