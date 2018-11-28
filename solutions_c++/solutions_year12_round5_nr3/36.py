#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <memory.h>
#include <sstream>
#include <ctime>
using namespace std;

#pragma comment(linker, "/stack:64000000")

typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;

typedef vector<int> vi;
typedef vector<pair<int, int > > vii;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef vector<ld> vld;

typedef vector<vi> vvi;
typedef vector<vii> vvii;
typedef vector<vll> vvll;
typedef vector<vs> vvs;

typedef map<int, int> mpii;
typedef map<int, string> mpis;
typedef map<string, int> mpsi;
typedef map<string, string> mpss;

#define all(a) (a).begin(),(a).end()
#define rall(a) (a).rbegin(),(a).rend()
#define sz(a) (int)((a).size())
#define len(a) (int)((a).length())

#define forr(i,n) for (int i = 0; i < (n); ++i)
#define fori(n) forr(i,n)
#define forj(n) forr(j,n)
#define fork(n) forr(k,n)
#define forin fori(n)
#define forjn forj(n)
#define forjm forj(m)
#define forkm fork(m)
#define foria(a) fori(sz(a))
#define foriv foria(v)
#define foris fori(len(s))
#define forja(a) forj(sz(a))
#define forjv forj(v)
#define forjs forj(len(s))

#define read cin>>
#define write cout<<
#define writeln write endl

#define readt int aaa; read aaa;
#define gett (bbb+1)
#define fort forr(bbb,aaa)

#define issa(a,s) istringstream a(s);
#define iss(s) issa(ss,s);

ld dis(ld x, ld y) {return sqrt(x*x+y*y);}
const ld PI = acos(ld(0.0))*2;

ll gcd(ll a, ll b){return b ? gcd(b,a%b) : a;}

template<class T>
struct makev
{
    vector<T> v;
    makev& operator << (const T& x)
    {
        v.push_back(x);
        return *this;
    }
    operator vector<T>& ()
    {
        return v;
    }
};

void assert(bool b)
{
    if (!b)
        throw 0;
}

const ll inf = 2000000000000000000LL;

ll safeadd(ll a, ll b)
{
	return min(inf, a+b);
}

ll safemul(ll a, ll b)
{
	if (a == 0 || b == 0)
		return 0;

	if (inf / a < b + 1)
		return inf;

	return min(inf, a*b);
}

vector<pair<ll, ll> > v;
ll getCost(ll t)
{
	ll curT = 0;
	ll cost = 0;
	for (int i = 0; i < sz(v); i++)
	{
		ll endT = min(v[i].first, t);
		cost = safeadd(cost, safemul(endT - curT, v[i].second));
		curT = endT;
		if (curT == t)
			return cost;
	}
	return inf;
}

ll m,f;



ll getCost(ll t, ll k)
{
	ll i = t / k;
	ll j = t / k + 1;
	ll cj = t % k;
	ll ci = k - cj;
	return safeadd(safemul(getCost(i), ci), safemul(getCost(j),cj));
}

void prepare()
{
	vector<pair<ll, ll> > v2(v);
	sort(all(v2));
	v.clear();
	for (int i = 0; i < sz(v2); i++)
	{
		while (sz(v) && v.back().second >= v2[i].second)
			v.pop_back();
		v.push_back(v2[i]);
	}
}

bool can(ll t)
{
	if (safeadd(safemul(t, v[0].second), f) > m)
		return false;
	ll l = 1;
	ll r = m / f;
	ll ans = inf;
	if (getCost(t,r) == inf)
		return false;
	ans = min(ans, safeadd(getCost(t,r), r * f));
	if (ans == inf)
		throw 0;
	ans = min(ans, safeadd(getCost(t,l), l * f));
	while (r - l > 3)
	{
		ll t1 = (l + l + r) / 3;
		ll t2 = (l + r + r) / 3;
		ll vt1 = safeadd(getCost(t, t1), t1 * f);
		ll vt2 = safeadd(getCost(t, t2), t2 * f);
		ans = min(ans, vt1);
		ans = min(ans, vt2);
		if (vt1 == vt2 && vt1 == inf)
			l = t1;
		else if (vt1 < vt2)
			r = t2;
		else
			l = t1;
	}
	for (ll i = l; i <= r; i++)
		ans = min(ans, safeadd(getCost(t, i), i * f));
	return ans <= m;
}

ll solve()
{
	ll cur = 0;
	ll step = (1LL << 60);
	while (step)
	{
		ll test = cur + step;
		if (can(test))
			cur = test;
		step /= 2;
	}
	return cur;
}

int main()
{
#ifndef _MSC_VER
    ifstream cin("input.txt");
    ofstream cout("output.txt");
#else
    ifstream cin("input.txt");
    ofstream cout("output.txt");
#endif 

	readt;
	fort
	{
		int n;
		read m;
		read f;
		read n;
		v.resize(n);

		forin {read v[i].second; read v[i].first; ++v[i].first;}
		prepare();

		cout << "Case #" << gett << ": ";
		cout << solve();
		//forin cout  << ' ' << v[i].ndx;
		cout << endl;
	}

    return 0;
}