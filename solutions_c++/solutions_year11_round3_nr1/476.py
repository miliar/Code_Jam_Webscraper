#include <iostream>
#include <cstdio>
using namespace std;

int tes,n,m;
char a[200][200];
int cov[200][200],t[200][200];

int solve()
{
	
		for (int i=1;i<=n;i++)
			for (int j=0;j<m;j++)
				if (!cov[i][j] && a[i][j]=='#')
				{
					if (j+1>m-1) return 0;
					if (i+1>n) return 0;
					if (a[i][j+1]!='#' || a[i+1][j]!='#' || a[i+1][j+1]!='#') return  0;
					cov[i][j]=cov[i+1][j]=cov[i][j+1]=cov[i+1][j+1]=1;
					t[i][j]=t[i+1][j+1]=1;
					t[i+1][j]=t[i][j+1]=2;
				}
		return 1;
}

int main()
{
	freopen("a.out","w",stdout);
	scanf("%d",&tes);
	for (int ttt=1;ttt<=tes;ttt++)
	{
		scanf("%d%d",&n,&m);
		for (int i=1;i<=n;i++) { scanf("%s",a[i]); }
		/*for (int i=0;i<=n;i++)
			for (int s=0;s<e[m];s++) f[i][s]=0;
		f[0][0]=1;
		for (int i=0;i<n;i++)
			for (int s=0;s<e[m];s++)
				if (f[i][s])
				{
					
				}*/
		for (int i=1;i<=n;i++)
			for (int j=0;j<m;j++)
				cov[i][j]=0;
		printf("Case #%d:\n",ttt);
		if (!solve()) printf("Impossible\n");
		else 
		{
			for (int i=1;i<=n;i++)
			{
				for (int j=0;j<m;j++)
					if (a[i][j]=='.') printf(".");
					else if (t[i][j]==1) printf("/");
					else if (t[i][j]==2) printf("\\");
				printf("\n");
			}
		}
	}
}
