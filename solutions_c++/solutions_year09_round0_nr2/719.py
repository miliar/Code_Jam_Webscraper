#include<cstdio>
#include<algorithm>
#include<map>
using namespace std;

#define H 100
#define W 100

int h, w;
int Alt[ H][ W];
int P[ H * W], C[ H * W];
int Dx[ 4] = { 0, -1, 1, 0}, Dy[ 4] = { -1, 0, 0, 1};
int Basin[ 30];
char Out[ H][ W];

FILE *fin, *fout;

void prs( int testnum) {
	
	fscanf( fin, "%d %d", &h, &w);
	for ( int i = 0; i < h; i++)
		for ( int j = 0; j < w; j++)
			fscanf( fin, "%d", &Alt[ i][ j]);
	
	int n = h * w;
	for ( int i = 0; i < n; i++)
		P[ i] = i, C[ i] = 1;

	for ( int i = 0; i < h; i++) {
		for ( int j = 0; j < w; j++) {
			int min_direction = -1, min_value = Alt[ i][ j];
			for ( int k = 0; k < 4; k++) {
				int wy = i + Dy[ k], wx = j + Dx[ k];
				if ( 0 <= wy && wy < h && 0 <= wx && wx < w && min_value > Alt[ wy][ wx])
					min_value = Alt[ wy][ wx], min_direction = k;
			}
			if ( min_direction != -1) {
				// Merge (i,j) & (wy, wx);
				int a = i * w + j, b = (i + Dy[ min_direction]) * w + (j + Dx[ min_direction]), fa, fb, ga;
				for ( fa = a; fa != P[ fa]; fa = P[ fa]);
				for ( fb = b; fb != P[ fb]; fb = P[ fb]);
				if ( fa == fb) 
					continue;

				if ( C[ fa] < C[ fb]) 
					C[ fb] += C[ fa], ga = fb;
				else
					C[ fa] += C[ fb], ga = fa;

				P[ fa] = P[ fb] = ga;
				for ( fa = a; fa != P[ fa];) {
					fb = P[ fa];
					P[ fa] = ga;
					fa = fb;
				}
				for ( fa = b; fa != P[ fa];) {
					fb = P[ fa];
					P[ fa] = ga;
					fa = fb;
				}
			}
		}
	}

	for ( int i = 0; i < n; i++) {
		int fa;
		for ( fa = i; fa != P[ fa]; fa = P[ fa]);
		P[ i] = fa;
	}

	int cnt = 0;

	for ( int i = 0; i < h; i++) {
		for ( int j = 0; j < w; j++) {
			int a = P[ i * w + j];
			bool is_ok = 0;
			for ( int k = 0; k < cnt; k++) {
				if ( Basin[ k] == a) {
					is_ok = 1;
					Out[ i][ j] = k + 'a';
					break;
				}
			}
			if ( !is_ok) {
				Out[ i][ j] = 'a' + cnt;
				Basin[ cnt++] = a;
			}
		}
	}	
	fprintf( fout, "Case #%d:\n", testnum);
	for ( int i = 0; i < h; i++) {
		for ( int j = 0; j < w; j++) {
			fprintf( fout, "%c ", Out[ i][ j]);
		}
		fprintf( fout, "\n");
	}
}

int main( void) {

	int testcase;

	fin = fopen ( "input.txt", "rt");
	fout = fopen( "output.txt", "wt");
	fscanf( fin, "%d", &testcase);
	for ( int i = 0; i < testcase; i++) {
		prs( i + 1);
	}
	fclose( fin);
	fclose( fout);
}

