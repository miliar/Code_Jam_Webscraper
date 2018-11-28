#include<iostream>
using namespace std;

int n,m,k,a[101][101],s[101][101];
int d[4][2]={{-1,0},{0,-1},{0,1},{1,0}};

bool ok(int x,int y) {
	if(x>0&&x<=n&&y>0&&y<=m)
		return true;
	else
		return false;
}

int dfs(int x,int y) {
	if(s[x][y]!=-1)
		return s[x][y];
	int i,x1,y1,t=10000000;
	bool yes=false;
	for(i=0;i<4;i++) {
		int xx=x+d[i][0],yy=y+d[i][1];
		if(ok(xx,yy)&&a[xx][yy]<a[x][y]) {
			yes=true;
			if(a[xx][yy]<t) {
				t=a[xx][yy];
				x1=xx;
				y1=yy;
			}
		}	
	}
	if(yes)
		return (s[x1][y1]=dfs(x1,y1));
	else
		return ++k;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("b.out","w",stdout);
	int t,num=0;
	scanf("%d",&t);
	while(t--) {
		int i,j;
		k=0;
		memset(s,-1,sizeof(s));
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
				scanf("%d",&a[i][j]);
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++) {
				s[i][j]=dfs(i,j);
			}
		printf("Case #%d:\n",++num);
		for(i=1;i<=n;i++) {
			for(j=1;j<=m;j++)
				printf("%c ",char(s[i][j]+'a'-1));
			printf("\n");
		}
	}
	return 0;
}
