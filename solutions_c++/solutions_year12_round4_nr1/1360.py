#include <iostream>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <cmath>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <map>
#include <set>
#define ll long long
#define mp(a, b) make_pair(a,b)
#define pb(a) push_back(a)
#define pii pair <int, int>
#define ff first
#define ss second
#define ldb long double
#define sqr(a) ((a) * (a))
#define nextLine() {int c = 0; while((c = getchar()) != 10 && c != EOF);}
#define addEdge(a, b) next[edges] = first[a]; first[a] = edges; end[edges] = a;
#define debug(a) cerr << #a << " = " << (a) << " ";
#define debugl(a) cerr << #a << " = " << (a) << "\n";
const ldb eps = 1e-9;
const ldb pi = fabsl(atan2l(0.0, -1.0));
const ll inf = 1 << 28;
using namespace std;
#define problem "a"

int n, d[123123], l[123123];
map <pair<int, int>, bool> dp;
int usd, D;

void load()
{
	cin >> n;
	for (int i = 0; i < n; i++)
		scanf("%d%d", &d[i], &l[i]);
	cin >> D;

}

bool f(int i, int j)
{
	if (abs(D - d[j]) <= l[j] && abs(D - d[j]) <= d[j] - i)
		return true;
	if (dp.find(mp(i, j)) != dp.end()) return dp[mp(i, j)];
	bool res = 0;
	for (int k = j + 1; !res && k < n; k++)
	{
		if (abs(d[k] - d[j]) > l[j] or abs(d[k] - d[j]) > d[j] - i) break;
		res |= f(d[k] - min(d[k] - d[j], l[j]),k);
	}
	dp[mp(i, j)] = res;
	return res;
}

void solve(int test_number)
{
	dp.clear();
	cerr << "Case #" << test_number << "\n";
	cout << "Case #" << test_number << ": " << (f(0, 0) ? "YES" : "NO") << "\n";
}

int main()
{
	freopen(problem ".in", "rt", stdin);
	freopen(problem ".out", "wt", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		load();
		solve(i + 1);
	}
	return 0;
}

