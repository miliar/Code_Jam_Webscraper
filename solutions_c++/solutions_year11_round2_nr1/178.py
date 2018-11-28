// GCJ Round 1B - Problem A
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
string a[128];
double WP[128], OWP[128];
int main()
{
	int kase;
	scanf("%d\n", &kase);
	for (int tkase=0; tkase<kase; tkase++)
	{
		printf("Case #%d:\n", tkase+1);
		int n;
		cin >> n;
		for (int i=0; i<n; i++)
		{
			string tmp;
			cin >> tmp;
			a[i] = tmp;
		}
		for (int i=0; i<n; i++)
		{
			int total = 0;
			int won = 0;
			OWP[i] = 0.0;
			for (int j=0; j<n; j++)
			{
				if (a[i][j] != '.')
				{
					total++;
					won += a[i][j] - '0';
					int oTotal = 0;
					int oWon = 0;
					for (int k=0; k<n; k++)
						if (i != k && a[j][k] != '.')
						{
							oTotal++;
							oWon += a[j][k] - '0'; 
						}
					OWP[i] += (double)oWon / oTotal;
				}
			}
			WP[i] = (double)won / total;
			OWP[i] /= total;
		}
		for (int i=0; i<n; i++)
		{
			double OOWP = 0.0;
			int cnt = 0;
			for (int j=0; j<n; j++)
				if (a[i][j] != '.')
				{
					OOWP += OWP[j];
					cnt++;
				}
			OOWP /= cnt;
			printf("%.9f\n", 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP);
		}
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
