#include<cstdio>
#include<vector>
using namespace std;
#define inf 0x7f7f7f7f
int t,k,n,m,i,j,a[20][20],x,y,ok;
char c;
void go(int i,int j,int x)
{
	if(a[i][j]!=-1 && a[i][j]>x)
	{
		a[i][j]=x;
		ok=1;
	}
}
int main()
{
	freopen("Input.in","r",stdin);
	freopen("Output.out","w",stdout);
	scanf("%d ",&t);
	for(k=1;k<=t;k++)
	{
		memset(a,0x7f,sizeof(a));
		scanf("%d %d",&n,&m);
		for(i=1;i<=n;i++)
			a[i][0]=a[i][m+1]=-1;
		for(i=1;i<=m;i++)
			a[0][i]=a[n+1][i]=-1;
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
			{
				scanf(" %c",&c);
				switch(c)
				{
				case 'O':
					a[i][j]=0;
					break;
				case 'X':
					x=i;
					y=j;
					break;
				case '#':
					a[i][j]=-1;
					break;
				}
			}

		do
		{
		ok=0;
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
				if(a[i][j]!=-1 && a[i][j]!=inf)
				{
					go(i+1,j,a[i][j]+1);
					go(i-1,j,a[i][j]+1);
					go(i,j+1,a[i][j]+1);
					go(i,j-1,a[i][j]+1);
					if(a[i-1][j]==-1 || a[i+1][j]==-1 || a[i][j-1]==-1 || a[i][j+1]==-1)
					{
						int k;
						k=i;
						while(a[k-1][j]!=-1) k--;
						go(k,j,a[i][j]+1);
						k=i;
						while(a[k+1][j]!=-1) k++;
						go(k,j,a[i][j]+1);
						k=j;
						while(a[i][k-1]!=-1) k--;
						go(i,k,a[i][j]+1);
						k=j;
						while(a[i][k+1]!=-1) k++;
						go(i,k,a[i][j]+1);
					}
				}
		}while(ok);
		printf("Case #%d: ",k);
		if(a[x][y]==inf)
			printf("THE CAKE IS A LIE");
		else
			printf("%d",a[x][y]);
		printf("\n");
	}
	return 0;
}
