#include<stdio.h>
#include<string.h>
#define L 15

int l, ans;
char Input[ L + 1];
long long Pow[ L];
long long n;

void Back( int x, long long sum) {

	long long tmp = n % Pow[ l - x];

	if ( x == l) {

		if ( sum == 0 || (sum % 2) == 0 || (sum % 3) == 0 || (sum % 5) == 0 || (sum % 7) == 0) {

			ans++;

		}

	} else {

		int i;

		for ( i = x + 1; i <= l; i++) {
			Back( i, sum + tmp / Pow[ l - i]);
			Back( i, sum - tmp / Pow[ l - i]);
		}

	}

}

void prs( void) {

	int i;
	long long tmp;

	l = strlen( Input);

	ans = 0;
	
	Pow[ 0] = 1;

	for ( i = 1; i < 15; i++) Pow[ i] = Pow[ i - 1] * (long long)10;

	n = 0;

	for ( i = 0; i < l; i++) n += (long long)( Input[ i] - '0') * Pow[ l - i - 1];

	for ( i = 1; i <= l; i++) {
		Back( i, n / Pow[ l - i]);
	}
}

int main( void) {

	FILE *fin = fopen ( "input.txt", "rt");

	FILE *fout = fopen ( "output.txt", "wt");

	int Testn, i;

	fscanf( fin, "%d", &Testn);

	for ( i = 1; i <= Testn; i++) {

		// Input
		

		fscanf (fin, "%s", &Input);

		prs();

		fprintf(fout, "Case #%d: %d\n", i, ans);

	}

	fclose(fin);
	fclose(fout);

	return 0;

}
