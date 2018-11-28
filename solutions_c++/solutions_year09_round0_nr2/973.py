#include<iostream>
#include<string>
#include<fstream>
using namespace std;

const int MAXN = 100 + 1;

char flag[MAXN][MAXN];
int imap[MAXN][MAXN];
int dir[4][2] = { {0,1},{1,0},{-1,0},{0,-1} };
int h,w;
char basin;

bool isvalid(int x,int y)
{
	if( x >= 0  && x < w && y >= 0 && y < h )
		return true;
	return false;
}

void dfs( int y, int x )
{
	int i,j;
	int nx,ny;
	int resx,resy;
	resx = 200,resy = 200;
	int min = 1000000;
	for( i = 0 ; i < 4 ; i++ )	
	{
		int nx = x+dir[i][0];
		int ny = y+dir[i][1];
		if( isvalid( nx, ny) && imap[y][x] > imap[ny][nx])
		{
			if( imap[ny][nx] <= min )
			{
				min = imap[ny][nx];
				resy = ny;
				resx = nx;
			}
			/*else if( resy == ny )
			{
				if( resx > nx )
				{
					resy = ny;
					resx = nx;
				}
			}*/
		}
	}
	if( resx != 200 )
	{
		if( flag[resy][resx] != -1 )
		{
			flag[y][x] = flag[resy][resx];
			return;
		} 
		else
		{
			dfs( resy,resx );
			flag[y][x] = flag[resy][resx];
			return;
		}
	}
	else
	{		
		flag[y][x] = basin;
		basin++;
		return;
	}
}

int main()
{
	ifstream fin("input");
	ofstream fout("output");
	int ncase;
	fin >> ncase;
	for( int i = 0 ; i < ncase ; i++ )
	{
		basin = 'a';
		fin >> h >> w;
		for( int j = 0 ; j < h ; j++ )
		{
			for( int k = 0 ; k <  w ; k++)
				fin >> imap[j][k];
		}
		memset(flag,-1,sizeof(flag));
		for( int j = 0 ; j < h ; j++ )
		{
			for( int k = 0 ; k < w ; k++ )
			{
				if( flag[j][k] == -1)
					dfs(j,k);
			}
		} 
		fout << "Case #"<< i+1<< ":"<<endl;
		for( int j = 0 ; j < h ; j++ )
		{
			for( int k = 0 ; k < w ; k++ )
				fout << flag[j][k] << " ";
			fout << endl;
		}

	}

	return 0;
}