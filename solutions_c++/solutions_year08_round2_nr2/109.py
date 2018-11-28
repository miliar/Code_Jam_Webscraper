// GCJ Round 1B - Problem B
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

class union_find
{
	private:
		vector<int> p;
	public:
		void init(int n)
		{
			p.resize(n);
			for (int i=0; i<n; i++)
				p[i] = i;
		}
		int find(int k)
		{
			return k == p[k] ? k : (p[k] = find(p[k]));
		}
		int unite(int a, int b)
		{
			if (find(a) == find(b))
				return 0;
			if (rand() % 2)
				p[p[a]] = p[b];
			else
				p[p[b]] = p[a];
			return 1;
		}
};
// code written during the competition follows
bool cmp(VI a, VI b)
{
	FORIT(it, b)
	{
		if (binary_search(a.begin(), a.end(), *it))
			return true;
	}
	return false;
}
int main()
{
	int kase;
	scanf("%d\n", &kase);
	for (int tkase=0; tkase<kase; tkase++)
	{
		int a, b, p;
		cin >> a >> b >> p;
		int n = b - a + 1;
		union_find uf;
		uf.init(n);
		VVI pf(n);
		for (int i=a; i<=b; i++)
		{
			int ix = i-a;
			int z = i;
			for (int j=2; j<=z; j++)
			{	
				if (z % j == 0 && j >= p)
					pf[ix].push_back(j);
				while (z % j == 0)
					z /= j;
			}	
		}
		for (int i=0; i<n; i++)
			for (int j=i+1; j<n; j++)
				if (cmp(pf[i], pf[j]))
					uf.unite(i, j);
		set<int> st;
		for (int i=0; i<n; i++)
			st.insert(uf.find(i));
		printf("Case #%d: %d\n", tkase+1, (int)st.size());
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
