#include <iostream>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define debuging

#ifdef debuging
#define FIN  {freopen("new.in" , "r" , stdin) ;}
#define FOUT {freopen("new.out" , "w" , stdout) ;}
#define OUT(x)  {cout<< #x << "  : " << x <<endl ;}
#define ERR(x)  {cout<<"#error: "<< x ; while(1) ;}
#endif

#ifndef debuging
#define FIN  ;
#define FOUT ;
#define OUT(x)  ;
#define ERR(x)  ;
#endif

#define rep(i,a,b) for(int i=(a);i<(int)(b);i++)
#define REP(i,n) rep(i,0,(n))
#define SZ(x) (int)((x).size())
#define CLR(a) memset((a),0,sizeof (a))
#define all(c) (c).begin(), (c).end()
#define iter(c) __typeof((c).begin())
#define contains(c, e) (find(all(c), (e)) != (c).end())
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> vint;
typedef set<int> sint;
typedef pair<int, int> pint;

const int maxint = -1u >> 2;
const double eps = 1e-8;
const double pi = acos(-1.0);

const int mn = 5005;

struct walkway {
	int s, e, w;
} a[mn];

bool cmppos(const walkway &a, const walkway &b) {
	return a.s < b.s;
}
bool cmpw(const walkway &a, const walkway &b) {
	return a.w < b.w;
}

int X, S, R, t, N;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int Tn;
	scanf("%d", &Tn);
	for (int Tc = 1; Tc <= Tn; ++Tc) {
		scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
		for (int i = 0; i < N; ++i) {
			scanf("%d%d%d", &a[i].s, &a[i].e, &a[i].w);
		}

		sort(a, a + N, cmppos);
		int newN = N;
		for (int i = 0; i < N; ++i)
			if (i == 0 && a[i].s != 0) {
				a[newN].s = 0, a[newN].e = a[i].s, a[newN].w = 0;
				++newN;
			} else if (i != 0 && a[i].s != a[i - 1].e) {
				a[newN].s = a[i - 1].e, a[newN].e = a[i].s, a[newN].w = 0;
				++newN;
			}
		if (a[N - 1].e != X) {
			a[newN].s = a[N - 1].e, a[newN].e = X, a[newN].w = 0;
			++newN;
		}
		sort(a, a + newN, cmpw);
		double ans = 0, rest = t;
		for (int i = 0; i < newN; ++i) {
			double l = (a[i].e - a[i].s);
			double need = l / (a[i].w + R);
			if (need <= rest) {
				rest -= need;
				ans += need;
			} else {
				double run = rest * (a[i].w + R);
				ans += rest;
				ans += (l - run) / (a[i].w + S);
				rest = 0;
			}
		}

		printf("Case #%d: ", Tc);
		// output statement(s);
		printf("%.10f\n", ans);
	}

	return 0;
}
