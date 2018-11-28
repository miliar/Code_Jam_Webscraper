// GCJ Round 1B - Problem C
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
		int K, n;
		cin >> K >> n;
		VI d;
		for (int i=0; i<n; i++)
		{
			int x;
			cin >> x;
			d.push_back(x);
		}
		VI v(K, -1);
		int j = 0;
		for (int i=1; i<=K; i++)
		{
//			cout << i << endl;
			int cnt = 0;
			while (1)
			{
				if (v[j] == -1)
				{
					cnt++;
					if (cnt == i)
					{
						break;
					}
				}
				j++;
				if (j == K)
					j = 0;
			}
			v[j] = i;
		}
		printf("Case #%d:", tkase+1);
		FORIT(it, d)
			cout << " " << v[*it-1];
		cout << endl;
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
