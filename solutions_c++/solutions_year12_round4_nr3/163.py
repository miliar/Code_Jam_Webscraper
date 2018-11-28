// GCJ Round 2 - Problem C
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
bool check(const vector<LL> height, int a, int b)
{
	int n = height.size();
	for (int i=a+1; i<n; i++)
	{
		if (i == b)
			continue;
		LL B = (height[b] - height[a]) * (i - a);
		LL C = (height[i] - height[a]) * (b - a);
		if (i < b)
		{
			if (B <= C)
				return false;
		}
		else
		{
			if (B < C)
				return false;
		}
	}
	return true;
}
int main()
{
	int kase;
	scanf("%d\n", &kase);
	for (int tkase=0; tkase<kase; tkase++)
	{
		int n;
		cin >> n;
		vector<int> x(n - 1);
		bool possible = true;
		for (int i=0; i<n-1; i++)
		{
			cin >> x[i];
			x[i]--;
			if (x[i] <= i)
			{
				possible = false;
			}
		}
		vector<LL> height(n, 1);
		int steps = 0;
		int current = 0;
		const int MAX_STEPS = 1000000;
		if (!possible)
			steps = MAX_STEPS;
		while (current < n - 1 && steps < MAX_STEPS)
		{
			steps++;
			bool changed = false;
			while (!check(height, current, x[current]) && steps < MAX_STEPS)
			{
				height[x[current]]++;
				changed = true;
				steps++;
			}
			if (changed)
				current = 0;
			else
				current++;
		}
		printf("Case #%d:", tkase+1);
		if (steps >= MAX_STEPS)
		{
			cout << " Impossible" << endl;
		}
		else
		{
			for (int i=0; i<n; i++)
				cout << " " << height[i];
			cout << endl;
		}
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
