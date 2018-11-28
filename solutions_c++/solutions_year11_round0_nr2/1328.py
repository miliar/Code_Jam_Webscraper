#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cassert>
#include <memory.h>
#include <ctype.h>

#include <iostream>

#include <string>
#include <complex>
#include <numeric>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <sstream>

//#pragma comment(linker, "/stack:64000000")

using namespace std;

template<typename TYPE> inline TYPE sqr(const TYPE& a) { return (a) * (a); }

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = 1000 * 1000 * 1000;
const ld EPS = 1e-9;
const ld PI = 2 * acos(0.0);
const int N = 110;

const char OFF = 'A';

int c, d, n;
int comb[N][N];
bool opp[N][N];
string seq;
char str[N];

int conv(char a) {
	return a - OFF;
}

void read() {
	memset(comb, -1, sizeof comb);
	memset(opp, 0, sizeof opp);

	scanf("%d", &c);
	forn(i, c) {
		scanf(" %s", str);
		int x = conv(str[0]);
		int y = conv(str[1]);
		int to = conv(str[2]);
		comb[x][y] = to;
		comb[y][x] = to;
	}
	scanf("%d", &d);
	forn(i, d) {
		scanf(" %s", str);
		int x = conv(str[0]);
		int y = conv(str[1]);
		opp[x][y] = opp[y][x] = true;
	}
	scanf("%d", &n);
	scanf(" %s\n", str);
	seq = string(str);
	assert(n == seq.size());
}

int z[N];
void solve(int test) {
	read();

	int top = 0;
	forn(i, n) {
		int cur = conv(seq[i]);
		z[top] = cur;
		++top;
		while(top >= 2 && comb[z[top - 1]][z[top - 2]] != -1) {
			z[top - 2] = comb[z[top - 1]][z[top - 2]];
			--top;
		}
		int last = z[top - 1];
		forn(j, top - 1) {
			if(opp[last][z[j]]) {
				top = 0;
				break;
			}
		}
	}

	printf("Case #%d: [", test);
	if(top > 0) {
		printf("%c", (char)(z[0] + OFF));
		for1(i, top - 1)
			printf(", %c", (char)(z[i] + OFF));
	}
	printf("]\n");
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tests;
	scanf("%d\n", &tests);

	for1(it, tests) {
		solve(it);		
	}
	

	return 0;
}
