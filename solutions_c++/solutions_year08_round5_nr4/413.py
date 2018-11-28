#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int d[101][101];
bool mk[101][101];
int main()
{
	int m,r,n,x,y,ii,k,j,may,ans,cs,css,i,need,l;
	char last;
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	scanf("%d",&cs);
	for(css=1;css<=cs;css++)
	{
		scanf("%d%d%d",&n,&m,&r);
		memset(d,0,sizeof(d));
		memset(mk,0,sizeof(mk));
		while(r--)
		{
			scanf("%d%d",&x,&y);
			mk[x][y]=true;
		}
		d[1][1]=1;
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
			{
				if(i>=3&&j>=2&&mk[i-2][j-1]==false)d[i][j]+=d[i-2][j-1];
				if(i>=2&&j>=3&&mk[i-1][j-2]==false)d[i][j]+=d[i-1][j-2];
				d[i][j]%=10007;
			}
		printf("Case #%d: %d\n",css,d[n][m]);
	}
	return 0;
}
