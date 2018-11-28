#include <cstdio>

#define FOR(a,b,c) for(a=b;a<c;a++)
#define LIM 4

using namespace std;

char mat [LIM][LIM];

int main () {
	int a,b,cc,TC;
	int p1, p2;
	int won;
	char inp;
	
	
	scanf("%d", &TC);
	for ( cc = 0; cc < TC; ++cc) {
	
		won = 3; //0->unfinished, 1->X, 2->O, 3->draw
		
		//printf("LABEL A");
		// get input
		FOR (a,0,LIM) {
			FOR (b,0,LIM) {
				scanf("%c",&inp);
				if ( inp != '\n' ) {
					mat[a][b] = inp;
				}
				else {
					b--;
					continue;
				}
		}	}
		scanf("%*c");
		//printf("LABEL B");
		
		/*
		printf("Good input ===\n");
		FOR (a,0,LIM) {
			FOR (b,0,LIM) {
				printf("%c", mat[a][b]);
			}	
			printf("\n");
		}
		printf(" ===\n");
		*/
		
		// check horizontal lines
		for ( a = 0; a < LIM; ++a ) {
			p1 = p2 = 0;
			for ( b = 0; b < LIM; ++b ) {
				switch (mat[a][b]) {
					case 'X' : p1++; break;
					case 'O' : p2++; break;
					case 'T' : p1++; p2++; break;
					case '.' : won = 0; break;
				}
			}
			if ( p1 == LIM ) {
				won = 1;
				break;
			}
			if ( p2 == LIM ) {
				won = 2;
				break;
			}
			if (won != 0 && won != 3) {
				break;
			}
		}
		//printf("LABEL C");
		
		// check vertical lines 
		if ( won != 1 && won != 2 ) {
			for ( a = 0; a < LIM; ++a ) {
				p1 = p2 = 0;
				for ( b = 0; b < LIM; ++b ) {
					switch (mat[b][a]) {
						case 'X' : p1++; break;
						case 'O' : p2++; break;
						case 'T' : p1++; p2++; break;
					}
				}
				if ( p1 == LIM ) {
					won = 1;
					break;
				}
				if ( p2 == LIM ) {
					won = 2;
					break;
				}
				if (won != 0 && won != 3) {
					break;
				}
			}
		}
		//printf("LABEL D");
		
		// check diagonals
		if ( won != 1 && won != 2 ) {
			p1 = p2 = 0;
			for ( b = 0; b < LIM; ++b ) {
				switch (mat[b][b]) {
					case 'X' : p1++; break;
					case 'O' : p2++; break;
					case 'T' : p1++; p2++; break;
				}
			}
			if ( p1 == LIM ) {
				won = 1;
			}
			if ( p2 == LIM ) {
				won = 2;
			}
		}
			
		if ( won != 1 && won != 2 ) {
			p1 = p2 = 0;
			FOR (b,0,LIM) {
				switch (mat[b][3-b]) {
					case 'X' : p1++; break;
					case 'O' : p2++; break;
					case 'T' : p1++; p2++; break;
				}
			}
			if ( p1 == LIM ) {
				won = 1;
			}
			if ( p2 == LIM ) {
				won = 2;
			}
		}
		//printf("LABEL E");
		
		// output
		printf("Case #%d: ", cc+1);
		switch ( won ) {
			case 0 : printf("Game has not completed\n"); break;
			case 1 : printf("X won\n"); break;
			case 2 : printf("O won\n"); break;
			case 3 : printf("Draw\n"); break;
		}
			
		//printf("LABEL F");
		
	}
	
	return 0;
}
