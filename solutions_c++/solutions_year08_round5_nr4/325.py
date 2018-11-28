#include <cstdio>
#define mod 10007
#define nmax 100

int ans[nmax][nmax];
bool rock[nmax][nmax];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,T,n,m,i,j,k,ii,jj;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d%d%d",&n,&m,&k);
		for(i=0;i<n;i++)
			for(j=0;j<m;j++) rock[i][j]=ans[i][j]=0;
		while(k--)
		{
			scanf("%d%d",&i,&j);
			rock[i-1][j-1]=true;
		}
		ans[0][0]=1;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
			{
				ii=i+2;
				jj=j+1;
				if (ii<n&&jj<m && !rock[ii][jj]) ans[ii][jj]=(ans[i][j]+ans[ii][jj])%mod;
				ii=i+1;
				jj=j+2;
				if (ii>=n||jj>=m) continue;
				if (rock[ii][jj]) continue;
				ans[ii][jj]=(ans[i][j]+ans[ii][jj])%mod;
			}
		printf("Case #%d: %d\n",t,ans[n-1][m-1]);
	}
	return 0;
}