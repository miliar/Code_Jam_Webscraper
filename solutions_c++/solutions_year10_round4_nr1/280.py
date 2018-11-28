#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <cstring>
using namespace std;
#define sqr( a) (( a) * ( a))
int K, L;
int Data[ 500][ 500];

int dy[ 4] = { 1, 1, -1, -1}, dx[ 4] = { 1, -1, 1, -1};

bool is_inside( int y, int x) {
	if ( 1 <= y && y <= L) 
		return 1 <= x && x <= L;
	return false;
}

int is_ok( int y, int x) {

	int d = 0;

	for ( int i = 1; i <= L; i++) {
		for ( int j = 1; j <= L; j++) {
			int dis_y = i - y, dis_x = j - x;
			if ( Data[ i][ j] != -1) {
				d = max ( d, abs(dis_y) + abs(dis_x));
			}
			for ( int k = 0; k < 4; k++) {
				int wy = y + dis_y * dy[ k];
				int wx = x + dis_x * dx[ k];
				if ( is_inside( wy, wx)) {
					if ( Data[ i][ j] != -1 && Data[ wy][ wx] != -1 && Data[ wy][ wx] != Data[ i][ j])
						return 0;
				}
			}
		}
	}

	return d + 1;
}

int prs( void) {
	int ret = 1000000000;

	for ( int i = 1; i <= L; i++) {
		for ( int j = 1; j <= L; j++) {
			int r;
			if ( r = is_ok( i, j)) {
				ret = min( ret, sqr( r) - sqr( K));				
			}
		}
	}
	return ret;
}

int main( void) {
	FILE *fin = fopen ( "input.txt", "rt");
	FILE *fout = fopen ( "output.txt", "wt");
	int tn;
	fscanf ( fin, "%d", &tn);
	for ( int ti = 1; ti <= tn; ti++) {

		fscanf ( fin, "%d", &K);
		L = 2 * K - 1;

		for ( int i = 1; i <= L; i++) {
			for ( int j = 1; j <= L; j++) {
				Data[ i][ j] = -1;
			}
		}

		for ( int i = 1; i <= K; i++) {
			for ( int j = 1; j <= i; j++) {
				fscanf ( fin, "%d", &Data[ i][ K - i + j * 2 - 1]);
			}
		}
		for ( int i = K + 1; i < 2 * K; i++) {
			for ( int j = 1; j <= 2 * K - i; j++) { 
				fscanf ( fin, "%d", &Data[ i][ i - K + j * 2 - 1]);
			}
		}
		if ( K == 1) {
			fprintf ( fout, "Case #%d: %d\n", ti, 0);
		} else {
			fprintf ( fout, "Case #%d: %d\n", ti, prs());
		}
	}

	return 0;
}