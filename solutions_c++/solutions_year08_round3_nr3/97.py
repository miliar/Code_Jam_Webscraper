#include<stdio.h>
#define MAX 1000000007
#define N 1000
#define M 100

int n, m, x, y, z, ans;
int Speed[ N + 1], A[ M + 1];
int D[ N + 1];

void prs( void) {

	int i, j;

	long long tmp;
	
	for ( i = 0, j = 0; i < n; i++) {

		Speed[ i] = A[ j];

		tmp = (long long)x * A[ j] + (long long)y * ( i + 1);

		A[ j] = (int)( tmp % z);

		if ( j == m - 1) j = 0; else j++;

	}

	for ( i = 0; i < n; i++) D[ i] = 1;

	ans = 0;

	for ( i = 0; i < n; i++) {

		for ( j = 0; j < i; j++) {

			if ( Speed[ i] > Speed[ j]) {

				tmp = (long long)D[ i] + D[ j];

				D[ i] = (int)( tmp % MAX);

			}

		}

		tmp = (long long)ans + D[ i];
		ans = (int)( tmp % MAX);

	}

}

int main( void) {

	FILE *fin = fopen ( "input.txt", "rt");

	FILE *fout = fopen ( "output.txt", "wt");

	int Testn, i, j;

	fscanf( fin, "%d", &Testn);

	for ( i = 1; i <= Testn; i++) {

		// Input

		fscanf( fin, "%d %d %d %d %d", &n, &m, &x, &y, &z);

		for ( j = 0; j < m; j++) {
			fscanf( fin, "%d", &A[ j]);
		}

		prs();

		fprintf(fout, "Case #%d: %d\n", i, ans);

	}

	fclose(fin);
	fclose(fout);

	return 0;

}
