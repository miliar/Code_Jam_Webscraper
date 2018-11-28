#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	int t;
	int r, c, i, j, k;
	int counth;
	char grid[100][100];

	scanf ("%d", &t);

	for ( k = 1; k <= t; k++ ) {
		scanf ("%d%d", &r, &c);
	
		counth = 1;

		for ( i = 0; i < r; i++ ) {
			scanf ("%s", grid[i]);
		}

		for ( i = 0; i < r; i++ ) {
			for ( j = 0; j < c; j++ ) {
				if ( grid[i][j] == '#' ) {
					counth = 0;
					if ( i + 1 < r && grid[i + 1][j] == '#' ) {
						if ( j + 1 < c && grid[i][j + 1] == '#' ) {
							if ( grid[i + 1][j + 1] == '#' ) {
								grid[i][j] = '/';
								grid[i + 1][j] = '\\';
								grid[i][j + 1] = '\\';
								grid[i + 1][j + 1] = '/';
								counth = 1;
							}
						}
					}
				}
				if ( counth == 0 ) {
					break;
				}
			}
			if ( counth == 0 )
				break;
		}
		
		printf ("Case #%d:\n", k);
		if ( counth == 0 ) {
			printf ("Impossible\n");
		} else {
			for ( i = 0; i < r; i++ ) {
				for ( j = 0; j < c; j++ ) {
					putchar(grid[i][j]);
				}
				putchar(10);
			}
		}
	}

	return 0;
}
