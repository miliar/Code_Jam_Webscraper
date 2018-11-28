#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:64000000")

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
//#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long ll;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<bool> vb;

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int)((x).size()))

#define forn(i, x) for (int i = 0; i < int(x); i++)
#define fors(i, x) forn(i, sz(x))

template<typename T> T sqr(T x) { return x * x;            }
template<typename T> T abs(T x) { return (x > 0) ? x : -x; }

int t;

int rdt()
{
	int h, m;
	scanf("%d:%d", &h, &m);
	return h * 60 + m;
}

struct Ev
{
	int time;
	int type;
	int where;
	
	Ev(int time, int type, int where): time(time), type(type), where(where) {}
};

bool operator < (const Ev &a, const Ev &b)
{
	if (a.time != b.time) return a.time < b.time;
	if (a.type != b.type) return a.type < b.type;
	return a.where < b.where;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int nt;
	scanf("%d", &nt);
	forn(it, nt)
	{
		scanf("%d", &t);
		int na, nb;
		scanf("%d%d", &na, &nb);
		vii ab, ba;
		forn(i, na)
		{
			int t1 = rdt();
			int t2 = rdt();
			ab.pb(mp(t1, t2));
		}
		forn(i, nb)
		{
			int t1 = rdt();
			int t2 = rdt();
			ba.pb(mp(t1, t2));
		}
		vector<Ev> e;
		fors(i, ab)
		{
			e.pb(Ev(ab[i].first, 1, 0));
			e.pb(Ev(ab[i].second + t, 0, 1));
		}
		fors(i, ba)
		{
			e.pb(Ev(ba[i].first, 1, 1));
			e.pb(Ev(ba[i].second + t, 0, 0));
		}
		sort(all(e));
		int cur[2], ans[2];
		cur[0] = cur[1] = ans[0] = ans[1] = 0;
		fors(i, e)
		{
			if (e[i].type)
			{
				if (!cur[e[i].where]) ans[e[i].where]++;
				else cur[e[i].where]--;
			}
			else cur[e[i].where]++;
		}
		printf("Case #%d: %d %d\n", it + 1, ans[0], ans[1]);
	}
	return 0;
}
