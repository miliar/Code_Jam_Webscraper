#include <iostream>
using namespace std;

bool	a[1000][1000],b[1000][1000];
int	TEST,t,m,n,x1,y1,x2,y2,i,j,k,p;
bool	flag;


int	main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	
	scanf("%d",&TEST);
	for (int t=1;t<=TEST;++t)
	{
		n=100;
		scanf("%d",&m);
		memset(a,0,sizeof(a));
		for (i=1;i<=m;++i)
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for (j=x1;j<=x2;++j)
			for (k=y1;k<=y2;++k)
			a[j][k]=1;
		}
		for (p=0;;++p)
		{
			flag=1;
			for (i=1;i<=n && flag;++i)
			for (j=1;j<=n && flag;++j)
			if (a[i][j]) flag=0;
			if (flag) break;
			
			
			for (i=1;i<=n;++i)
			for (j=1;j<=n;++j)
			if (a[i][j])
			{
				if (!a[i-1][j] && !a[i][j-1]) b[i][j]=0; else
				b[i][j]=1;
			} else
			{
				if (a[i-1][j] && a[i][j-1]) b[i][j]=1; else
				b[i][j]=0;
			}
			for (i=1;i<=n;++i)
			for (j=1;j<=n;++j)
			a[i][j]=b[i][j];
		}
		printf("Case #%d: %d\n",t,p);
	}
	
	return 0;
}
