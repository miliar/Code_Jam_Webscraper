#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <memory.h>
#include <cassert>

using namespace std;

#define fo(a,b,c) for (int a = (b); a < (c); a++)
#define fr(a,b) fo(a, 0, (b))
#define fi(n) fr(i, (n))
#define fj(n) fr(j, (n))
#define fk(n) fr(k, (n))
#define fd(a,b,c) for (int a = (b); a >= (c); a--)
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define _(a,b) memset((a), (b), sizeof(a))
#define __(a) memset((a), 0, sizeof(a))
#define sz(a) (int)(a).size()
#define mp make_pair
#define pb push_back

typedef long long lint;
typedef unsigned long long ull;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int, int> PII;

const int INF = 1 << 30;
const lint LINF = 1LL << 60;
const double EPS = 1e-9;

void prepare()
{
	freopen("b-large.in", "r", stdin);
	freopen("b-large.out", "w", stdout);
}

void panic(bool expression = false)
{
	if (!expression)
	{
		cerr << "PANIC!" << endl;
		assert(false);
	}
}

const int maxn = 205;

int n, d;
pair<int, int> x[maxn];
vector<lint> xx;
vector<double> v;

bool good(double t)
{
	double x = v[0] - t;
	fo(i, 1, sz(v))
	{
		if (v[i] + t < x + d - EPS)
			return false;
		x = max(x + d, v[i] - t);
	}
	return true;
}

void solve(int test_num)
{
	cerr << test_num << endl;
	printf("Case #%d: ", test_num);
	scanf("%d%d", &n, &d);
	fi(n)
		scanf("%d%d", &x[i].first, &x[i].second);
	sort(x, x + n);
	v.clear();
	fi(n)
	{
		fj(x[i].second)
			v.pb(x[i].first);
	}
	double l = 0, r = 1e15;
	fi(60)
	{
		double f = (r + l) / 2;
		if (good(f))
			r = f;
		else
			l = f;
	}
	printf("%.2lf\n", (l + r) / 2);
}

int main()
{
	prepare();
	int number_of_tests;
	cin >> number_of_tests;
	fi(number_of_tests)
		solve(i + 1);
	return 0;
}