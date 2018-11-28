#include<stdio.h>
#include<stdlib.h>

#define N 801

int n;
long long ans;
int X[ N];
int Y[ N];

int sortf( const void *a, const void *b) {
	return *( int *)a - *( int *)b;
}

void prs( void) {

	int i;

	qsort( X, n, sizeof( X[0]), sortf);
	qsort( Y, n, sizeof( Y[0]), sortf);

	ans = 0;

	for ( i = 0; i < n; i++) {

		ans += (long long) X[ i] * Y[ n - i - 1];

	}	

}

int main( void) {

	FILE *fin = fopen ( "input.txt", "rt");
	FILE *fout = fopen ( "output.txt", "wt");

	int i, test, j;

	fscanf( fin, "%d", &test);

	for ( i = 0; i < test; i++) {

		fscanf ( fin, "%d", &n);

		for ( j = 0; j < n; j++) fscanf( fin, "%d", &X[ j]);
		for ( j = 0; j < n; j++) fscanf( fin, "%d", &Y[ j]);

		prs();

		fprintf(fout, "Case #%d: %I64d\n", i + 1, ans);

	}

	return 0;

}
