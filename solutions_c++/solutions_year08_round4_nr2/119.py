#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
using namespace std; 

#define DEBUG(x) cerr << '>' << #x << ':' << x << endl;
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define FOR2(i, a, b) for (int i = (a); i > (b); --i)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }
const int INF = 1 << 29;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
#ifdef WIN32
typedef __int64 ll;
#else
typedef long long ll;
#endif

/////////////////////////////////////////////////////////////////////////////////////////////////////////////// 

ofstream fout("output.out");
ifstream fin("input.in");

int main()
{
	int T;
	fin >> T;

	FOR(step, 0, T)
	{
		ll N, M, A;
		fin >> N >> M >> A;

		bool r = false;
		FOR(x1, 0, N+1)
		{
			FOR(y1, 0, M+1)
			{
				FOR(x2, 0, N+1)
				{
					FOR(y2, 0, M+1)
					{
						if (x1*y2-x2*y1==A)
						{
							fout << "Case #" << step+1 << ": 0 0 " << x1 << " " << y1 << " " << x2 << " " << y2 << endl;
							r = true;
							break;
						}
					}
					if(r)break;
				}
				if(r)break;
			}
			if(r)break;
		}
		if (!r) fout << "Case #" << step+1 << ": IMPOSSIBLE" << endl;
	}

	return 0;
}
