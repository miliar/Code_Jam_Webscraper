#include <string>
#include <vector>
#include <cmath>

#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include<fstream> 

using namespace std;

string res[102];
int a[102][102]={0};
int keyx[]={-1,0,0,1},keyy[]={0,-1,1,0};
char chk(int x,int y,int &asc)
{
	int vx=x,vy=y;
	if(res[x][y]!='#'){return res[x][y];}
	else
	{
		for(int i=0;i<4;i++)
		{
			if(a[x+keyx[i]][y+keyy[i]]<a[vx][vy]){vx=x+keyx[i];vy=y+keyy[i];}
		}
		if(vx!=x||vy!=y){res[x][y]=res[vx][vy];return chk(vx,vy,asc);}else {res[x][y]=('a'+asc);asc++;return ('a'+asc-1);}
	}
	return ('a'+asc);
}
int main()
{
	ofstream ofs; 
	ifstream ifs;
	ifs.open("d:\\Wraith\\B.in");
	ofs.open("d:\\Wraith\\b.out");
	int N,m,n;
	ifs>>N;
	for(int i=1;i<=N;i++)
	{		
		ofs<<"Case #"<<i<<":"<<endl;
		ifs>>m>>n;
		for(int x1=0;x1<=m+1;++x1)
		{
			a[x1][0]=100000;
			a[x1][n+1]=100000;
		}
			for(int y1=0;y1<=n+1;++y1)
			{
				a[0][y1]=100000;
				a[m+1][y1]=100000;
			}
		for(int x2=0;x2<102;++x2)
		{
			res[x2].clear();
			for(int y2=0;y2<102;++y2)
				res[x2]+='#';
		}
		for(int x=1;x<=m;++x)
		{
			for(int y=1;y<=n;++y)
			{
				ifs>>a[x][y];
			}
		}
		int asc=0;
		for(int X=1;X<=m;++X)
		{
			for(int Y=1;Y<=n;++Y)
			{
				res[X][Y]=chk(X,Y,asc);
			}
		}
		for(int X=1;X<=m;++X)
		{
			for(int Y=1;Y<=n;++Y)
			{
				if(Y!=1)ofs<<" ";ofs<<res[X][Y];
			}
			ofs<<endl;
		}
	}
	return 0;
}