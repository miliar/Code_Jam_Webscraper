#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>

using namespace std;

const int M = 11814486;

int happy[15][M];
int together[M];
int lookup[1<<11];

char input[1024];

int ishappy( int number, int base ) {

	int s;
	int b;
	int o;

	o = number;

	if ( happy[base][number] ) return happy[base][number];

	// visited
	happy[base][number] = 1;

	s = 0;
	b = 1;
	while ( number ) {
		s += (number % base) * ( number % base );
		number /= base;
	}

	if ( s == 1 ) {
		s = 3;
	} else {
		s = ishappy( s, base );
	}

	if ( s == 3 ) {
		together[o] |= (1<<base);
	}
	return happy[base][o] = s;
}

int main ( int argc, char ** argv ) {
	int x,y;
	int t, tn;
	char *c;

	for (y=2; y<=10; y++) {
		for (x=2; x<M; x++) {
			ishappy(x, y);
		}
	}
	for (x=2; x<M; x++) {
		if ( together[x] == 0 ) continue;
		if ( lookup[ together[x] ] ) continue;
		for ( y=2; y<(1<<11)-1; y++) {
			if ( ( y & together[x] ) == y ) {
				if ( lookup[y] == 0 ) {
					lookup[y] = x;
				}
			}
		}
	}

	scanf("%d", &t);
	fgets( input, 1024, stdin );
	for (tn = 0; tn<t; tn++) {
		fgets( input, 1024, stdin );
		y = 0;
		c = strtok( input, " \n");
		while ( c ) {
			y |= 1<<(atoi(c));
			c = strtok( NULL, " \n");
		}
		printf("Case #%d: %d\n", tn+1, lookup[y]);
	}

	return 0;
}
