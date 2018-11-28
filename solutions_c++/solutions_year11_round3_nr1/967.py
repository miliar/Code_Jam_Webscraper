#include<iostream>
#include<string>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;

bool visited[60][60];
string table[60];
int R, C;

bool check(int x, int y)
{
	if(x == R-1 || y == C-1)
		return false;

	if(table[x][y] == '#' && table[x+1][y] == '#' && table[x][y+1] == '#' && table[x+1][y+1] == '#')
		return true;
	else
		return false;
}

void go(int x, int y)
{
	table[x][y] = '/';
	table[x+1][y+1] = '/';
	table[x][y+1] = '\\';
	table[x+1][y] = '\\';
	visited[x][y] = visited[x][y+1] = visited[x+1][y] = visited[x+1][y+1] = true;
	return;
}

int main()
{

	freopen ("A-large.in", "r", stdin);
	freopen ("A-large.out", "w", stdout);

	int tc;
	cin >> tc;
	for(int TC=1; TC<=tc; TC++)
	{
		memset( table, 0, sizeof table);
		memset( visited, 0, sizeof visited);
		
		cin >> R >> C;
		for(int i=0; i<R; i++)
		{
			cin >> table[i];
		}

		for(int i=0; i<R-1; i++)
		{
			for(int j=0; j<C-1; j++)
			{
				if(table[i][j] == '#')
				{
					if( !visited[i][j] && check(i,j) )
					{
						go(i,j);
					}
				}
			}
		}
		bool flag = true;
		for(int i=0; i<R; i++)
			for(int j=0; j<C; j++)
				if( !visited[i][j] && table[i][j] == '#')
					flag = false;

		cout << "Case #" << TC << ":" << endl;
		if(!flag)
			cout << "Impossible" << endl;
		else
		{
			for(int i=0; i<R; i++)
			{
				cout << table[i] << endl;
			}
		}
	}
	return 0;
}