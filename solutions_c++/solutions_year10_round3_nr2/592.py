#include <iostream>
#include <vector>
using namespace std;

int factor( int n, int p, int c )
{
	int res = 0;

	double dn = n;
	double dp = p;

	while( dn > dp )
	{
		dn /= c;
		++res;
	}

	return res;
}

int main( )
{
	freopen( "B.in", "rt", stdin );
	freopen( "B.out", "wt", stdout );

	int T = 0;
	cin >> T;

	for( int ct = 0; ct < T; ++ct )
	{
		int L, P, C;
		cin >> L >> P >> C;
		int best = INT_MAX;

		vector<long long > bottoms;

		long long cur = L*C;

		while( cur < P )
		{
			bottoms.push_back( cur );
			cur *= C;
		}

		vector<long long > ups;

		cur = ( P + 1 ) / C;

		while( cur > L )
		{
			ups.push_back( cur );
			cur = ( cur + 1 ) / C;
		}

		int res1 = 0;

		int pp = 1;

		int s = bottoms.size( );

		while( s > 0 )
		{
			++res1;
			s /= 2;
		}

		s = ups.size( );

		int res2 = 0;

		while( s > 0 )
		{
			++res2;

			s/= 2;
		}

		best = max( res1, res2 );

		cout << "Case #" << ct + 1<< ": " << best << endl;
	}
}
