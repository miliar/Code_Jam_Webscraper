#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <sstream>
using namespace std;
#pragma comment(linker, "/STACK:255000000")

typedef long long ll;

#define rep(i, a, b) for(i = (a); i < (b); ++i)
#define repb(i, a, b) for(i = (a) - 1; i >= (b); --i)
#define repd(i, a, b, d) for(i = (a); i < (b); i += (d))
#define repbd(i, a, b, d) for(i = (a) - 1; i >= (b); i -= (d))
#define reps(i, s) for(i = 0; (s)[i]; ++i)
#define repl(i, l) for(i = l.begin(); i != l.end(); ++i)

#define in(f, a) scanf("%"#f, &(a))

bool firstout = 1;

#define out(f, a) printf("%"#f, (a))
#define outf(f, a) printf((firstout) ? "%"#f : " %"#f, (a)), firstout = 0
#define nl printf("\n"), firstout = 1

#define all(x) (x).begin(),(x).end()
#define sqr(x) ((x) * (x))
#define mp make_pair

template<class T>
T &minn(T &a, T b)
{
	if(b < a) a = b;
	return a;
}

template<class T>
T &maxx(T &a, T b)
{
	if(a < b) a = b;
	return a;
}

#define inf 1012345678
#define eps 1e-9


#ifdef XDEBUG
#define mod 23
#else
#define mod 1000000009
#endif

int &madd(int &a, int b)
{
	a += b;
	if(a >= mod) a -= mod;
	return a;
}

int &msub(int &a, int b)
{
	a -= b;
	if(a < 0) a += mod;
	return a;
}

int &mmult(int &a, int b)
{
	return a = (ll)a * b % mod;
}

int mdiv(ll a, ll b, ll m)
{
	a = (a % m + m) % m;
	b = (b % m + m) % m;
	if(a % b == 0) return a / b;
	return (a + m * mdiv(-a, m, b)) / b;
}

#define N 33
#define M 1012

int n, m, l, si, sj;
char S[N][N];

int gcd(int a, int b)
{
	for(; b;) a %= b, swap(a, b);
	return a;
}

int lcm(int a, int b)
{
	return a / gcd(a, b) * b;
}

int corner(int w1, int w2)
{
	return 2 * w1 + w2;
}

ll abs(ll x)
{
	if(x < 0) return -x;
	return x;
}

bool mv(ll d, int i, int j, ll x, ll y, ll vx, ll vy, ll l, ll lx = 0, ll ly = 0)
{
	if(l < sqr(lx) + sqr(ly)) return 0;
	if(i == si && j == sj && !(x == d / 2 && y == d / 2))
	{
		if(vx * (d / 2 - y) - vy * (d / 2 - x) == 0) return sqr(lx + abs(d / 2 - x)) + sqr(ly + abs(d / 2 - y)) <= l;
	}
	int px = - 2 * (x == 0) + 1;
	int py = - 2 * (y == 0) + 1;
	if(S[i][j])
	{
		if((x == 0 || x == d) && (y == 0 || y == d))
		{
			int r = corner(S[i + px][j], S[i][j + py]);
			if(r == 0) return 0;
			if(r == 1) return mv(d, i + px, j, x - px * d, y, vx * -1, vy, l, lx, ly);
			if(r == 2) return mv(d, i, j + py, x, y - py * d, vx, vy * -1, l, lx, ly);
			if(r == 3) return mv(d, i + px, j + py, x - px * d, y - py * d, vx * -1, vy * -1, l, lx, ly);
		}
		if(x == 0 || x == d) 
			return mv(d, i + px, j, x - px * d, y, vx * -1, vy, l, lx, ly);
		else
			return mv(d, i, j + py, x, y - py * d, vx, vy * -1, l, lx, ly);
	}
	int t;
	px = - 2 * (vx < 0) + 1;
	py = - 2 * (vy < 0) + 1;
	if(vx != 0 && (vy == 0 || abs((x - (vx > 0) * d) / vx) <= abs((y - (vy > 0) * d) / vy)))
	{		
		t = abs((x - (vx > 0) * d) / vx);
		if(!(vy && t == abs((y - (vy > 0) * d) / vy))) py = 0;
	}
	else
	{
		px = 0;
		t = abs((y - (vy > 0) * d) / vy);
	}
	lx += abs(vx * t);
	ly += abs(vy * t);
	x += vx * t;
	y += vy * t;
	return mv(d, i + px, j + py, x - px * d, y - py * d, vx, vy, l, lx, ly);
}

int main()
{
	freopen("d.in", "rt", stdin);
#ifdef XDEBUG	
#else
	freopen("d.out", "wt", stdout);
#endif

	int i, j, k;
	char c;
	int a, d;
	
	int ts;	
#if 1
	int tss;
	in(d, tss);
	rep(ts, 1, tss + 1)
#else
	for(ts = 1; in(d, n) > 0; ++ts)
#endif
	{
		in(d, n); in(d, m); in(d, l);
		rep(i, 0, n) in(s, S[i]);
		rep(i, 0, n) rep(j, 0, m)
		{
			if(S[i][j] == 'X') si = i, sj = j;
			S[i][j] = S[i][j] == '#';
		}
		int res = 0;

		rep(i, 0, l + 1) rep(j, 0, l + 1)
		{
			if(i == 0 && j == 0) continue;
			if(sqr(i) + sqr(j) <= sqr(l) && gcd(i, j) == 1)
			{
				d = max(lcm(i, j), 1);
				res += mv(2 * d, si, sj, d, d, i, j, (ll)4 * sqr(d) * sqr(l));
				if(j) res += mv(2 * d, si, sj, d, d, i, -j, (ll)4 * sqr(d) * sqr(l));
				if(i) res += mv(2 * d, si, sj, d, d, -i, j, (ll)4 * sqr(d) * sqr(l));
				if(i && j) res += mv(2 * d, si, sj, d, d, -i, -j, (ll)4 * sqr(d) * sqr(l));
			}
		}

		printf("Case #%d: ", ts);
		out(d, res); nl;

		cerr << ts << endl;
	}

	return 0;
}
