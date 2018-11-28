
#include <iostream>

#include <vector>
#include <string>

#include <algorithm>

using namespace std;

int tests;

long long HI;

long long lcm( long long l, long long r )
{
	long long ll = min( l, r );
	long long rr = max( l, r );
	long long cur = ll;
	long long mm = rr;
	while( cur < mm )
	{
		cur += ll;
		while( cur > mm )
			mm += rr;
		if ( cur == mm )
			return cur;
		if ( cur > HI )
			break;
	}
	return -1;
}

bool check( int l, int r )
{
	if ( max( l, r )%min( l, r ) == 0 )
		return true;
	return false;
}


int main()
{
	cin >> tests;

	for( int curTest=0; curTest<tests; ++curTest )
	{

		int N, L, H;
		cin >> N >> L >> H;
		vector<int> a( N, 0 );
		for( int i=0; i<N; ++i )
			cin >> a[i];

		HI = H;

		long long ret;
		if ( L == 1 )
			ret = 1;
		else
		{
			ret = -1;
			const int mmm = H;
			for( int i=L; i<=mmm; ++i )
			{
				bool b_ok = true;
				for( int j=0; j<N&&b_ok; ++j )
					if ( !check( i, a[j] ) )
						b_ok = false;
				if ( b_ok )
				{
					ret = i;
					break;
				}
			}
		}

		cout << "Case #" << (curTest+1) << ": ";
		if ( ret == -1 )
			cout << "NO";
		else
			cout << ret;
		cout << endl;
	}

	return 0;
}

