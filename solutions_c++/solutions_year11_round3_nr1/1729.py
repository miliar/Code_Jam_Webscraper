#include <iostream>
#define BLUE '#'
#define WHITE '.'

using namespace std;

int main()
{
	int ncases, ccase = 0;
	cin >> ncases;
	while (ccase++ < ncases)
	{
		int r, c;
		cin >> r >> c;
		char tiles[r][c];
		int blueCount = 0;
		
		for (int i=0; i<r; i++)
			for (int j=0; j<c; j++)
			{
				char tile; cin >> tile;
				tiles[i][j] = tile;
				if (tile == BLUE)
					blueCount++;
			}
		
		bool possible = !(blueCount % 4);
		if (possible && blueCount)
		{
			for (int i=0; i<r-1; i++)
				for (int j=0; j<c-1; j++)
				{
					if (tiles[i][j] == BLUE && tiles[i][j+1] == BLUE && tiles[i+1][j] == BLUE && tiles[i+1][j+1] == BLUE)
					{
						tiles[i][j] = tiles[i+1][j+1] = '/';
						tiles[i+1][j] = tiles[i][j+1] = '\\';
						blueCount -= 4;
					}
				}
			possible = !blueCount;
		}
		
		cout << "Case #" << ccase << ":" << endl;
		if (possible)
		{
			for (int i=0; i<r; i++)
			{
				for (int j=0; j<c; j++)
					cout << tiles[i][j];
				cout << endl;
			}
		}
		else
		{
			cout << "Impossible" << endl;
		}
	}
	return 0;
}
