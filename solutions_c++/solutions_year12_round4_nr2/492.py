
#include <iostream>

#include <vector>
#include <string>

#include <utility>

#include <algorithm>

using namespace std;

int tests;

int N;
long long W, L;
vector< pair<int,int> > r;
vector< pair<int,int> > p;
vector< int > rre;


int hit_with( int x, int y, int r )
{
	for( int i=0; i<N; ++i )
	{
		if ( p[i].first < 0 )
			continue;
		const int rr = r + rre[i];
		if ( abs( x - p[i].first ) < rr && abs( y - p[i].second ) < rr )
			return i;
	}
	return -1;
}

int main()
{
	cin >> tests;

	for( int curTest=0; curTest<tests; ++curTest )
	{


		cin >> N >> W >> L;
		rre = vector< int >( N );
		p = r = vector< pair<int,int> >( N );
		for( int i=0; i<N; ++i )
		{
			int rr;
			cin >> rr;
			r[i] = make_pair( rr, i );
			rre[i] = rr;
		}

		sort( r.begin(), r.end() );
		do
		{
			bool ok = true;
			for( int i=0; i<N; ++i )
				p[i] = make_pair( -1, -1 );
			for( int i=0; i<N; ++i )
			{
				const int idx = r[i].second;
				const int h = r[i].first/2 + r[i].first%2;
				bool br = false;
				for( int x=0; x<=W; x+=h )
				{
					for( int y=0; y<=L; y+=h )
					{
						if ( hit_with( x, y, r[i].first ) == -1 )
						{
							p[idx].first = x;
							p[idx].second = y;
							br = true;
							break;
						}
					}
					if ( br )
						break;
				}
				if ( !br )
				{
					ok = false;
					break;
				}
			}
			if ( ok )
				break;
		} while( next_permutation( r.begin(), r.end() ) );

		cout << "Case #" << (curTest+1) << ": ";
		for( int i=0; i<N; ++i )
		{
			cout << " " << p[i].first << " " << p[i].second;
		}
		cout << endl;
	}

	return 0;
}

