#include<iostream>
#include<fstream>
#include<climits>
using namespace std;

char map[1000][1000];
int h[1000][1000];
int H,W;
char basen ;
void Union( char a, char b)
{
	if ( a > b)
		a^= b ^= a ^= b;
	for(int i=1;i<=H;i++)
		for(int j=1;j<=W;j++)
			if( map[i][j] > b )
				map[i][j] --;
			else if( map[i][j] == b)
				map[i][j] = a;
	basen--;
}

void flow( int x,int y)
{
	int n,w,e,s;
	n = h[x-1][y];
	w = h[x][y-1];
	e = h[x][y+1];
	s = h[x+1][y];
	if(x-1>0 &&  n<h[x][y] && n <= w && n <= e && n<=s )
		map[x][y] = map[x-1][y];
	else if( y-1>0 && w<h[x][y] &&  w<n && w<=e && w<=s )
		map[x][y] = map[x][y-1];
	else if(  y+1 <W+1&& e < h[x][y] && e<n && e<w && e<=s)
		map[x][y] = map[x][y+1];
	else if( x+1 < H+1 && s < h[x][y] && s<n && s<w && s<e)
		map[x][y] = map[x+1][y];
}

void color(int x,int y)
{
	int n,w,e,s;
	n = h[x-1][y];
	w = h[x][y-1];
	e = h[x][y+1];
	s = h[x+1][y];
	int M=-1,N=-1;
	char tmp=map[x][y];
	if( x-1 > 0 && n<h[x][y] && n <= w && n <= e && n<=s )
	{
		tmp = map[x-1][y];
		M = x-1;
		N = y;
	}
	else if( y-1>0 &&  w<h[x][y] &&  w<n && w<=e && w<=s )
	{
		tmp = map[x][y-1];
		M = x;
		N = y-1;
	}
	else if( y+1 <W+1 && e < h[x][y] && e<n && e<w && e<=s)
	{
		tmp = map[x][y+1];
		M = x;
		N = y+1;
	}
	else if(  x+1 < H+1 && s < h[x][y] && s<n && s<w && s<e)
	{
		tmp = map[x+1][y];
		M = x+1;
		N = y;
	}
	if( tmp!=0 && tmp != map[x][y] )
		Union( tmp ,map[x][y] );
	if( M!=-1 && N!=-1)
	{	
		if( tmp != 0 )
			map[M][N] = tmp < map[x][y] ? tmp : map[x][y];
		else
			map[M][N] = map[x][y];
	}
}

int main()
{
	ofstream fout("out");
	int testcase;
	cin >> testcase;
	for(int k=0;k<testcase;k++)
	{
		cin >> H >> W;
		for(int i=0;i<=H;i++)
			for(int j=0;j<=W;j++)
				map[i][j] = 0;
		for(int i=0;i<=W+1;i++)
			h[0][i] = h[H+1][i ] = INT_MAX;
		for(int i=0;i<=H+1;i++)
			h[i][0] = h[i][ W+1 ] = INT_MAX;
		for(int i=1;i<=H;i++)
			for(int j=1;j<=W;j++)
				cin >> h[i][j];
		map[1][1] = 'a';
		basen = 'a';
		for(int i = 1;i<=H;i++)
		{
			for(int j=1;j<=W;j++)
			{
				if( map[i][j] ==0 )
				{
					flow( i,j );
					if( map[i][j]== 0)
						map[i][j] = ++basen;
				}
				color( i,j );
			}
		}
		fout << "Case #" << k+1 << ":" << endl;
		for(int i=1;i<=H;i++)
		{
			fout << map[i][1];
			for(int j=2;j<=W;j++)
				fout << " " << map[i][j];
			fout << endl;
		}
	}
}