#include <iostream>
using namespace std;

char tiles[60][60];
int T, R, C;

bool replace(void)
{
	for(int i = 0; i < R; i++)
	{
		for(int j = 0; j < C; j++)
		{	
			if(tiles[i][j] == '#')
			{
				if(tiles[i][j + 1] == '#' && tiles[i + 1][j] == '#' && tiles[i + 1][j + 1] == '#')
				{
					tiles[i][j] = '/';
					tiles[i][j + 1] = '\\';
					tiles[i + 1][j] = '\\';
					tiles[i + 1][j + 1] = '/';
				}
				else return false;
			}
		}
	}
	
	return true;
}

int main(void)
{
	cin >> T;
	for(int numCase = 1; numCase <= T; numCase++)
	{
		cin >> R >> C;
		for(int i = 0; i < R; i++) for(int j = 0; j < C; j++) cin >> tiles[i][j];
		
		cout << "Case #" << numCase << ":" << endl;
		if(replace())
		{
			for(int i = 0; i < R; i++)
			{
				for(int j = 0; j < C; j++) cout << tiles[i][j];
				cout << endl;
			}
		}
		else cout << "Impossible" << endl;
	}
}
