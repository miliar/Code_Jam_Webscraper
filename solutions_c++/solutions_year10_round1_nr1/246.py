#include <iostream>
using namespace std;

int dx[4]={-1,-1,0,1};
int dy[4]={0,1,1,1};
int t,i,j,k,kk,n,x,y,z;
char c;
bool okr,okb,ok;
int a[51][51];

void dfs(int x, int i, int j)
{
	int v,i1,j1,c;
	
	for (v=0; v<4; v++)
	{
		i1=i;
		j1=j;
		ok=true;
		for (c=1; c<kk; c++)
		{
			i1+=dx[v];
			j1+=dy[v];
			if (a[i1][j1]!=x) {ok=false; break;}
			if (!(i1>=1 && i1<=n && j1>=1 && j1<=n)) {ok=false; break;}
		}
		if (ok) return;
	}
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	for (z=1; z<=t; z++)
	{
		scanf("%d%d",&n,&kk);
		
		for (j=n; j>=1; j--)
		{
			for (i=1; i<=n; i++)
			{
				while (scanf("%c",&c)) if (c=='.' || c=='R' || c=='B') break;
				if (c=='.') a[i][j]=0;
				if (c=='R') a[i][j]=1;
				if (c=='B') a[i][j]=2;
			}
		}
		
		for (j=1; j<=n; j++)
			for (i=n; i>=1; i--)
				if (a[i][j]==0)
					for (k=i-1; k>=1; k--)
						if (a[k][j]!=0)
						{
							a[i][j]=a[k][j];
							a[k][j]=0;
							break;
						}
		
		okr=okb=false;
		for (i=1; i<=n; i++)
			for (j=1; j<=n; j++)
			{
				ok=false;
				if (!okr && a[i][j]==1) {dfs(a[i][j],i,j); okr=ok;}
				if (!okb && a[i][j]==2) {dfs(a[i][j],i,j); okb=ok;}
			}
		printf("Case #%d: ",z);
		if (okr && okb) printf("Both");
		if (okr && !okb) printf("Red");
		if (!okr && okb) printf("Blue");
		if (!okr && !okb) printf("Neither");
		printf("\n");
	}
	
//	system("pause");
	return 0;
}
