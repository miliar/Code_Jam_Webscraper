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

int count(const vector<int> & perm, const string & str)
{
	string str2 = str;
	int index = 0;
	while (index < str2.size())
	{
		FOR(i, 0, perm.size()) str2[index+perm[i]] = str[index+i];
		index += perm.size();
	}

	int res = 0;
	FOR(i, 0, str2.size())
		if (!i || str2[i-1] != str2[i]) ++res;
	return res;
}

int main()
{
	int T;
	fin >> T;

	FOR(step, 0, T)
	{
		int K;
		string str;
		fin >> K >> str;

		vector<int> perm;
		FOR(i, 0, K) perm.push_back(i);

		int res = INF;
		do
		{
			res = min(res, count(perm, str));
		} while (next_permutation(perm.begin(), perm.end()));
		fout << "Case #" << step+1 << ": " << res << endl;
	}

	return 0;
}
