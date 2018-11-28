
#include <iostream>

using namespace std;

bool is_possible( long long N, int Pd, int Pg )
{
	if ( Pg == 100 && Pd != 100 )
		return false;
	if ( Pg == 0 && Pd != 0 )
		return false;
	int d;
	for ( d = 1; d <= 100; ++d )
		if ( ( Pd * d ) % 100 == 0 )
			break;
	return d <= N;
}

int main()
{
	int T;
	cin >> T;
	for ( int tc = 1; tc <= T; ++tc ) {
		long long n;
		int pd, pg;
		cin >> n >> pd >> pg;
		cout << "Case #" << tc << ": " << 
			( is_possible( n, pd, pg ) ? "Possible" : "Broken" ) << 
			endl;
	}
	return 0;
}
