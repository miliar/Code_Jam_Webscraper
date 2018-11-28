// gcc version 4.5.0 (tdm-1)
// g++ -I tr1 femidav.cpp -O2 -Wall -fpermissive -o femidav.exe
// femidav < A-small-attempt0.in > A-small-attempt0.out
// femidav < A-large.in > A-large.out

#include <cstdio>
#include <vector>
#include <utility>
#include <iostream>
#include <cmath>

typedef std::pair<char, int> PCI;
typedef std::vector<PCI> VPCI;

#define FOR(I, N) for( int I = 0, end_ = (N); I < end_; ++I )
int ri() { int r; scanf("%d", &r); return r; }
PCI rpci() { char f[2]; int s; scanf("%s%d", f, &s); return std::make_pair(f[0], s); }
VPCI const rvpci( int n ) { VPCI r(n); FOR(i, n) r[i] = rpci(); return r; }

int main()
{
	FOR(i, ri())
	{
		VPCI v = rvpci(ri());

		int O_pos = 1, O_time = 0, B_pos = 1, B_time = 0, T = 0;
		FOR( j, v.size() )
		{
			PCI task = v[j];
			int time_needed = std::abs(task.second - (task.first =='O' ? O_pos : B_pos)) + 1;
			int time_avail = T - (task.first =='O' ? O_time : B_time);
			T += std::max(time_needed - time_avail, 1);
			(task.first =='O' ? O_time : B_time) = T;
			(task.first =='O' ? O_pos : B_pos) = task.second;
		}

		printf( "Case #%d: %i\n", i + 1, T );
	}
}
