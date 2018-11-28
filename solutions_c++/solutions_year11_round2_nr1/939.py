#include <iostream>
#include <fstream>
#define MAX 200
#define cin fin
#define cout fout
using namespace std;

double WP[MAX], OWP[MAX], OOWP[MAX];
int n, T;
char b[MAX][MAX];

ifstream fin( "A-large(2).in" );
ofstream fout( "o.txt" );

int main(){
	cin >> T;
	for( int tt = 1; tt <= T; tt++ ){
		cin >> n;
		for( int i = 0;i < n; i++ )
			for( int j = 0;j < n; j++ )
				cin >> b[i][j];
		for( int i = 0;i < n; i++ ){
			int w = 0, l = 0;
			for( int j = 0;j < n; j++ )
				if( b[i][j] == '1' )
					w++;
				else if( b[i][j] == '0' )
					l++;
			WP[i] = (double)w / (double)( l + w );
		}
		for( int i = 0;i < n; i++ ){
			int cnt = 0;
			double sum = 0;
			for( int j = 0;j < n; j++ )
				if( b[i][j] != '.' ){
					int w = 0, l = 0;
					cnt++;
					for( int k = 0;k < n; k++ ){
						if( k != i ){
							if( b[j][k] == '1' )
								w++;
							else if( b[j][k] == '0' )
								l++;
						}
					}
					sum += (double)w / (double)( w + l );
				}
			OWP[i] = sum / (double)cnt;
		}
		for( int i = 0;i < n; i++ ){
			int cnt = 0;
			double sum = 0;
			for( int j = 0;j < n; j++ )
				if( b[i][j] != '.' )
					sum += OWP[j], cnt++;
			OOWP[i] = sum / (double)cnt;
		}
		cout << "Case #" << tt << ":" << endl;
		cout.setf( ios::showpoint | ios::fixed );
		cout.precision( 8 );
		for( int i = 0;i < n; i++ )
			//printf( "%.8lf\n", 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i] );
			cout << 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i] << endl;
	}
	return 0;
}