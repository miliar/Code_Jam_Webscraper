// gcc version 4.5.0 (tdm-1)
// g++ -I tr1 femidav.cpp -O2 -Wall -fpermissive -o femidav.exe
// femidav < C-small-attempt0.in > C-small-attempt0.out
// femidav < C-large.in > C-large.out

#include <cstdio>
#include <vector>
#include <algorithm>
#include <numeric>

#define FOR(I, N) for( int I = 0, end_ = (N); I < end_; ++I )
#define FORN(I, IN, N) for( int I = IN, end_ = (N); I < end_; ++I )
int ri() { int r; scanf("%d", &r); return r; }
typedef std::vector<int> VI;
VI const rvi( int n ) { VI r(n); FOR(i, n) r[i] = ri(); return r; }

int main()
{
	FOR(i, ri())
	{
		VI C = rvi(ri());

		bool dividable = true;
		FOR(j, 32)
		{
			int count = 0;
			FOR(k, C.size())
				if ( C[k] & (1 << j) )
					++count;
			if ( count % 2 )
				dividable = false;
		}

		if ( dividable )
			printf( "Case #%d: %d\n", i + 1, std::accumulate(C.begin(), C.end(), 0) - *std::min_element(C.begin(), C.end()) );
		else
			printf( "Case #%d: NO\n", i + 1 );
	}
}
