#include <cstdlib>
#include <string>
#include <cstdio>
#include <iostream>

using namespace std;


#define forl(x,a,b) for(int x = a; x < b; ++x)

char tile[50][50];
int r,c;
int numBlue;


char getTile(int x, int y)
{
	if (x < 0 || x >= c) return '\0';
	if (y < 0 || y >= r) return '\0';
	return tile[y][x];
}

bool posOk(int x, int y)
{
	if (getTile(x,y) != '#') return false;
	if (getTile(x+1,y) != '#') return false;
	if (getTile(x, y+1) != '#') return false;
	if (getTile(x+1, y+1) != '#') return false;
	return true;
}

void putTile(int x, int y)
{
	//cerr << "putTile: " << x << ", " << y << endl;
	tile[y][x] = '/';
	tile[y][x+1] = '\\';
	tile[y+1][x] = '\\';
	tile[y+1][x+1] = '/';
	numBlue -= 4;
}

void solveTile(int x, int y)
{
	if (posOk(x-1,y-1)) putTile(x-1,y-1);
	else if (posOk(x,y-1)) putTile(x,y-1);
	else if (posOk(x-1,y)) putTile(x-1,y);
	else if (posOk(x,y)) putTile(x,y);
}

void solve()
{
	forl(j,0,r) forl (i,0,c) solveTile(i,j);
}

void draw()
{
	forl(i,0,r) 
	{
		forl(j,0,c)
		{
			if (getTile(j,i) != '\0')
				cout << getTile(j,i);
		}
		cout << endl;
	}
}

main()
{
	int t;
	cout.precision(12);
	cin >> t;
	forl(i,0,t)
	{
		numBlue = 0;
		
		cin >> r >> c;
		forl(row,0,r)
		{
			string srow;
			cin >> srow;
			forl(column,0,c)
			{
				char ch = srow[column];
				if (ch == '#') numBlue++;
				tile[row][column] = ch;
			}
		}
		solve();
		cout << "Case #" << i + 1 << ":" << endl;
		if (numBlue)
		{
			cout << "Impossible" << endl;
		}
		else
		{
			draw();
		}
	}
}
