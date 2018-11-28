// gcc version 4.5.0 (tdm-1)
// g++ -I tr1 femidav.cpp -O2 -Wall -std=c++0x -o femidav.exe
// femidav < small-attempt0.in > small-attempt0.out
// femidav < large.in > large.out

#include <cstdio>
#include <vector>
#include <algorithm>

typedef std::vector<int> VI;
#define FOR(I, N) for( int I = 0, end_ = (N); I < end_; ++I )
int ri() { int r; scanf("%d", &r); return r; }
VI const rvi( int n ) { VI r(n); FOR(i, n) r[i] = ri(); return r; }

int main()
{
	FOR(i, ri())
	{
		int N = ri(), L = ri(), H = ri();
		VI F = rvi(N);

		bool printed = false;
		for( int f = L; f <= H && !printed; ++f )
		{
			bool harmony = true;
			for( int n = 0; n < N; ++n )
				harmony = harmony && ( std::max(f, F[n]) % std::min(f, F[n]) == 0 );
			if ( harmony )
				printf( "Case #%d: %d\n", i + 1, f ), printed = true;
		}
		if ( ! printed )
			printf( "Case #%d: NO\n", i + 1 );
	}
}
