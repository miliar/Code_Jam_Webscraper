#include <iostream>
#include <fstream>
#define EPS 1e-10
#define MAX 1000
using namespace std;

int S[MAX], n, T, C = 1;

ifstream fin( "A.in" );
ofstream fout( "A.out" );
#define cin fin
#define cout fout

int main()
{
	for( cin >> T; T--; ){
		double sum = 0;
		cin >> n;
		for( int i = 0; i < n; i++ ){
			cin >> S[i];
			sum += S[i];
		}
		cout << "Case #" << C++ <<":";
		for( int idx = 0; idx < n; idx++ ){
			double l = 0, r = 1;
			for( int iter = 0; iter < 300; iter++ ){
				double mid = ( l + r ) / 2.;
				double val = S[idx] + sum * mid;
				double rem = 1. - mid;
				for( int i = 0; i < n; i++ ){
					if( i == idx )
						continue;
					if( S[i] - EPS > val )
						continue;
					rem -= ( val - S[i] ) / sum;
				}
				//cout << mid << ' ' << rem << endl;
				if( rem + EPS < 0 )
					r = mid;
				else l = mid;
			}
			cout.setf( ios::showpoint | ios::fixed );
			cout.precision( 8 );
			cout << ' ' << l * 100.;
		}
		cout << endl;
	}
	return 0;
}