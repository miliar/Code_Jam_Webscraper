#include<cstdio>
#include<vector>
using namespace std;
int t,k,n,m,i,j,a[101][101],l;
void go(int i,int j,int x)
{
	if(i<=n && j<=m && a[i][j]!=-1) a[i][j]=(a[i][j]+x)%10007;

}
int main()
{
	freopen("Input.in","r",stdin);
	freopen("Output.out","w",stdout);
	scanf("%d ",&t);
	for(k=1;k<=t;k++)
	{
		memset(a,0,sizeof(a));
		scanf("%d %d",&n,&m);
		scanf("%d",&l);
		while(l--)
		{
			scanf("%d %d",&i,&j);
			a[i][j]=-1;
		}
		if(a[1][1]==0)
			a[1][1]=1;
		else
			a[1][1]=-1;
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
				if(a[i][j]>0)
				{
					go(i+1,j+2,a[i][j]);
					go(i+2,j+1,a[i][j]);
				}
		printf("Case #%d: %d",k,a[n][m]);
		printf("\n");
	}
	return 0;
}
