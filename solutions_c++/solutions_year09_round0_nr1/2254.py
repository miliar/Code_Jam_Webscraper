// GCJ Qualification Round - Problem A
// -- strapahuulius

// pre-written code follows
// #includes {{{
#include <algorithm>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;
// }}}
// constants, typedefs, macros {{{
typedef long long LL;
typedef unsigned long long ULL;
const int oo = 1000000000;
const LL OO = 1000000000000000000LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<string> VS;
typedef queue<int> QI;
typedef queue<PII> QPII;
typedef complex<double> tComp;
const double PI = 2.0 * acos(0.0);
const double EPS = 1e-9;
#define FORIT(i,c) for (typeof((c).end()) i=(c).begin(); i!=(c).end(); ++i)
#define CERR(x) cerr << (#x) << " = " << (x) << endl
#define COUT(x) cout << (#x) << " = " << (x) << endl
// }}}

// code written during the competition follows

string w[1<<13];
int d, l;

int countMatches(const string &pattern)
{
	int cnt = 0;
	for (int i = 0; i < d; i++)
	{
		bool match = true;
		for (int j = 0, k = 0; j < l && match; j++, k++)
		{
			if (pattern[k] == '(')
			{
				while(pattern[k] != ')' && pattern[k] != w[i][j])
					k++;
				if (pattern[k] == ')')
					match = false;
				while(pattern[k] != ')')
					k++;
			}
			else if (pattern[k] != w[i][j])
				match = false;
		}
		if (match)
			cnt++;
	}
	return cnt;
}

int main()
{
	int n;
	cin >> l >> d >> n;
	for (int i = 0; i < d; i++)
		cin >> w[i];
	string pattern;
	for (int p = 1; p <= n; p++)
	{
		cin >> pattern;
		cout << "Case #" << p << ": " << countMatches(pattern) << endl;
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
