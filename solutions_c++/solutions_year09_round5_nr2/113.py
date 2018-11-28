#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<string>
using namespace std;

FILE *fin, *fout;

int n;
int K;

int Ans[ 11];
int cntLetter[ 100][ 26];
int Fact[ 11];
char P[ 50], Term[ 10][ 10], buf[ 55];
int cntTerm = 0, l = 0;

void backtrack( int d, int c[ 26]) {

	if ( d != -1) {

		int point = 0;
		for ( int j = 0; j < cntTerm; j++) {
			int a = 1;
			for ( int k = 0;;k++) {
				if ( Term[ j][ k] == 0) break;
				a *= c[ (int)( Term[ j][ k] - 'a')];
				a %= 10009;
			}
			point += a;
			point %= 10009;
		}
		if ( d == 0)
			d = d;
		Ans[ d] += point;
		Ans[ d] %= 10009;
	}

	if ( d == K - 1)
		return;

	for ( int i = 0; i < n; i++) {
		for ( int j = 0; j < 26; j++)
			c[ j] += cntLetter[ i][ j];
		backtrack( d + 1, c);
		for ( int j = 0; j < 26; j++)
			c[ j] -= cntLetter[ i][ j];
	}
}

void prs( void) {
	
	fscanf( fin, "%s %d %d", P, &K, &n);

	cntTerm = 0; l = 0;

	for ( int i = 0;; i++) {
		if ( P[ i] == 0) break;
		if ( P[ i] == '+') {
			cntTerm++;
			l = 0;
		} else {
			Term[ cntTerm][ l++] = P[ i];
			Term[ cntTerm][ l] = 0;
		}
	}
	cntTerm++;

	for ( int i = 0; i < n; i++) {
		for ( int j = 0; j < 26; j++)
			cntLetter[ i][ j] = 0;
		fscanf( fin, "%s", buf);
		for ( int k = 0;; k++) {
			if ( buf[ k] == 0) break;
			int index = (int)( buf[ k] - 'a'); 
			cntLetter[ i][ index]++;
		}
	}

	for ( int i = 0; i < K; i++)
		Ans[ i] = 0;

	int tc[ 26];
	for ( int i = 0; i < 26; i++)
		tc[ i] = 0;

	backtrack( -1, tc);

	for ( int i = 0; i < K; i++) {
		fprintf( fout, "%d ", Ans[ i]);
	}
	fprintf( fout, "\n");
}

int main( void) {
	fin = fopen( "input.txt", "rt");
	fout = fopen( "output.txt", "wt");
	
	int testcase;
	fscanf( fin, "%d", &testcase);

	/* input */

	Fact[ 0] = 1;
	for ( int i = 1; i <= 10; i++) {
		Fact[ i] = Fact[ i - 1] * i;
		Fact[ i] %= 10009;
	}

	/* process */
	for ( int i = 1; i <= testcase; i++) {
		fprintf( fout, "Case #%d: ", i);
		prs();
	}


	fclose( fin);
	fclose( fout);

	return 0;
}