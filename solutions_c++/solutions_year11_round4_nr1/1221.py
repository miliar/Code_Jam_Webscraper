#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define For(i, a, b) for (int i = (a); i < (b); ++i)
#define Fod(i, a, b) for (int i = (a); i >= (b); --i)
#define Rep(i, a) for (int i = 0; i < (a); ++i)
#define sz(a) ((int)((a).size()))
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define all(a) (a).begin(), (a).end()
#define Sort(a) sort(all(a))

typedef long long ll;
typedef pair <int, int> pii;

int main(int argc, char ** argv)
{
	if (argc > 1)
		freopen(argv[1], "r", stdin);
	int Tn;
	scanf("%d", &Tn);
	Rep(T, Tn) {
		printf("Case #%d: ", T + 1);
		int x, s, r, t, n;
		scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
		int e = 0;
		vector <pair <double, int> > a;
		Rep(i, n) {
			int B, E, w;
			scanf("%d%d%d", &B, &E, &w);
			if (B > e)
				a.pb(mp(s, B - e));
			a.pb(mp(s + w, E - B));
			e = E;
		}
		if (e != x)
			a.pb(mp(s, x - e));
		Sort(a);
		r -= s;
		double left = t;
		double rez = 0;
		Rep(i, sz(a)) {
			double x = (double)a[i].Y / (a[i].X + r);
			if (left >= x) {
				left -= x;
				rez += x;
			}
			else {
				rez += left + (a[i].Y - (a[i].X + r) * left) / a[i].X;
				left = 0;
			}
		}
		printf("%.8lf\n", rez);
	}
	return 0;
}
