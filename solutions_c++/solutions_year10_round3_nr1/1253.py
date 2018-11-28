#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int, int> PII;
int ri() { int r; scanf( "%d", &r ); return r; }
PII rip() { int f, s; scanf( "%d%d", &f, &s ); return make_pair( f, s ); }
bool operator < ( const PII& l, const PII& r ) { return l.first < r.first; }

int main()
{
	freopen( "A-large.in", "rt", stdin );
	freopen( "A-large.in.out", "wt", stdout );

	int T = ri();	
	for( int n = 0; n < T; ++n )
	{
		int N = ri();
		vector<PII> data;
		for( int i = 0; i < N; ++i )
			data.push_back( rip() );
		sort( data.begin(), data.end() );
		int answer = 0;
		for( int i = 0; i < data.size(); ++i )
			for( int j = 0; j < data.size(); ++j )
				if ( (data[j].first < data[i].first && data[j].second > data[i].second) 
					|| (data[j].first > data[i].first && data[j].second < data[i].second) )
					++answer;
		printf( "Case #%d: %d\n", n + 1, answer/2 );
	}
}
