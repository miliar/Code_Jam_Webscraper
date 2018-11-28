#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <cstring>
using namespace std;
#define MAX 2000000000

int P;
int n;
int C[ 1025];
int D[ 2100][ 11];

int main( void) {
	FILE *fin = fopen ( "input.txt", "rt");
	FILE *fout = fopen ( "output.txt", "wt");
	int tn;
	fscanf ( fin, "%d", &tn);
	for ( int ti = 1; ti <= tn; ti++) {
		fscanf ( fin, "%d", &P);
		n = (1 << (P + 1)) - 1;
		for ( int i = 1; i <= n; i++) {
			for ( int j = 0; j <= P; j++) {
				D[ i][ j] = MAX;
			}
		}

		for ( int i = 0; i < (1 << P); i++) {
			int j = (1 << P) + i, t;
			fscanf ( fin, "%d", &t);
			for ( int k = P - t; k <= P; k++)
				D[ j][ k] = 0;
		}

		for ( int i = 0; i < P; i++) {
			for ( int j = 0; j < ( 1 << ( P - i - 1)); j++) {
				fscanf ( fin, "%d", &C[ (1 << (P - i - 1)) + j ]);
			}
		}

		for ( int i = (1<<P) - 1; i >= 1; i--) {
			for ( int j = 0; j <= P; j++) {
				if ( D[ i * 2][ j] == MAX) continue;
				for ( int k = 0; k <= P; k++) {
					if ( D[ i * 2 + 1][ k] == MAX) continue;
					int l = max( j, k);
					D[ i][ l] = min( D[ i][ l], D[ i * 2][ j] + D[ i * 2 + 1][ k]);
					if ( l) {
						D[ i][ l - 1] = min( D[ i][ l - 1], D[ i * 2][ j] + D[ i * 2 + 1][ k] + C[ i]);
					}
				}
			}						
		}

		fprintf ( fout, "Case #%d: %d\n", ti, D[ 1][ 0]);
	}

	return 0;
}