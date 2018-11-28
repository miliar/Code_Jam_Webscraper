#include <stdio.h>

int main() {

	int i, t;
	scanf("%d", &t);

	for ( i = 0; i < t; ++i ) {

		int r, c;
		scanf("%d %d", &r, &c);

		char input[r][c];

		for ( int j = 0; j < r; ++j ) {

			getchar();

			for ( int k = 0; k < c; ++k )
				input[j][k] = getchar();

		}

		int print = false;

		while ( 1 ) {

			int bb = true;
			int stop = false;

			for ( int j = 0; j < r; ++j ) {

				for ( int k = 0; k < c; ++k ) {

					if ( input[j][k] == '#' ) {

						if ( k <= c-1 && j <= r-1 ) {

							if ( input[j][k+1] == '#' && input[j+1][k] == '#' && input[j+1][k+1] == '#' ) {

								input[j][k] = '/';
								input[j][k+1] = '\\';
								input[j+1][k] = '\\';
								input[j+1][k+1] = '/';
								bb = false;

							} else {

								printf("Case #%d:\nImpossible\n", i+1);
								print = true;

							}

						} else {

							printf("Case #%d:\nImpossible\n", i+1);
							print = true;

						}

						stop = true;

					}

					if ( stop )
						break;

				}

				if ( stop )
					break;

			}

			if ( bb )
				break;

		}

		if ( ! print ) {

			printf("Case #%d:\n", i+1);

			for ( int j = 0; j < r; ++j ) {

				for ( int k = 0; k < c; ++k )
					putchar(input[j][k]);

				printf("\n");

			}

		}

	}

}
