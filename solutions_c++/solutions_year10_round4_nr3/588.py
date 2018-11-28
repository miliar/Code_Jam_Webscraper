#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <cstring>
using namespace std;
#define N 1000
#define S 401

int n;
vector < int > Line;
int X1[ N], X2[ N], Y1[ N], Y2[ N];
int Data[ 2][ S][ S];

int prs( void) {
	int ret = 0;
	for ( int i = 0; i < S; i++) {
		for ( int j = 0; j < S; j++) {
			Data[ 0][ i][ j] = 0;
		}
	}
	for ( int i = 0; i < n; i++) {
		for ( int y = Y1[ i]; y <= Y2[ i]; y++) {
			for ( int x = X1[ i]; x <= X2[ i]; x++) {
				Data[ 0][ y][ x] = 1;
			}
		}
	}

	int sw = 0, ch = 1;
	while ( ch) {
		ret++;
		for ( int i = 1; i < S; i++) {
			for ( int j = 1; j < S; j++) {
				Data[ !sw][ i][ j] = 0;
			}
		}
		ch = 0;
		for ( int i = 1; i < S; i++) {
			for ( int j = 1; j < S; j++) {
				if ( Data[ sw][ i][ j] && ( Data[ sw][ i - 1][ j] || Data[ sw][ i][ j - 1]))
					Data[ !sw][ i][ j] = 1;
				if ( Data[ sw][ i - 1][ j] && Data[ sw][ i][ j - 1])
					Data[ !sw][ i][ j] = 1;
				if ( Data[ !sw][ i][ j])
					ch = 1;
			}
		}
		sw = !sw;
	}

	return ret;
}

int main( void) {
	FILE *fin = fopen ( "input.txt", "rt");
	FILE *fout = fopen ( "output.txt", "wt");
	int tn;
	fscanf ( fin, "%d", &tn);
	for ( int ti = 1; ti <= tn; ti++) {
		fscanf ( fin, "%d", &n);
		Line.clear();
		for ( int i = 0; i < n; i++) {
			fscanf ( fin, "%d %d %d %d", &X1[ i], &Y1[ i], &X2[ i], &Y2[ i]);
			Line.push_back( X1[ i] + Y1[ i]);
			Line.push_back( X1[ i] + Y2[ i]);
			Line.push_back( X2[ i] + Y1[ i]);
			Line.push_back( X2[ i] + Y2[ i]);
		}
		sort( Line.begin(), Line.end());
		Line.erase( unique( Line.begin(), Line.end()), Line.end());

		fprintf ( fout, "Case #%d: %d\n", ti, prs());
	}

	return 0;
}