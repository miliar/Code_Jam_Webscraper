#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <string.h>
#include <math.h>

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

int main()
{
	int t, ti, n, p[2], w[2], i, d, r, tm, t1;
	char s[2];
	scanf("%d", &t);
	FOR(ti, 1, t) {
		scanf("%d", &n);
		p[0] = 1;
		p[1] = 1;
		w[0] = 0;
		w[1] = 0;
		tm = 0;
		FOR0(i, n) {
			scanf("%s %d", s, &d);
			r = *s == 'B' ? 1 : 0;
			t1 = max(1, abs(p[r] - d) + 1 - w[r]);
			w[1 - r] += t1;
			tm += t1;
			w[r] = 0;
			p[r] = d;
		}
		printf("Case #%d: %d\n", ti, tm);
	}
	return 0;
}
