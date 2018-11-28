#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char input[10000];

int occ[10000][32];

const char *aim = "welcome to code jam";
const int L = 19;
int N;

void trim( char *what ) {
	if ( what[strlen(what)-1] == '\n' ) {
		what[strlen(what)-1] = '\0';
	}
}

int main ( int argc, char ** argv ) {
	int casenr;
	int a,b,x,y;
	int len;
	int s;

	scanf("%d", &N);
	fgets( input, 10000, stdin );
	for (casenr=0; casenr<N; casenr++) {
		fgets( input, 10000, stdin );
		trim( input );
		len = strlen( input );
		for (y=0; y<len+1; y++) {
			for (x=0; x<L+1; x++) {
				occ[y][x] = 0;
			}
		}
		for (y=0; y<len+1; y++) {
			for (x=L; x>0; x--) {
				if ( input[y] != aim[x] ) continue;
				s = 0;
				for (a=0; a<y; a++) {
					s = ( s + occ[a][x-1] ) % 10000;
				}
				occ[y][x] = s;
			}
			if ( input[y] == aim[0] ) occ[y][0] = 1;
		}
		printf("Case #%d: %04d\n", casenr+1, occ[len][L]);
	}
	return 0;
}

