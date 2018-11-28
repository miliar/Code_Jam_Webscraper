/*
TASK: 
ID: marijon1
LANG: C++
*/

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cerrno>
#include <cfloat>
#include <ciso646>
#include <climits>
#include <clocale>
#include <cmath>
#include <complex>
#include <csetjmp>
#include <csignal>
#include <cstdarg>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>
#define mp make_pair
#define st first
#define nd second
#define FOR(i,n) for(int i=0;i<(n);i++)
#define FORO(i,n) for(int i=1;i<=(n);i++)
#define FORS(i,a,n) for(int i=(a);i<(n);i++)
#define FORB(i,a,n) for(int i=(a);i>=(n);i--)
#define foreach(v, i) for (typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)
#define INRANGE(a,b,c,d) ((a)>=0&&(b)>=0&&(a)<(c)&&(b)<(d))
#define sz(v) ((int)(v).size())
#define pf printf

using namespace std;
typedef long long ll;

int n, m;
char Color[512][512];

int maxd[512][512];
bool used[512][512];
int num_by_edge[600];

void recalc() {
	FOR(r, m) {
		FOR(c, n) {
			if (used[r][c])
				maxd[r][c] = 0;
			else if (r == 0 || c == 0)
				maxd[r][c] = 1;
			else {
				if (!used[r-1][c] && !used[r-1][c-1] && !used[r][c-1]
					&& Color[r][c] == Color[r-1][c-1] && Color[r][c-1] == Color[r-1][c] && Color[r][c] != Color[r-1][c])
					maxd[r][c] = min(min(maxd[r-1][c-1], maxd[r-1][c]), maxd[r][c-1]) + 1;
				else
					maxd[r][c] = 1;
			}
		}
	}
}

void go() {
	cin >> m >> n;
	FOR(i, m) {
		FOR(j, n/4) {
			char ch;
			scanf(" %c", &ch);
			int q;
			if (ch >= '0' && ch <= '9')
				q = ch - '0';
			else
				q = ch - 'A' + 10;
			Color[i][4*j] = (q & 8) > 0;
			Color[i][4*j+1] = (q & 4) > 0;
			Color[i][4*j+2] = (q & 2) > 0;
			Color[i][4*j+3] = (q & 1) > 0;
		}
	}
	fill(used[0], used[512], false);
	fill(num_by_edge, num_by_edge + 600, 0);
	while (true) {
		recalc();
		int mbr = 0, mbc = 0, edg = 0;
		FOR(i, m) FOR(j, n) {
			if (maxd[i][j] > edg) {
				mbr = i;
				mbc = j;
				edg = maxd[i][j];
				break;
			}
		}
		if (edg <= 1) break;
		num_by_edge[edg]++;
		for (int r = mbr-edg+1; r <= mbr; r++)
			for (int c = mbc-edg+1; c <= mbc; c++)
				used[r][c] = true;
	}
	FOR(r, m) FOR(c, n)
		if (maxd[r][c] == 1)
			num_by_edge[1]++;
	int k = 0;
	FOR(i, 600)
		if (num_by_edge[i] > 0)
			k++;
	pf("%d\n", k);
	FORB(i, 599, 0)
		if (num_by_edge[i] > 0)
			pf("%d %d\n", i, num_by_edge[i]);
}

int main() {
	//freopen("xxxxx.in", "r", stdin);
	//freopen("xxxxx.out", "w", stdout);
	int t;
	cin >> t;
	FOR(i, t) {
		pf("Case #%d: ", i+1);
		go();
	}
	return 0;
}
