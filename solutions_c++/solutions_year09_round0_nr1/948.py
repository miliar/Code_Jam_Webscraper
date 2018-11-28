#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

int words[5005][20];
int L,D,N;
char input[1024];
int pattern[20];

void trim(char *what) {
	if ( what[ strlen(what) -1 ] == '\n' ) {
		what[ strlen(what) -1 ] = '\0';
	}
}

int main ( int argc, char ** argv ) {
	
	int x,y,z;
	int cnt;
	int stop;
       	int pos;

	scanf("%d %d %d", &L, &D, &N);
	fgets( input, 1024, stdin );
	for (y=0; y<D; y++) {
		fgets( input, 1024, stdin );
		trim( input );
		for (x=0; x<strlen(input); x++) {
			words[y][x] = 1<<(input[x]-'a');
		}
	}
	for (y=0; y<N; y++) {
		fgets( input, 1024, stdin );
		trim( input );
		
		memset( pattern, 0, sizeof(int)*20 );
		pos = 0;
		stop = 0;
		
		for (x=0; x<strlen(input); x++) {
			if ( input[x] == '(' ) {
				stop = 1;
				continue;
			}
			if ( input[x] == ')' ) {
				stop = 0;
				pos++;
				continue;
			}
			pattern[pos] |= 1<<(input[x]-'a');
			if ( !stop ) pos++;
		}

		assert ( pos==L );

		cnt = 0;
		for (x=0; x<D; x++) {
			for (z=0; z<L; z++) {
				if ( ( pattern[z] & words[x][z] ) == 0 ) break;
			}
			if ( z == L ) cnt++;
		}

		printf("Case #%d: %d\n", y+1, cnt);
	}
	return 0;
}
