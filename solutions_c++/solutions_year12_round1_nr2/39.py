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

#define N 1012
#define M 1012

int n, m;
pair<int, int> AA[N];
int X[N];
bool B[N];

int main()
{
	freopen("b.in", "rt", stdin);
#ifdef XDEBUG	
#else
	freopen("b.out", "wt", stdout);
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
		in(d, n);
		rep(i, 0, n)
		{
			in(d, X[i]);
			in(d, AA[i].first);
			AA[i].second = i;
			B[i] = 0;
		}
		sort(AA, AA + n);

		int res = 0, r = 0;
		for(j = 0; j < n;) if(j < n && AA[j].first <= r)
		{
			++r; ++res;
			if(!B[AA[j].second])
			{
				++r;
				B[AA[j].second] = 1;
			}
			++j;
		}
		else
		{
			repb(i, n, 0) if(!B[AA[i].second] && X[AA[i].second] <= r) break;
			if(i < 0) break;
			++r; ++res;
			B[AA[i].second] = 1;
		}

		printf("Case #%d: ", ts);
		if(r != 2 * n) out(s, "Too Bad");
		else out(d, res); nl;

		cerr << ts << endl;
	}

	return 0;
}
