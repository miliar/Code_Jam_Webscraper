#include<iostream>
using namespace std;
int n,m;
int i[1000][1000];
char b[1000][1000],ch;
int get(int x,int y)
{
	if( x<0 || x>=n ) return 1000000;
	if( y<0 || y>=m ) return 1000000;
	return i[x][y];
}
char dfs(int x,int y)
{
	int mn;
	if( b[x][y]!=0 ) return b[x][y];
	mn=i[x][y];
	if( get(x-1,y)<mn ) mn=get(x-1,y);
	if( get(x,y-1)<mn ) mn=get(x,y-1);
	if( get(x,y+1)<mn ) mn=get(x,y+1);
	if( get(x+1,y)<mn ) mn=get(x+1,y);
	if( mn==i[x][y] )
	{
		b[x][y]=ch;
		ch++;
		return b[x][y];
	}
	if( get(x-1,y)==mn ) return b[x][y]=dfs(x-1,y);
	if( get(x,y-1)==mn ) return b[x][y]=dfs(x,y-1);
	if( get(x,y+1)==mn ) return b[x][y]=dfs(x,y+1);
	if( get(x+1,y)==mn ) return b[x][y]=dfs(x+1,y);
	return 0;
}
int main()
{
	int a,s;
int T,X;
scanf("%d",&T);
for(X=1;X<=T;X++)
{
	printf("Case #%d:\n",X);
	scanf("%d%d",&n,&m);
	for(a=0;a<n;a++) for(s=0;s<m;s++) scanf("%d",&i[a][s]);
	for(a=0;a<n;a++) for(s=0;s<=m;s++) b[a][s]=0;
	ch='a';
	for(a=0;a<n;a++)
	{
		for(s=0;s<m;s++)
		{
			dfs(a,s);
			printf("%c ",b[a][s]);
		}
		printf("\n");
	}
}
	return 0;
}
