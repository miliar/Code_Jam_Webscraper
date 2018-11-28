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
bool solve (vi v, int left, int minLine, int prev, bool bar = false)
{
	bool ok = true;
	foriv if (v[i] != -1) ok = false;
	if (ok) return true;
	if (!left) return false;
	if (solve(v, left - 1, minLine + 1, -1000))
		return true;

	int barMax = 0;
	while (barMax < sz(v) && v[barMax] >= minLine) ++barMax;
	fori(barMax)
	{
		vi v2 = v;
		int mn = 10000;
		forj(i+1) mn = min(mn, v[j]);
		forj(i+1) if (v[j] == mn) v2[j] = -1;
		bool ok = true;
		forja(v) if (j > i && v[j] == mn) ok = false;

		if (ok && prev < 0 || bar && prev == mn || !bar && prev + 1 == mn)
			if (solve(v2, left - 1, max(minLine, mn + 1), mn + 1, true))
				return true;
	}

	foriv if (v[i] >= minLine) if (prev <= 0 || prev == v[i] || !bar && prev + 1 == v[i])
	{
		vi v2 = v;
		v2[i] = -1;
		if (solve(v2, left - 1, max(v[i], minLine), v[i]))
			return true;
	}
	return false;
}

bool solve (vi v)
{
//	if (v == vector<int>(makev<int>() << 2 << 4 << 4 << 4 << 2 << 0))
//		return true;
	int m = *min_element(all(v));
	while (find(all(v), m) != v.end())
		*find(all(v), m) = -1;
	return solve(v, 4, -1, -20);
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
	string s;
	getline(cin,s);
	fort
	{
		int a,b;
		read a;
		read b;
		int ans = 0;
		for (int i = a; i <= b; i++)
		{
			string s;
			char buf[20];
			sprintf(buf, "%d", i);
			s = buf;

			set<int> st;
			for (int j = 1;j<len(s); j++)
			{
				char c = s.back();
				s.erase(s.begin() + s.length() - 1);
				s = c + s;
				int val = atoi(s.c_str());
				if (i < val && val <= b)
					st.insert(val);
			}
			ans += (int)st.size();
		}
		cout << "Case #" << gett << ": " << ans << endl;
		std::cout << "Case #" << gett << ": " << ans << endl;
	}
    return 0;
}