#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main ()
{
	freopen( "C-large.in", "r", stdin );
	freopen( "C-large.out", "w", stdout );
	int t, k;
	cin >> t;
	for( k = 1;  k <= t; ++k )
	{
		
		
		int n;
		cin >> n;
		int sum = 0;
		int sumx = 0;
		int mn = 2000000000;
		vector< int > v( n );
		int i;
		for( i = 0; i < n; ++i )
		{
			cin >> v[ i ];
			mn = min( mn, v[ i ] );
			sum += v[ i ];
			sumx = sumx ^ v[ i ];
		}
		cout << "Case #" << k << ": ";
		if( sumx != 0 )
			cout << "NO\n";
		else
			cout << sum - mn << endl;
	}
	return 0;
}