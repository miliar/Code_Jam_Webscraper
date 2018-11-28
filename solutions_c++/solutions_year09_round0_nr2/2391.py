#include<iostream>
#include<cstring>
#define F(i,n) for( i = 1; i <=(int)n;i++)

using namespace std;

int m, n;
int a[105][105];
const int inf = 1<<25;
int dy[]={0,-1,1,0};
int dx[]={-1,0,0,1};
char d[105][105];
char fill( int x, int y, char c)
{
	if(d[x][y]) 
		return d[x][y];
	int k;
	int s = a[x][y];
	int xx;
	int yy;
	int sk=5;
	for(k=0;k<4;k++) 
	{
		xx=x+dx[k];
		yy=y+dy[k];
		if( a[xx][yy] < s) 
		{
			s=a[xx][yy];
			sk=k;
		}
	}
	if(sk!=5)
		d[x][y] = fill(x+dx[sk],y+dy[sk],c);
	else d[x][y] = c;
	return d[x][y];
}
int main()
{
	int i, j, t, tt;
	scanf("%d",&tt);
	F(t,tt)
	{
		memset(a,10,sizeof(a));
		memset(d,0,sizeof(d));
		char s = 'a';
		scanf("%d%d",&m,&n);
		F(i,m)
			F(j,n)
			scanf("%d",&a[i][j]);
		F(i,m)
			F(j,n)
			{
				if(!d[i][j])
					if(fill(i,j,s)==s) s++;
			}
		printf("Case #%d:\n",t);
		F(i,m)
		{
			F(j,n)
				printf("%c ",d[i][j]);
			printf("\n");
		}
	}
	return 0;
}
