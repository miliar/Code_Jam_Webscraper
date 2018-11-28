#include<cstdio>
#include<algorithm>
using namespace std;
#define N 103
const int dx[]={-1,0,0,1};
const int dy[]={0,-1,1,0};
const int dx1[]={-1,0,0,1,1,1,-1,-1};
const int dy1[]={0,-1,1,0,1,-1,1,-1};
short int a[N][N],n,m,b[N][N],f;
char c='a';
int num,nr;
struct uplever{short int val,x,y;}v[N*N];
bool compar(const uplever&a,const uplever&b)
{
	return a.val>b.val;
}
void dfs(short int x, short int y)
{
	int x1,y1;
	if (!b[x][y])
		b[x][y]=nr;
	else
	{
		nr=b[x][y];
		return;
	}
	short int minim=a[x][y],px=0,py=0;
	for (int i=0; i<4; ++i)
	{
		x1=dx[i]+x;
		y1=dy[i]+y;
		if (x1&&y1&&x1<=n&&y1<=m)
		{
			if (minim>a[x1][y1])
			{
				minim=a[x1][y1];
				px=x1;
				py=y1;
			}
		}
	}
	if (px)
	{
		dfs(px,py);
		b[x][y]=nr;
	}
}
void matrice()
{
	nr=0;
	for (int i=num; i; --i)
	{
		if (!b[v[i].x][v[i].y])
		{
			++nr;
			dfs(v[i].x,v[i].y);
		}
	}
}
void afis()
{
	++f;
	printf("Case #%hd:\n",f);
	for (int i=1; i<=n; ++i)
	{
		for(int j=1; j<=m; ++j)
			printf("%c ",a[i][j]);
		printf("\n");
	}
}
void dfs1(int x, int y,int z)
{
	b[x][y]=0;
	a[x][y]=c;
	int x1,y1;
	for (int i=0; i<8; ++i)
	{
		x1=dx1[i]+x;
		y1=dy1[i]+y;
		if (b[x1][y1]==z)
			dfs1(x1,y1,b[x1][y1]);
	}
}
void matrice1()
{
	c='a';
	for (int i=1; i<=n; ++i)
		for (int j=1; j<=m; ++j)
		{
			if (b[i][j])
			{
				dfs1(i,j,b[i][j]);
				++c;
			}
		}
}
void citire()
{
	freopen("uplever.in","r",stdin);
	freopen("uplever.out","w",stdout);
	short int t;
	scanf("%hd",&t);
	while (t--)
	{
		scanf("%hd%hd",&n,&m);
		num=0;
		for (int i=1; i<=n; ++i)
			for (int j=1; j<=m; ++j)
			{
				scanf("%hd",&a[i][j]);
				v[++num].val=a[i][j];
				v[num].x=i;
				v[num].y=j;
			}
		sort (v+1,v+1+num,compar);
		matrice();
		matrice1();
		afis();
	}
}
int main()
{
	citire();
	return 0;
}
