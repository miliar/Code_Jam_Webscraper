#include<cstdio>
#include<algorithm>
#include<cstring>
#include<string>
using namespace std;

FILE *fin, *fout;

int n, l;
char inp[ 30];

int main( void) {
	fin = fopen ( "input.txt", "rt");
	fout = fopen ( "output.txt", "wt");

	int testnum;
	fscanf( fin, "%d", &testnum);

	for ( int i = 1; i <= testnum; i++) {

		fscanf ( fin, "%s", inp);
		fprintf( fout, "Case #%d: ", i);
		l = strlen( inp);
		if ( next_permutation( inp, inp + l)) {
			fprintf( fout, "%s\n", inp);
		} else {
			sort( inp, inp + l);
			if ( inp[ 0] == '0') {
				for ( int j = 1; j < l; j++) {
					if ( inp[ j] != '0') {
						swap( inp[ 0], inp[ j]);
						break;
					}
				}
			}

			fprintf ( fout, "%c0", inp[ 0]);
			for ( int j = 1; j < l; j++)
				fprintf( fout, "%c", inp[ j]);		
			fprintf( fout, "\n");
		}

	}
	
	return 0;
}


	