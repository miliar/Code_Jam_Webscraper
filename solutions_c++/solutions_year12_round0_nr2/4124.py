
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cassert>

using namespace std;

class Triple
{
public:
	Triple( int t, bool surprising = false )
	{
		int median = t / 3;
		if ( t % 3 == 2 )
			++median;
		if ( surprising )
		{
			p[ 0 ] = median - 1;
			p[ 1 ] = median + 1;
			p[ 2 ] = median - 1 + (t + 1) % 3;
		}
		else
		{
			p[ 0 ] = median;
			p[ 1 ] = median;
			p[ 2 ] = median - 1 + (t + 1) % 3;
		}
		assert( isValid() );
	}

	int getTotalPoints() const
	{
		return accumulate( p, p + 3, 0 );
	}

	int getBestResult() const
	{
		return *max_element( p, p + 3 );
	}

	bool isSurprising() const
	{
		return *max_element( p, p + 3 ) - *min_element( p, p + 3 ) == 2;
	}

	bool canBeSurprising() const
	{
		int t = getTotalPoints();
		return t != 0 && t != 1 && t != 29 && t != 30;
	}

	Triple getSurprising() const
	{
		return Triple( getTotalPoints(), true );
	}

	Triple getNotSurprising() const
	{
		return Triple( getTotalPoints(), false );
	}

	bool hasScore( int sc ) const
	{
		return getBestResult() >= sc;
	}

protected:
	bool isValid() const
	{
		return 0 <= p[ 0 ] && p[ 0 ] <= 10 
			&& 0 <= p[ 1 ] && p[ 1 ] <= 10 
			&& 0 <= p[ 2 ] && p[ 2 ] <= 10;
	}

	int p[ 3 ];
};

int main()
{
	int T;
	cin >> T;
	for ( int t = 1; t <= T; ++t )
	{
		int N, S, p;
		cin >> N >> S >> p;
		vector< Triple > v;
		vector< bool > w;
		for ( int i = 0; i < N; ++i )
		{
			int t;
			cin >> t;
			v.push_back( Triple( t ) );
			w.push_back( false );
		}
		for ( int i = 0; i < N; ++i )
		{
			assert( ! v[ i ].isSurprising() );
			if ( v[ i ].canBeSurprising() && ! v[ i ].hasScore( p ) && v[ i ].getSurprising().hasScore( p ) )
			{
				w[ i ] = true;
				if ( S > 0 )
				{
					v[ i ] = v[ i ].getSurprising();
					--S;
				}
			}
		}
		for ( int i = 0; i < N; ++i )
		{
			if ( v[ i ].canBeSurprising() && ! w[ i ] )
			{
				if ( S > 0 )
				{
					v[ i ] = v[ i ].getSurprising();
					--S;
				}
			}
		}
		assert( S == 0 );
		int r = 0;
		for ( int i = 0; i < N; ++i )
		{
			if ( v[ i ].hasScore( p ) )
				++r;
		}
		cout << "Case #" << t << ": " << r << endl;
	}

	return 0;
}
