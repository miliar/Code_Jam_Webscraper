
#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

struct segment
{
	segment( double l_, int w_ )
		: l( l_ ), w( w_ ) {}

	double l;
	int w;
};

bool operator<( const segment& lhs, const segment& rhs )
{
	return lhs.w < rhs.w;
}

int main()
{
	int TC;
	cin >> TC;
	for ( int tc = 1; tc <= TC; ++tc ) {
		int X, S, R, N;
		double t;
		cin >> X >> S >> R >> t >> N;
		vector< segment > v;
		for ( int i = 0; i < N; ++i ) {
			int b, e;
			int w;
			cin >> b >> e >> w;
			v.push_back( segment( e - b, w + S ) );
			X -= (e - b);
		}
		v.push_back( segment( X, S ) );
		sort( v.begin(), v.end() );
		R -= S;
		assert( R > 0 );
		for ( int i = 0; i < (int)v.size() && t > 0.0; ++i ) {
			double t2 = (double)(v[i].l) / (double)(v[i].w + R);
			if ( t2 <= t ) {
				v[i].w += R;
				t -= t2;
			}
			else {
				double dx = t * (double)(v[i].w + R);
				v[i].l -= dx;
				v.push_back( segment( dx, v[i].w + R ) );
				t = 0.0;
				break;
			}
		}
		double T = 0.0;
		for ( int i = 0; i < (int)v.size(); ++i ) {
			T += ((double)v[i].l) / ((double)v[i].w);
		}
		cout << "Case #" << tc << ": " << 
			setiosflags( ios::fixed | ios::showpoint ) << setprecision( 7 ) << T << endl;
	}

	return 0;
}
