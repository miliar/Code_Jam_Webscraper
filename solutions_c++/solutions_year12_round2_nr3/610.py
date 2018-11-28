#include <iostream>
#include <algorithm>
#include <fstream>
#define P pair< int, int >
using namespace std;

int sm[( 1 << 20 )], T, C = 1, n, arr[20];
P rev[( 1 << 20 )];

ifstream fin( "C1.in" );
ofstream fout( "C1.out" );
#define cin fin
#define cout fout

void ff( int mask ){
	int fir = true;
	for( int i = 0; i < n; i++ )
		if( mask & ( 1 << i ) ){
			if( !fir )
				cout << ' ';
			cout << arr[i];
			fir = false;		
		}
	cout << endl;
}

int main()
{
	for( cin >> T; T--; ){
		memset( sm, 0, sizeof sm );
		cin >> n;
		for( int i = 0; i < n; i++ )
			cin >> arr[i];
		for( int i = 0; i < ( 1 << n ); i++ )
			for( int j = 0; j < n; j++ )
				if( i & ( 1 << j ) )
					sm[i] += arr[j];
		for( int i = 0; i < ( 1 << n ); i++ )
			rev[i] = P( sm[i], i );
		sort( rev, rev + ( 1 << n ) );
		cout << "Case #" << C++ << ":" << endl;
		bool f = false;
		for( int i = 1; i < ( 1 << n ); i++ )
			if( rev[i].first == rev[i - 1].first ){
				int m1 = rev[i].second, m2 = rev[i - 1].second;
				for( int j = 0; j < n; j++ )
					if( ( m1 & ( 1 << j ) ) && ( m2 & ( 1 << j ) ) )
						m1 -= ( 1 << j ), m2 -= ( 1 << j );
				ff( m1 );
				ff( m2 );
				f = true;
				break;
			}
		if( ! f )
			cout << "Impossible" << endl;
	}
	return 0;
}