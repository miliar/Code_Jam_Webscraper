#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

string S[100];
double WP[100];
double OWP[100];
double OOWP[100];

int main() {
	freopen( "A_Large.in", "r", stdin );
	freopen( "A_Large.out", "w", stdout );
	int TC;
	cin >> TC;

	for( int TCC=1; TCC<=TC; TCC++ ) {
		int N;
		cin >> N;
		for( int i=0; i<N; i++ ) cin >> S[i];
		
		for( int i=0; i<N; i++ ) {
			WP[i] = 0.0;
			double nume = 0.0;
			double deno = 0.0;
			for( int j=0; j<N; j++ ) {
				if( S[i][j] == '0' ) deno += 1.0;
				if( S[i][j] == '1' ) { nume += 1.0; deno += 1.0; }
			}
			WP[i] = nume / deno;
		}

		for( int i=0; i<N; i++ ) {
			OWP[i] = 0.0;
			double NN = 0.0;
			for( int j=0; j<N; j++ ) {
				if( i == j ) continue;
				if( S[i][j] == '.' ) continue;

				double nume = 0.0;
				double deno = 0.0;
				for( int k=0; k<N; k++ ) {
					if( k == i ) continue;
					if( S[j][k] == '.' ) continue;
					nume += S[j][k] - '0';
					deno += 1.0;
				}

				OWP[i] += nume / deno;
				NN += 1.0;
			}
			OWP[i] /= NN;
		}
		for( int i=0; i<N; i++ ) {
			OOWP[i] = 0.0;
			double nume = 0.0;
			double deno = 0.0;
			for( int j=0; j<N; j++ ) {
				if( S[i][j] != '.' ) {
					deno += 1.0;
					OOWP[i] += OWP[j];
				}
			}
			OOWP[i] /= deno;
		}

		cout << "Case #" << TCC << ":" << endl;
		for( int i=0; i<N; i++ ) {
			//cout << WP[i] << ' ' << OWP[i] << ' ' << OOWP[i] << endl;
			printf( "%.12lf\n", 0.25*WP[i] + 0.50*OWP[i] + 0.25*OOWP[i] );
		}
	}
}