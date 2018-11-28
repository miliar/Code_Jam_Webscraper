#include<stdio.h>
#include<memory>
const int mod=10007;
int z[128][128];
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	int c,o,n,m,g,i,j,x,y;
	scanf("%d",&c);
	for(o=1;o<=c;o++)
	{
		scanf("%d%d%d",&n,&m,&g);
		memset(z,0,sizeof(z));
		while(g--)
		{
			scanf("%d%d",&x,&y);
			z[x][y]=-1;
		}
		z[1][1]=1;
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
				if(z[i][j]!=-1)
				{
					if(z[i+1][j+2]!=-1)
						z[i+1][j+2]=(z[i+1][j+2]+z[i][j])%mod;
					if(z[i+2][j+1]!=-1)
						z[i+2][j+1]=(z[i+2][j+1]+z[i][j])%mod;
				}
		printf("Case #%d: %d\n",o,z[n][m]);
	}
	return 0;
}


