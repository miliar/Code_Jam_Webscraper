#include<cstdio>
#include<vector>
#include<cstdlib>
#include<cmath>
#include<string>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;

#define N 10
#define gmax( a, b) (( a) > ( b) ? ( a) : ( b))

FILE *fin, *fout;
char String[ 11][ 11];
int ans, m, n;
int Dynamic[ N][ 1100];
int Pow[ 12];

void inp( void) {

	fscanf( fin, "%d %d", &m, &n);
	ans = 0;

	for ( int i = 0; i < m; i++) {
		fscanf( fin, "%s", String[ i]);
	}
	Pow[ 0] = 1;
	for ( int i = 1; i <= n; i++)
		Pow[ i] = Pow[ i - 1] * 2;
}

void prs( void) {
	for ( int i = 0; i < m; i++) {
		for ( int j = 0; j < Pow[ n]; j++) {
			Dynamic[ i][ j] = 0;
		}
	}

	for ( int i = 0; i < Pow[ n]; i++) {
		int tmp = i, ch = 0, cnt = 0;
		for ( int j = 0; j < n; j++) {
			if ( ( tmp >> j) % 2 && ( tmp >> (j - 1)) % 2) ch = 1;
			if ( ( tmp >> j) % 2 && ( tmp >> (j + 1)) % 2) ch = 1;
			if ( ( tmp >> j) % 2 && String[ 0][ j] == 'x') ch = 1;
			if ( ( tmp >> j) % 2) cnt++;
		}		
		if ( ch == 0) Dynamic[ 0][ i] = cnt;
		ans = gmax( ans, Dynamic[ 0][ i]);
	}

	for ( int i = 1; i < m; i++) {
		for ( int j = 0; j < Pow[ n]; j++) {
			int cnt = 0, ch = 0;
			for ( int k = 0; k < n; k++) {
				if ( ( j >> k) % 2 && ( j >> (k - 1)) % 2) ch = 1;
				if ( ( j >> k) % 2 && ( j >> (k + 1)) % 2) ch = 1;
				if ( ( j >> k) % 2 && String[ i - 1][ k] == 'x') ch = 1;
			}
			if ( ch) continue;
			for ( int l = 0; l < Pow[ n]; l++) {
				ch = 0; cnt = 0;
				for ( int k = 0; k < n; k++) {
					if ( ( l >> k) % 2 && ( l >> (k - 1)) % 2) ch = 1;
					if ( ( l >> k) % 2 && ( l >> (k + 1)) % 2) ch = 1;
					if ( ( l >> k) % 2 && ( j >> (k + 1)) % 2) ch = 1;
					if ( ( l >> k) % 2 && ( j >> (k - 1)) % 2) ch = 1;
					if ( ( l >> k) % 2 && String[ i][ k] == 'x') ch = 1;
					if ( ( l >> k) % 2) cnt++;
				}
				if ( ch) continue;
				Dynamic[ i][ l] = gmax( Dynamic[ i][ l], Dynamic[ i - 1][ j] + cnt);
				ans = gmax( ans, Dynamic[ i][ l]);
			}
		}
	}
}

void outp( void) {

	fprintf( fout, "%d\n", ans);

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


