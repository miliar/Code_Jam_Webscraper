// GCJ Round X - Problem C
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
bool bipartite_matching(int act, int m, int n, const VVI &adj, VI &left, VI &right, VI &visited)
{
	for (VI::const_iterator it = adj[act].begin(); it != adj[act].end(); ++it)
	{
		if (visited[*it])
			continue;
		visited[*it] = 1;
		if (right[*it] == -1 || bipartite_matching(right[*it], m, n, adj, left, right, visited))
		{
			left[act] = *it;
			right[*it] = act;
			return true;
		}
	}
	return false;
}
// code written during the competition follows
int A[1024][1024];
int main()
{
	int kase;
	scanf("%d\n", &kase);
	for (int tkase=0; tkase<kase; tkase++)
	{
		printf("Case #%d: ", tkase+1);
		int n, k;
		cin >> n >> k;
		for (int i=0; i<n; i++)
			for (int j=0; j<k; j++)
				cin >> A[i][j];
		VVI adj(n);
		for (int i=0; i<n; i++)
		{
			for (int j=0; j<n; j++)
			{
				bool good = true;
				for (int z=0; z<k; z++)
					if (A[j][z] >= A[i][z])
					{
						good = false;
						break;
					}
				if (good)
					adj[i].push_back(j);
			}
		}
		VI left(n, -1), right(n, -1);
		int cnt = 0;
		for (int i=0; i<n; i++)
		{
			VI visited(n, 0);
			if (bipartite_matching(i, n, n, adj,  left, right, visited))
				cnt++;
		}
		cout << n - cnt << endl;
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
