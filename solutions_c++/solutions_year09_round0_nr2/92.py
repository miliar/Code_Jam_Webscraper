#include <iostream>
using namespace std;

const int dx[4]={-1,0,0,1};
const int dy[4]={0,-1,1,0};

int a[101][101];
bool b[101][101];
char f[101][101];
char c;
int i,j,k,m,n,t,p,i1,j1,v,tmp,x,y;
bool ok;

void dfs(int i, int j)
{
	if (b[i][j]) {c=f[i][j]; k--; return;}
	b[i][j]=true;
	
	ok=false;
	tmp=a[i][j];
	for (v=0; v<4; v++)
	{
		i1=i+dx[v];
		j1=j+dy[v];
		if (i1>=1 && j1>=1 && i1<=n && j1<=m) 
			if (a[i1][j1]<tmp)
			{
				x=i1;
				y=j1;
				tmp=a[i1][j1];
				ok=true;
			}
	}
	if (ok) dfs(x,y);
	f[i][j]=c;
	
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&t);
	for (p=1; p<=t; p++)
	{
		scanf("%d%d",&n,&m);
		for (i=1; i<=n; i++)
			for (j=1; j<=m; j++)
				scanf("%d",&a[i][j]);
		memset(b,false,sizeof(b));
		f[1][1]='a';
		k=0;
		for (i=1; i<=n; i++)
			for (j=1; j<=m; j++)
				if (!b[i][j]) {c='a'+k; k++; dfs(i,j);}
		
		printf("Case #%d:\n",p);
		for (i=1; i<=n; i++)
		{
			for (j=1; j<m; j++)
				printf("%c ",f[i][j]);
			printf("%c\n",f[i][m]);
		}
	}

//	system("pause");
	return 0;
}
