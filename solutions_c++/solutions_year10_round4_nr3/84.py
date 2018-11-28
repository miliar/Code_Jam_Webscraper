#include <stdio.h>
#include <string.h>

bool a[200][200],b[200][200],ok;
int ans,n,x1,y1,x2,y2,i,j,T,t;

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		memset(a,0,sizeof(a));
		scanf("%d",&n);
		while(n--)
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for(i=x1-1;i<x2;i++)
				for(j=y1-1;j<y2;j++)
					a[i][j]=1;
		}
		ans=0;
		while(1)
		{
			ans++;
			for(i=0;i<100;i++)
				for(j=0;j<100;j++)
					if(a[i][j])
						b[i][j]=i&&j&&(a[i-1][j] || a[i][j-1]);
					else
						b[i][j]=i&&j&&a[i-1][j]&&a[i][j-1];
			ok=0;
			for(i=0;i<100;i++)
				for(j=0;j<100;j++)
				{
					a[i][j]=b[i][j];
					ok|=a[i][j];
				}
			if(!ok)
				break;				
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}