// Google CodeJAM 2011
// Author: Syed Ghulam Akbar

#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <iostream>

using namespace std;
char Tile[60][60];

int main() {
	FILE *in = freopen( "Debug\\input.txt", "r", stdin );
	FILE *out = freopen( "Debug\\output.txt", "w", stdout );

	int C;
	scanf("%d",&C);

	for (int test=1;test<=C;test++) {
		
		long row=0, col=0;
		cin >> row >> col;

		for (int i=0; i<row; i++)
			for (int j=0; j<col; j++)
				cin >> Tile[i][j];

		int possible = true;

		// Now check and process the titles
		for (int i=0; i<row; i++)
			for (int j=0; j<col; j++)
			{
				// Blue color
				if (Tile[i][j] == '#')
				{
					if (i+1 < row && j + 1 < col)
					{
						if (Tile[i][j+1] == '#' && Tile[i+1][j] == '#' && Tile[i+1][j+1] == '#')
						{
							Tile[i][j] = '/';
							Tile[i][j+1] = '\\';
							Tile[i+1][j] = '\\';
							Tile[i+1][j+1] = '/';
						}
						else
							possible = false;
					}
					else
						possible = false;
				}
			}

		printf("Case #%d: \n", test);

		if (possible==false)
			printf("Impossible\n");
		else
			for (int i=0; i<row; i++)
			{
				for (int j=0; j<col; j++)
					printf("%c", Tile[i][j]);
				printf("\n");
			}

	}
}