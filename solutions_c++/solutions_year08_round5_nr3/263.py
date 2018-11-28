#include <cstdio>
#define nmax 11

int ans[nmax][1<<nmax];
char board[20][20];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,T,n,m,i,j,k,l,x,a;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d%d",&n,&m);
		gets(board[0]);
		for(i=0;i<n;i++) gets(board[i]);
		for(i=1;i<=n;i++)
			for(j=0;j<(1<<m);j++) ans[i][j]=0;
		a=0;
		for(i=1;i<=n;i++)
			for(j=0;j<(1<<m);j++)
				for(k=0;k<(1<<m);k++)
				{
					for(l=0;l<m;l++)
						if (((1<<l)&k) && board[i-1][l]=='x') break;
					if (l<m) continue;
					for(l=1;l<m;l++)
						if (((1<<l)&k) && ((1<<(l-1))&k)) break;
					if (l<m) continue;
					for(l=0;l<m;l++)
						if (((1<<l)&k))
						{
							if (l && ((1<<(l-1))&j)) break;
							if (l<m-1 && ((1<<(l+1)&j))) break;
						}
					if (l<m) continue;
					for(l=0,x=0;l<m;l++)
						if ((1<<l)&k) ++x;
					if (ans[i][k]<ans[i-1][j]+x) ans[i][k]=ans[i-1][j]+x;
					if (ans[i][k]>a) a=ans[i][k];
				}
		printf("Case #%d: %d\n",t,a);
	}
	return 0;
}