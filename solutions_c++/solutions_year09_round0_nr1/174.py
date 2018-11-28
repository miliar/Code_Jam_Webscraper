#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>

#include <memory.h>
using namespace std;

#define FOR(i,a,n) for (int i = (a); i < (n); ++i)
#define FORE(i,a,n) for (int i = (a); i <= (n); ++i)
#define FORD(i,a,b) for (int i = (a); i >= (b); --i)
#define REP(i,n) FOR(i,0,n)
#define REPE(i,n) FORE(i,0,n)
#define LL long long
#define FIR(n) REP(i,n)
#define FJR(n) REP(j,n)
#define ALL(v) v.begin(), v.end()

#define FI FIR(n)
#define FJ FJR(n)
#define FR(i,a) FOR(i,a,n)
#define REPN(i) REP(i,n)

int L, D, cases;
string words[6000];

int m[6000][16];
int ok[6000];

int main( int argc, char* argv[] ) {
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "w", stdout);

	cin >> L >> D >> cases;
	FIR(D) cin >> words[i];

	FIR(D) FJR(L) m[i][j] = 1 << (words[i][j] - 'a');

	FORE(cas, 1, cases) {
		string s;
		cin >> s;
		FIR(D) ok[i] = 1;
		int pos = 0;
		FJR(L) {
			// parse next token
			int mask = 0;
			if (s[pos] == '(') {
				for (++pos; s[pos] != ')'; ++pos) mask |= 1 << (s[pos]-'a');
				++pos;
			} else {
				mask = 1 << (s[pos]-'a');
				++pos;
			}

			FOR(w, 0, D) if (ok[w]) ok[w] = (m[w][j] & mask) != 0;
		}

		int res = 0;
		FIR(D) if (ok[i]) ++res;
		printf("Case #%d: %d\n", cas, res);
	}
}