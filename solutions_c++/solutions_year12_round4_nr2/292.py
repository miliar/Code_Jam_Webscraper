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
int x[3000], y[3000];

int n,w,l;

struct item
{
	int yf, yt;
	int xf;
};

void solve(vii v)
{
	sort(all(v));
	item it;
	it.yf = 0;
	it.yt = l;
	it.xf = 0;
	vector<item> items;
	items.push_back(it);

	while (v.size())
	{
		if (!items.size())
			throw 0;

		item cur = items.back();
		items.pop_back();
		int rr = v.back().first;
		int ndx = v.back().second;
		
		int yfr = (cur.yf == 0 ? -rr : cur.yf);
		int ytr = yfr + rr + rr;
		int xfr = (cur.xf == 0 ? -rr : cur.xf);
		int xtr = xfr + rr + rr;
		if (xfr + rr > w)
			continue;
		if (cur.yt - yfr >= 2 * (ytr - yfr))
		{
			item it1, it2;
			it1.xf = it2.xf = cur.xf;
			it1.yf = cur.yf;
			it1.yt = ytr;
			it2.yf = ytr;
			it2.yt = cur.yt;
			items.push_back(it2);
			items.push_back(it1);
			continue;
		}
		cur.xf = xtr;
		items.push_back(cur);
		x[ndx] = xfr + rr;
		y[ndx] = yfr + rr;
		v.pop_back();
	}
}

int main()
{
#ifndef ONLINE_JUDGE
    ifstream cin("input.txt");
    ofstream cout("output.txt");
#else
    ifstream cin("towers.in");
    ofstream cout("towers.out");
#endif

	readt;
	fort
	{
		read n;
		read w;
		read l;
		vii v(n);
		forin read v[i].first;
		forin v[i].second = i;
		solve(v);

		cout << "Case #" << gett << ":";
		forin cout << ' ' << x[i] << ' ' << y[i];
		writeln;
	}
}