#include <stdio.h>
#include <vector>
#include <stdlib.h>


using namespace std;


int main()
{

	int T, i, n;
	
	char tablero[4][4];
	
	scanf("%d\n", &n);

	for ( i=0 ; i<n ; ++i ) {
	
		scanf("%c %c %c %c\n%c %c %c %c\n%c %c %c %c\n%c %c %c %c\n", &tablero[0][0], &tablero[0][1], &tablero[0][2], &tablero[0][3], &tablero[1][0], &tablero[1][1], &tablero[1][2], &tablero[1][3], &tablero[2][0], &tablero[2][1], &tablero[2][2], &tablero[2][3], &tablero[3][0], &tablero[3][1], &tablero[3][2], &tablero[3][3]);

		int f, c;

		bool end = false;

		char jugador;

		int cont;

		bool hubopunto = false;

		for ( f=0 ; f<4 ; ++f ) {

			jugador = tablero[f][0];

			if ( jugador == '.' ) {
				hubopunto = true;
				continue;
			}

			cont = 0;

			for ( c=0 ; c<4 ; ++c ) {
				if ( tablero[f][c] == jugador || tablero[f][c] == 'T' ) {
					cont++;
				} else if ( tablero[f][c] == '.' ) {
					hubopunto = true;
				}
			}
			
			if ( cont == 4 ) {
				end = true;
				printf( "Case #%d: %c won\n", i+1, jugador );		
				break;
			}
		}
		
		if ( end ) continue;

		for ( c=0 ; c<4 ; ++c ) {

			jugador = tablero[0][c];

			if ( jugador == '.' ) {
				hubopunto = true;
				continue;
			}

			cont = 0;

			for ( f=0 ; f<4 ; ++f ) {
				if ( tablero[f][c] == jugador || tablero[f][c] == 'T' ) {
					cont++;
				} else if ( tablero[f][c] == '.' ) {
					hubopunto = true;
				}
			}
			
			if ( cont == 4 ) {
				end = true;
				printf( "Case #%d: %c won\n", i+1, jugador );		
				break;
			}
		}
					
		if ( end ) continue;

		jugador = tablero[0][0];

		if ( jugador != '.' ) {

			cont = 0;
			for ( f=0 ; f<4 ; ++f ) {


				if ( tablero[f][f] == jugador || tablero[f][f] == 'T' ) {
					cont++;
				} else if ( tablero[f][f] == '.' ) {
					hubopunto = true;
				}
			}
			
			if ( cont == 4 ) {
				end = true;
				printf( "Case #%d: %c won\n", i+1, jugador );		
				continue;
			}

		} else {
			hubopunto = true;
		}

		if ( end ) continue;

		jugador = tablero[0][3];

		if ( jugador != '.' ) {

			cont = 0;
			for ( f=0 ; f<4 ; ++f ) {


				if ( tablero[f][3-f] == jugador || tablero[f][3-f] == 'T' ) {
					cont++;
				} else if ( tablero[f][3-f] == '.' ) {
					hubopunto = true;
				}
			}
				
			if ( cont == 4 ) {
				end = true;
				printf( "Case #%d: %c won\n", i+1, jugador );		
				continue;
			}
		} else {
			hubopunto = true;
		}

		if ( hubopunto ) {
			printf("Case #%d: Game has not completed\n", i+1);
		} else {
			printf("Case #%d: Draw\n", i+1);
		}
	}

	return 0;
}
