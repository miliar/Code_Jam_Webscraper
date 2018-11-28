#include<stdio.h>

#define MAX 10007

FILE *fin, *fout;
int r, w, h;
int Dynamic[ 101][ 101];

void inp( void) {


	fscanf( fin, "%d %d %d", &h, &w, &r);

	for ( int i = 1; i <= h; i++) {
		for ( int j = 1; j <= w; j++) {
			Dynamic[ i][ j] = 0;
		}
	}
	
	for ( int i = 0; i < r; i++) {
		int a, b;
		fscanf( fin, "%d %d", &a, &b);
		Dynamic[ a][ b] = -1;
	}
}

void prs( void) {

	Dynamic[ 1][ 1] = 1;

	for ( int i = 1; i <= h; i++) {
		for ( int j = 1; j <= w; j++) {
			if ( Dynamic[ i][ j] <= 0) continue;
			if ( i + 1 <= h && j + 2 <= w && Dynamic[ i + 1][ j + 2] != -1) {
				Dynamic[ i + 1][ j + 2] += Dynamic[ i][ j];
				Dynamic[ i + 1][ j + 2] %= MAX;
			}
			if ( i + 2 <= h && j + 1 <= w && Dynamic[ i + 2][ j + 1] != -1) {
				Dynamic[ i + 2][ j + 1] += Dynamic[ i][ j];
				Dynamic[ i + 2][ j + 1] %= MAX;
			}
		}
	}
}

void outp( void) {

	if ( Dynamic[ h][ w] <= 0) fprintf( fout, "%d\n", 0);
	else fprintf( fout, "%d\n", Dynamic[ h][ w]);
}

int main( void) {

	fin = fopen ( "input.txt", "rt");
	fout = fopen ( "output.txt", "wt");

	int tmp;

	fscanf( fin, "%d", &tmp);

	for ( int i = 0; i < tmp; i++) {
		inp();	
		prs();
		fprintf( fout, "Case #%d: ", i + 1);
		outp();
	}

	fclose(fin);
	fclose(fout);

	return 0;

}


