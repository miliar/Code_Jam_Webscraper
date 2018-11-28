#if 1
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <functional>
#include <cstring>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <ctime>
#include <cassert>
#include <sstream>
#include <iostream>
#include <bitset>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int , int> pii;
typedef vector <int> veci;
typedef vector <veci> graph;
const LD eps = 1e-9;
const LD pi = acos(-1.0);
const int inf = 1000 * 1000 * 1000;
const LL inf64 = LL(inf) * inf;

#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) {cerr << #x << " = " << x << endl;}
#define dbgv(x) {cerr << #x << " ={"; for (int _i = 0; _i < x.size(); _i++) {if (_i) cerr << ", "; cerr << x[_i];} cerr << "}" << endl;}
#define NAME "problem"

void solve(int test)
{
	int n;
	scanf("%d", &n);
	vector<int> d(n), l(n);
	for(int i = 0; i < n; ++i)
		scanf("%d%d", &d[i], &l[i]);
	
	int D;
	scanf("%d", &D);
	d.pb(D);
	l.pb(D);
	n = d.size();
	int start = 0, dist = d[0];

	while(true)
	{
		// dbg(start);
		// dbg(dist);
		int next = -1, ndist = -1, nlen = -1;
		for(int i = start + 1; i < n; ++i)
		{
			// dbg(i);
			// dbg((d[i] - d[start] <= dist));
			// dbg((d[i] - d[start] <= l[i]));
			// dbg(d[i]);
			// dbg(l[i]);
			if(d[i] - d[start] <= dist)
			{
				int maxd = min(2 * d[i] - d[start], d[i] + l[i]);
				if(maxd >= nlen)
				{
					nlen = maxd;
					ndist = min(l[i], d[i] - d[start]);
					next = i;
				}
			}
		}
		if(next == -1)
			break;
		start = next;
		dist = ndist;
	}
	// dbg(start);
	if(d[start] + dist >= D)
		cout << "Case #" << test << ": " << "YES" << endl;
	else
		cout << "Case #" << test << ": " << "NO" << endl;
}


void solve2(int test)
{
	int n;
	scanf("%d", &n);
	vector<int> d(n), l(n);
	for(int i = 0; i < n; ++i)
		scanf("%d%d", &d[i], &l[i]);
	
	int D;
	scanf("%d", &D);
	d.pb(D);
	l.pb(D);
	
	n = d.size();

	vector<int> dp(n, -1);
	dp[0] = d[0];

	for(int i = 0; i < n; ++i)
		for(int j = i + 1; j < n; ++j)
			if(d[j] - d[i] <= dp[i])
			{
				dp[j] = max(dp[j], min(l[j], d[j] - d[i]));
			}

	if(dp.back() != -1)
		cout << "Case #" << test << ": " << "YES" << endl;
	else
		cout << "Case #" << test << ": " << "NO" << endl;
}

int main()
{
	//freopen("input.txt", "r", stdin); //freopen("output.txt", "w", stdout);
	//freopen(NAME ".in","r",stdin);freopen(NAME ".out","w",stdout);

	int tests; cin >> tests;
	for(int t = 1; t <= tests; ++t)
		solve2(t);

	return 0;
}
/*************************
*************************/
#endif
