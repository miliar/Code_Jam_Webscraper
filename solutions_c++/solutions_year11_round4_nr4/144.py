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

#define MAX 400

int v[MAX];
int th[MAX];
char e[MAX][MAX];
int q[MAX * MAX];

int n;

int bfs(int n1, int n2)
{
	int pq, i, j, nq;
	MSET(v, -1);
	v[n1] = 0;
	nq = 0;
	q[nq++] = n1;
	FORL(pq, 0, nq) {
		i = q[pq];
		FOR0(j, n) {
			if (e[i][j] && v[j] < 0) {
				v[j] = v[i] + 1;
				if (j == n2)
					return v[j] - 1;
				q[nq++] = j;
			}
		}
	}
	return 0;
}

int dfs(int i, int n2, int threat)
{
	int j;
	FOR0(j, n) {
		if (e[i][j]) {
			if (!th[j])
				threat++;
			th[j]++;
		}
	}
	int m = 0;
	FOR0(j, n) {
		if (e[i][j]) {
			if (v[j] == v[i] + 1) {
				if (j == n2) {
					m = threat;
					break;
				} else {
					int d = dfs(j, n2, threat);
					MAXA(m, d);
				} 
			}
		}
	}
	FOR0(j, n)
		if (e[i][j])
			th[j]--;
	return m;
}


int main()
{
	int t, ti, i, w, u1, u2, m;
	scanf("%d", &t);
	FOR(ti, 1, t) {
		scanf("%d %d\n", &n, &w);
		MSET(e, 0);
		FOR0(i, w) {
			scanf("%d,%d", &u1, &u2);
			e[u1][u2] = 1;
			e[u2][u1] = 1;
		}
		m = bfs(0, 1);
		MSET(th, 0);
		w = dfs(0, 1, 0) - m;
		if (m != 0)
			w--;
		printf("Case #%d: %d %d\n", ti, m, w);
	}
	return 0;
}
