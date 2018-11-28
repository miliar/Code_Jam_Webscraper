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
#define fd(a,b,c) for (a = (b); a >= (c); a--)
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
const double EPS = 1e-9;

void prepare()
{
	freopen("a-large.in", "r", stdin);
	freopen("a-large.out", "w", stdout);
}

void panic(bool expression = false)
{
	if (!expression)
	{
		cerr << "PANIC!" << endl;
		assert(false);
	}
}

bool eq(double a, double b)
{
	return fabs(a - b) < EPS;
}

struct C
{
	double x;
	int type;
	C(){}
	C(double x, int type) : x(x), type(type)
	{
	}
	bool operator < (const C &c) const
	{
		return eq(x, c.x) && type < c.type || x < c.x;
	}
};

struct G
{
	int b, e, w;
	G(){}
	G(int b, int e, int w) : b(b), e(e), w(w) {}
	bool operator < (const G &g) const
	{
		//return w < g.w || w == g.w && e - b > g.e - g.b;
		return b < g.b || b == g.b && e < g.e;
	}
};

bool ms(const G &a, const G &b)
{
	return a.w < b.w;
}

int n;

double calc(vector<G> &g, int r, int s, double x)
{
	double res = 0;
	fi(sz(g))
	{
		double cr = (double)(g[i].e - g[i].b) / (g[i].w + r);
		if (cr < 0)
			cr = 0;
		if (res + cr > x)
		{
			x -= res;
			if (x < 0)
				x = 0;
			res += x;
			x = g[i].b + x * (g[i].w + r);
			if (x > g[i].e)
				x = g[i].e;
			res += (g[i].e - x) / (g[i].w + s);
			r = s;
			x = 1e20;
		}
		else
			res += cr;
	}
	return res;
}

void solve(int test_num)
{
	//cerr << test_num << endl;
	printf("Case #%d: ", test_num);
	int len, s, r, t;
	scanf("%d%d%d%d%d", &len, &s, &r, &t, &n);
	vector<G> g(n);
	fi(n)
		scanf("%d%d%d", &g[i].b, &g[i].e, &g[i].w);
	sort(all(g));
	double x = r * t;
	double res = 0;
	int pr = 0;
	vector<G> v;
	fi(n)
	{
		v.pb(G(pr, g[i].b, 0));
		pr = g[i].e;
	}
	v.pb(G(pr, len, 0));
	fi(n)
		v.pb(g[i]);
	sort(all(v), ms);
	res += calc(v, r, s, t);
	printf("%.9lf\n", res);
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