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
	int n, s, p;
	cin >> n >> s >> p;
	vector<int> a(n);
	for(int i = 0; i < n; ++i)
		cin >> a[i];

	vector<int> sc(n);
	vector<int> imp(n);
	vector<bool> used(n);
	for(int i = 0; i < n; ++i)
	{
		sc[i] = (a[i] + 2) / 3;
		if(a[i] % 3 != 1)
		{
			if(a[i] > 0)
				imp[i] = 1;
		}
	}

//	dbgv(sc);
//	dbgv(imp);

	vector< vector<int> > dp(n + 1, vector<int>(s + 1, 0));
	for(int i = 1; i <= n; ++i)
		for(int j = 0; j <= s; ++j)
		{
			dp[i][j] = max(dp[i][j], dp[i - 1][j] + (sc[i - 1] >= p));
			if(j < s)
				dp[i][j + 1] = max(dp[i][j], dp[i - 1][j] + (sc[i - 1] + imp[i - 1] >= p));
		}

	int cnt = dp[n][s];
	cout << "Case #" << test << ": " << cnt << endl;
}

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	//freopen(NAME ".in","r",stdin);freopen(NAME ".out","w",stdout);

	int tests; cin >> tests;
	for(int test = 1; test <= tests; ++test)
		solve(test);

	return 0;
}
/*************************
*************************/
#endif
