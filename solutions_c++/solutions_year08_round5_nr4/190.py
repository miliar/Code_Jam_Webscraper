#include <stdio.h>

#define MAX 110

int tab[MAX][MAX];
int di[]={1,2},dj[]={2,1};

int solve(int n,int m)
{
	int i,j,k;
	int ni,nj;
	tab[0][0]=1;
	for(i=0;i<n;++i)
		for(j=0;j<m;++j)
		{
			tab[i][j]%=10007;
			for(k=0;k<2;++k)
			{
				ni=i+di[k];
				nj=j+dj[k];
				if(ni>0 && nj>0 && ni<n && nj<m && tab[i][j]>0 && tab[ni][nj]>=0)
					tab[ni][nj]+=tab[i][j];
			}
		}
	return tab[n-1][m-1]%10007;
}

int main()
{
	int n,m;
	int i,j,k;
	int cnt,t;
	int p;
	scanf("%d",&t);
	for(cnt=1;cnt<=t;++cnt)
	{
		scanf("%d %d %d",&n,&m,&p);
		for(i=0;i<n;++i)
			for(j=0;j<m;++j)
				tab[i][j]=0;
		for(k=0;k<p;++k)
		{
			scanf("%d %d",&i,&j);
			--i;--j;
			tab[i][j]=-1;
		}
		printf("Case #%d: %d\n",cnt,solve(n,m));
	}
	return 0;
}





