#include <iostream>
#include <string.h>
#include <fstream>

using namespace std;

int map[102][102];
char ma[102][102],p;
int direction[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
int xm,ym;
ifstream fin("B-large.in");
ofstream fout("B-large.out");
void init()
{
	fin>>xm>>ym;
	memset(map,0,sizeof(map));
	memset(ma,' ',sizeof(ma));
	for (int i=1;i<=xm;++i)
		for (int j=1;j<=ym;++j)
			fin>>map[i][j];
}

void floodfill(int x,int y)
{
	if (ma[x][y]!=' ') return;
	int xx=0,yy=0,tx,ty;
	int q=map[x][y];
	for (int i=0;i<4;++i)
	{
		tx=x+direction[i][0];ty=y+direction[i][1];
		if (tx>0&&tx<=xm&&ty>0&&ty<=ym&&map[tx][ty]<q)
		{xx=tx;yy=ty;q=map[xx][yy];}
	}
	if (xx!=0) {floodfill(xx,yy);ma[x][y]=ma[xx][yy];}
	else {ma[x][y]=p;p++;}
}

void print(int nn)
{
	fout<<"Case #"<<nn<<':'<<endl;
	for (int i=1;i<=xm;++i)
	{
		fout<<ma[i][1];
		for(int j=2;j<=ym;++j)
			fout<<' '<<ma[i][j];
		fout<<endl;
	}
}

void solve()
{
	p='a';
	for (int i=1;i<=xm;++i)
		for (int j=1;j<=ym;++j)
	floodfill(i,j);
}

int main()
{
	int t,tt;
	fin>>t;
	tt=t;
	while (t-->0)
	{
		init();
		solve();
		print(tt-t);
	}
	return 0;
}