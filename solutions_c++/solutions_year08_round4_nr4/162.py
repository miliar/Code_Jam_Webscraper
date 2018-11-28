// GCJ Round 2 - Problem D
// I can't tell you how proud I am,
// I'm writing down things that I don't understand.
// -- blackmath

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
int main()
{
	int kase;
	scanf("%d\n", &kase);
	for (int tkase=0; tkase<kase; tkase++)
	{
		int k;
		cin >> k;
		string s;
		cin >> s;
		printf("Case #%d: ", tkase+1);
		VI perm(k);
		for (int i=0; i<k; i++)
			perm[i] = i;
		int n = s.size();
		int best = oo;
		do
		{
			string t(n, '?');
			for (int i=0; i<n; i+=k)
			{
				for (int j=0; j<k; j++)
					t[i+j] = s[i+perm[j]];
			}
			int cnt = 1;
			for (int i=1; i<n; i++)
				if (t[i] != t[i-1])
					cnt++;
			best <?= cnt;
		} while (next_permutation(perm.begin(), perm.end()));
		cout << best << endl;
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
