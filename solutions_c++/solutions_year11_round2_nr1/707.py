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

typedef struct tow {
	int w;
	int a;
	double wp;
	double owp;
	double oowp;
} tow;

char m[100][100];
tow o[100];

int main()
{
	int t, ti, i, j, n, a;
	double r;
	scanf("%d", &t);
	FOR(ti, 1, t) {
		scanf("%d\n", &n);
		FOR0(i, n)
			gets(m[i]);
		MSET(o, 0);
		FOR0(i, n) {
			FOR0(j, n) {
				if (m[i][j] == '1')
					o[i].w++;
				if (m[i][j] != '.')
					o[i].a++;
			}
			o[i].wp = (double) o[i].w / o[i].a;
		}
		FOR0(i, n) {
			r = 0;
			a = 0;
			FOR0(j, n) {
				if (m[i][j] == '1' ) {
					r += (double) o[j].w / (o[j].a - 1);
					a++;
				} else if (m[i][j] == '0' ) {
					r += (double) (o[j].w - 1) / (o[j].a - 1);
					a++;
				}
			}
			o[i].owp = r / a;
		}
		FOR0(i, n) {
			r = 0;
			a = 0;
			FOR0(j, n) {
				if (m[i][j] != '.' ) {
					r += o[j].owp;
					a++;
				}
			}
			o[i].oowp = r / a;
		}
		printf("Case #%d:\n", ti);
		FOR0(i, n) {
			r = 0.25 * o[i].wp + 0.5 * o[i].owp + 0.25 * o[i].oowp;
			printf("%.10lf\n", r);
		}
	}
	return 0;
}
