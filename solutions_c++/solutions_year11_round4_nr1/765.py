#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

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

using namespace std;

#define FOR(i, b, e)	for(i = (b); i <= (e); i++)
#define FORL(i, b, e)	for(i = (b); i < (e); i++)
#define FORD(i, e, b)	for(i = (e); i >= (b); i--)
#define FOR0(i, e)		FORL(i, 0, e)

#define min(a, b)		(((a) < (b)) ? (a) : (b))
#define max(a, b)		(((a) > (b)) ? (a) : (b))
#define MINA(a, b)		do { if ((a) > (b)) (a) = (b); } while(0)
#define MAXA(a, b)		do { if ((a) < (b)) (a) = (b); } while(0)
#define MINA2(a, b, i, j)		do { if ((a) > (b)) { (a) = (b); (i) = (j); } } while(0)
#define MAXA2(a, b, i, j)		do { if ((a) < (b)) { (a) = (b); (i) = (j); } } while(0)

#define SWAP(a, b)		do { int _t = a; a = b; b = _t; } while(0)
#define SWAPT(a, b, t)	do { t _t = a; a = b; b = _t; } while(0)
#define SQR(a)			((a) * (a))
#define MSET(a, b)		memset(a, b, sizeof(a))

#define INT int

typedef pair<int, int>	II;
typedef vector<int>		VI;
#define ALL(c)			c.begin(), c.end()
#define SZ(c)			((int) c.size())
#define FORALL(it, c)	for(it = c.begin(); it != c.end(); ++it)
#define PB				push_back
#define MP				make_pair
#define P1				first
#define P2				second

multimap<int, int> mp;

int main()
{
	int t, ti, i, n, s, r, e, w, b, x;
	double m, m1, tt, d;
	scanf("%d", &t);
	FOR(ti, 1, t) {
		scanf("%d %d %d %lf %d\n", &x, &s, &r, &tt, &n);
		m = 0;
		mp.clear();
		FOR0(i, n) {
			scanf("%d %d %d", &b, &e, &w);
			mp.insert(MP(w, e - b));
			x -= (e - b);
		}
		mp.insert(MP(0, x));
		multimap<int, int>::iterator it;
		FORALL(it, mp) {
			w = it->first;
			d = it->second;
			m1 = (double) d / (w + r);
			if (m1 <= tt) {
				tt -= m1;
				m += m1;
			} else {
				d -= tt * (w + r);
				m += tt;
				tt = 0;
				m1 = (double) d / (w + s);
				m += m1;
			}
		}
		printf("Case #%d: %lf\n", ti, m);
	}
	return 0;
}
