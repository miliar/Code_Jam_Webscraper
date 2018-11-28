#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
using namespace std;

int main( void) {

	FILE *fin = fopen ( "input.txt", "rt");
	FILE *fout = fopen ( "output.txt", "wt");

	int tn;
	fscanf ( fin, "%d", &tn);

	for ( int ti = 1; ti <= tn; ti++) {
		int N, M, D, I;
		int A[ 100];
		int Dynamic[ 100][ 256];
		int ans;
		fscanf ( fin, "%d %d %d %d", &D, &I, &M, &N);
		for ( int i = 0; i < N; i++)
			fscanf ( fin, "%d", &A[ i]);
		ans = D * N;


		for ( int j = 0; j <= 255; j++) {
			int d = abs( j - A[ 0]);
			Dynamic[ 0][ j] = D;
			Dynamic[ 0][ j] = min( Dynamic[ 0][ j], d);
		}

		for ( int i = 1; i < N; i++) {
			for ( int j = 0; j <= 255; j++) {
				int d = abs( j - A[ i]);
				Dynamic[ i][ j] = ( i + 1) * D;
				Dynamic[ i][ j] = min( Dynamic[ i][ j], i * D + d);
			}

			for ( int j = 0; j <= 255; j++)
				for ( int k = j + 1; k <= j + M && k <= 255; k++)
					Dynamic[ i - 1][ k] = min( Dynamic[ i - 1][ k], Dynamic[ i - 1][ j] + I);

			for ( int j = 255; j >= 0; j--)
				for ( int k = j - 1; k >= j - M && k >= 0; k--)
					Dynamic[ i - 1][ k] = min( Dynamic[ i - 1][ k], Dynamic[ i - 1][ j] + I);

			for ( int j = 0; j <= 255; j++) {
				Dynamic[ i][ j] = min( Dynamic[ i][ j], Dynamic[ i - 1][ j] + D);
				for ( int k = 0; k <= 255; k++) {
					if ( abs( k - j) <= M)
						Dynamic[ i][ j] = min( Dynamic[ i][ j],
							Dynamic[ i - 1][ k] + abs( A[ i] - j));
				}
			}
		}

		for ( int j = 0; j <= 255; j++)
			for ( int k = j + 1; k <= j + M && k <= 255; k++)
				Dynamic[ N - 1][ k] = min( Dynamic[ N - 1][ k], Dynamic[ N - 1][ j] + I);

		for ( int j = 255; j >= 0; j--)
			for ( int k = j - 1; k >= j - M && k >= 0; k--)
				Dynamic[ N - 1][ k] = min( Dynamic[ N - 1][ k], Dynamic[ N - 1][ j] + I);

		for ( int i = 0; i <= 255; i++)
			ans = min ( ans, Dynamic[ N - 1][ i]);


		fprintf ( fout, "Case #%d: %d\n", ti, ans);
	}

	fclose( fin);
	fclose( fout);

	return 0;
}