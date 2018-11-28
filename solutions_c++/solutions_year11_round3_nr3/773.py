#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <numeric>
#include <cassert>
using namespace std;

long long gcd(long long a, long long b)
{
    while( 1 )
    {
        a = a % b;
		if( a == 0 )
			return b;
		b = b % a;

        if( b == 0 )
			return a;
    }
}

long long lcm(long long a, long long b)
{
	return a * b / gcd( a, b );
}

int main( )
{
	freopen( "input.txt", "rt", stdin );
	freopen( "output.txt", "wt", stdout );

	int cases = 0;
	cin >> cases;


	for( int ct = 0; ct < cases; ++ct )
	{
		int N, L, H;
		cin >> N >> L >> H;

		vector<int> freqs;

		for( int i = 0; i < N; ++i )
		{
			int t = 0;
			cin >> t;
			freqs.push_back( t );
		}

		int res = 0;

		for( int sz = L; sz <= H; ++sz )
		{
			vector< bool > inHarmony( N, true );

			for( int j = 0; j < N; ++j )
			{
				if( freqs[ j ] % sz  != 0 && sz % freqs[ j ] != 0 )
				{
					inHarmony[ j ] = false;
				}
			}

			long long musiciansLCM = 1;

			bool inHarmonyWithAll = true;

			for( int i = 0; i < N; ++i )
			{
				if( ! inHarmony[ i ] )
				{
					musiciansLCM = lcm( musiciansLCM, freqs[ i ] );
					inHarmonyWithAll = false;
				}
			}

			if( inHarmonyWithAll )
			{
				res = sz;
				break;
			}
		}

		if( res == 0 )
		{
			cout << "Case #" << ct + 1 << ": NO" << endl;
		}
		else
		{
			cout << "Case #" << ct + 1 << ": " << res << endl;
		}

	}
}