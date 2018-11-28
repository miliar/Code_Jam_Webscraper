#include<cstdio>
#include<algorithm>
#include<string>
using namespace std;

int n;
struct M { 
	string s;
	int least;
} Matrix[ 40];

int prs( void) {

	bool change = 1;
	int ans = 0;

	for ( int i = 0; i < n; i++) {
		Matrix[ i].least = 0;
		for  ( int j = n - 1; j >= 0; j--) {
			if ( Matrix[ i].s[ j] == '1') {
				Matrix[ i].least = j;
				break;
			}
		}
	}

	while( change) {

		change = 0;

		for ( int i = 0; i < n; i++) {
			if ( i < Matrix[ i].least) {
				for ( int j = i + 1; j < n; j++) {
					if ( i >= Matrix[ j].least) {
						change = 1;
						for ( int k = j - 1; k >= i; k--) {
							swap( Matrix[ k], Matrix[ k + 1]);
							ans++;
						}
						break;
					}
				}
			}
		}				
	}

	return ans;
}

int main( void) {

	int testnum;
	FILE *fin = fopen ( "input.txt", "rt");
	FILE *fout = fopen ( "output.txt", "wt");

	fscanf( fin, "%d", &testnum);
	char buf[ 42];

	for ( int testcase = 1; testcase <= testnum; testcase++) {
		fscanf( fin, "%d", &n);
		for ( int i = 0; i < n; i++) {
			fscanf( fin, "%s", buf);
			Matrix[ i].s = buf;
		}

		fprintf( fout, "Case #%d: %d\n", testcase, prs());

	}
	return 0;
}