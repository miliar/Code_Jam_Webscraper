#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#define P pair< long long, int >
#define MAX 300
#define cin fin
#define cout fout
using namespace std;

ifstream fin( "B-small-attempt3.in" );
ofstream fout( "o.txt" );
int t, n;
long long d;
P cord[MAX];

long long ABS( long long bd ){
	return bd < 0 ? -bd : bd;
}

int main()
{
	cin >> t;
	for( int T = 1; T <= t; T++ ){
		cin >> n >> d;
		for( int i = 0;i < n; i++ ){
			cin >> cord[i].first >> cord[i].second;
			cord[i].first *= 2;
		}
		d *= 2;
		sort( cord, cord + n );
		long long l = 0, r = ( 1LL << 60 );
		//long long l = 0, r = 10;
		long long res;
		while( l <= r ){
			long long mid = ( l + r ) / 2;
			long long leftMost = 0;
			bool fir = 1;
			bool can = true;
			for( int i = 0; i < n; i++ )
				for( int j = 0;j < cord[i].second; j++ ){
					if( leftMost + mid < cord[i].first || fir == 1 )
						leftMost = cord[i].first - mid, fir = false;
					else if( ( leftMost + d - cord[i].first ) > mid ){
						can = false;
						break;
					}
					else leftMost += d;
				}
			if( can )
				res = mid, r = mid - 1;
			else l = mid + 1;
		}
		cout << "Case #" << T << ": " << res / 2 << ".";
		if( res % 2 == 0 )
			cout << "000000" << endl;
		else cout << "500000" << endl;
	}
	return 0;
}