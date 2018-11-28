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

int aa[110];

#define INT_CAP	0x3F3F3F3F

int main()
{
	int t, ti, c, d, p, v, tm, i, n; 
	scanf("%d", &t);
	FOR(ti, 1, t) {
		scanf("%d %d", &c, &d);
		d *= 2;
		aa[0] = -INT_CAP;
		n = 1;
		FOR0(i, c) {
			scanf("%d %d", &p, &v);
			while(v--)
				aa[n++] = p * 2;			
		}
		aa[n--] = INT_CAP;
		tm = 0;
		while(1) {
			FOR(i, 1, n)
				if (aa[i] - aa[i - 1] < d)
					break;
			if (i == n + 1)
				break;
			tm++;
			FOR(i, 1, n) {
				if (aa[i] - aa[i - 1] > d)
					aa[i]--;
				else if (aa[i + 1] - aa[i] >= d)
					aa[i]++;
			}
		}
		printf("Case #%d: %.1lf\n", ti, 0.5 * tm);
	}
	return 0;
}
