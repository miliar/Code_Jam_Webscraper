#include<stdio.h>
#include<string.h>
#define N 100
#define M 1000
#define LENGTH 111

FILE *fin, *fout;

int ans, n, m;
char Name[ N][ LENGTH], Temp[ LENGTH];
int Query[ M], Check[ N];

void inp() {

	fscanf ( fin, "%d\n", &n);

	int i, j;

	for ( i = 0; i < n; i++) {

		fgets ( Name[ i], LENGTH, fin);

		for ( j = strlen( Name[ i]) - 1; j >= 0; j--) {

			if ( Name[ i][ j] == ' ' || Name[ i][ j] == '\n') Name[ i][ j] = 0;

			else break;

		}

	}

	fscanf( fin, "%d\n", &m);

	for ( i = 0; i < m; i++) {

		fgets ( Temp, LENGTH, fin);

		for ( j = strlen( Temp) - 1; j >= 0; j--) {

			if ( Temp[ j] == ' ' || Temp[ j] == '\n') Temp[ j] = 0;

			else break;

		}

		for ( j = 0; j < n; j++) {

			if ( !strcmp( Temp, Name[ j])) {

				Query[ i] = j; break;

			}

		}

	}

}

void prs( void) {

	ans = 0;

	int i, j, sum;

	sum = 0;

	for ( i = 0; i < n; i++) Check[ i] = 0;

	for ( i = 0; i < m; i++) {

		j = Query[ i];

		if ( !Check[ j]) {

			sum++;

		}

		Check[ j]++;

		if ( sum == n) {

			sum = 1; ans++;

			for ( j = 0; j < n; j++) Check[ j] = 0;

			Check[ Query[ i]] = 1;

		}
		
	}

}

void outp( void) {

	fprintf( fout, "%d\n", ans);

}

int main( void) {

	int testn;

	fin = fopen ( "input.txt", "rt");
	fout = fopen ( "output.txt", "wt");

	fscanf( fin, "%d", &testn);

	for ( int i = 1; i <= testn; i++) {

		inp();
		prs();

		fprintf( fout, "Case #%d: ", i);
		outp();

	}

	return 0;

}