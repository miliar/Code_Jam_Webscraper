#include <cstdio>
#include <algorithm>
using namespace std;

int G[ 1000];
int NextS[ 1000], VisitR[ 1000], Value[ 1000];
long long VisitV[ 1000];

int main( void) {
	FILE *fin = fopen( "input.txt", "rt");
	FILE *fout = fopen ( "output.txt", "wt");
	int tn;
	fscanf ( fin, "%d", &tn);

	for ( int tc = 1; tc <= tn; tc++) {
		int R, N, K;
		fscanf ( fin, "%d %d %d", &R, &K, &N);
		for ( int i = 0; i < N; i++)
			fscanf ( fin, "%d", &G[ i]);
		for ( int i = 0; i < N; i++) {
			int v, p;
			v = 0, p = i;
			while ( v + G[ p] <= K) {
				v += G[ p];
				p++;
				if ( p == N)
					p = 0;
				if ( p == i)
					break;
			}
			NextS[ i] = p;
			Value[ i] = v;
			VisitR[ i] = 0;
			VisitV[ i] = 0;
		}
		
		long long v;
		int p;
		v = 0, p = 0;
		for ( int i = 1; i <= R; i++) {
			if ( VisitR[ p] && R - i + 1 >= i - VisitR[ p]) {
				int cl = i - VisitR[ p];
				long long cv = v - VisitV[ p];
				int round = ( R - i + 1) / cl;
				v += cv * round;
				i += cl * round;
				for ( ; i <= R; i++) {
					v += Value[ p];
					p = NextS[ p];
				}
			} else {
				VisitR[ p] = i;
				VisitV[ p] = v;
				v += Value[ p];
				p = NextS[ p];
			}
		}
		fprintf ( fout, "Case #%d: %lld\n", tc, v);
	}
	return 0;
}