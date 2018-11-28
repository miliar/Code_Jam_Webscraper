#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

FILE *fin, *fout;

int l = 19;
char Pattern[ 20] = "welcome to code jam";
char Data[ 600];

int nCnt[ 20], Cnt[ 20];

void prs( int testnum) {
	fgets( Data, 600, fin);
	int n = strlen( Data);

	for ( int i = 0; i < l; i++) {
		nCnt[ i] = Cnt[ i] = 0;
	}

	for ( int i = 0; i < n; i++) {
		for ( int j = 0; j < l; j++) {
			if ( Pattern[ j] == Data[ i]) {
				if ( j == 0) nCnt[ 0] += 1;
				else nCnt[ j] += Cnt[ j - 1];				
			}
		}

		for ( int j = 0; j < l; j++)
			Cnt[ j] = ( Cnt[ j] + nCnt[ j]) % 10000, nCnt[ j] = 0;
	}

	fprintf( fout, "Case #%d: %04d\n", testnum, Cnt[ l - 1]);
}

int main( void) {
	fin = fopen( "input.txt", "rt");
	fout = fopen( "output.txt", "wt");
	
	int testcase;
	fscanf( fin, "%d", &testcase);
	fgets( Data, 600, fin);

	for ( int i = 1; i <= testcase; i++)
		prs( i);

	fclose( fin);
	fclose( fout);

	return 0;
}