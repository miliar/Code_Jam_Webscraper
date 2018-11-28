#include <iostream>
using namespace std;

int a[101][101];
bool b[101][101];
int n,m;

int main()
{
	//freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	int nn;
	scanf("%d",&nn);
	int i,j,ii,x,y,t;
	for(ii=1;ii<=nn;ii++)
	{
		scanf("%d%d%d",&n,&m,&t);
		memset(a,0,sizeof(a));
		a[1][1]=1;
		memset(b,0,sizeof(b));
		for(i=0;i<t;i++)
		{
			scanf("%d%d",&x,&y);
			b[x][y]=true;
		}
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
			{
				x=i-1;
				y=j-2;
				if(x>0&&y>0&&!b[x][y])
				{
					a[i][j]=(a[i][j]+a[x][y])%10007;
				}
				x=i-2;
				y=j-1;
				if(x>0&&y>0&&!b[x][y])
				{
					a[i][j]=(a[i][j]+a[x][y])%10007;
				}
			}
		printf("Case #%d: %d\n",ii,a[n][m]);
	}
	return 0;
}