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

#define DEBUG(x) fout << '>' << #x << ':' << x << endl;
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define FOR2(i, a, b) for (int i = (a); i > (b); --i)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }
const int INF = 1 << 29;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
#ifdef WIN32
typedef __int64 ll;
#else
typedef long long ll;
#endif

/////////////////////////////////////////////////////////////////////////////////////////////////////////////// 

ofstream fout("output.out");
ifstream fin("input.in");

char name[150];
int main()
{
	int T;
	fin >> T;

	FOR(step, 0, T)
	{
		int S;
		fin >> S;
		fin.get();

		map<string, int> names;
		FOR(i, 0, S)
		{
			fin.getline(name, 150);
			names[name] = i;
		}

		int Q;
		fin >> Q;
		fin.get();

		vector<int> dp(S, 0);
		FOR(i, 0, Q)
		{
			fin.getline(name, 150);
			int index = names[name];

			FOR(j, 0, S)
				dp[j] = min(dp[j], dp[index]+1);
			dp[index] = INF;
		}

		int res = INF;
		FOR(i, 0, S)
			res = min(res, dp[i]);

		fout << "Case #" << step+1 << ": " << res << endl;
	}

	return 0;
}
