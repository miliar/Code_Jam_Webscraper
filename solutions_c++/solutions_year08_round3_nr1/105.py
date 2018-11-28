#include<stdio.h>
#include<stdlib.h>
#define L 1000
#define K 1000
#define P 1000

int l, k, p;
long long ans;

int Push[ L + 1];

int sortf( const void *a, const void *b) {

	return *( int *)b - *( int *)a;

}

void prs( void) {

	qsort( Push, l, sizeof(int), sortf);

	int i, j, t;

	for ( i = 1, j = 0; i <= p && j < l; i++) {

		for ( t = 0; t < k && j < l; j++, t++) {
		
			ans += Push[ j] * i;

		}

	}

}

int main( void) {

	FILE *fin = fopen ( "input.txt", "rt");

	FILE *fout = fopen ( "output.txt", "wt");

	int Testn, i, j;

	fscanf( fin, "%d", &Testn);

	for ( i = 1; i <= Testn; i++) {

		// Input

		ans = 0;
		fscanf( fin, "%d %d %d", &p, &k, &l);

		for ( j = 0; j < l; j++) {
			fscanf( fin, "%d", &Push[ j]);
		}
		prs();

		fprintf(fout, "Case #%d: %I64d\n", i, ans);

	}

	fclose(fin);
	fclose(fout);

	return 0;

}
