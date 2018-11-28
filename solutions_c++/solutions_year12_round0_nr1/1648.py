#pragma comment(linker, "/stack:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <algorithm>
#include <iostream>
#include <cassert>
#include <iomanip>
#include <climits>
#include <utility>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <bitset>
#include <string>
#include <queue>
#include <cmath>
#include <ctime>
#include <set>
#include <map>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define forn1(i, n) for (int i = 1; i <= int(n); i++)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define debug(x) cerr << #x << " = " << x << endl;
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(a, b) make_pair((a), (b))
#define X first
#define Y second
#define fs first
#define ft first
#define sc second

using namespace std;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;
typedef pair<ld, ld> ptd;
typedef unsigned char byte;
typedef vector<vector<int> > matrix;

const int INF = INT_MAX / 2;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

string s;

inline bool read()
{
	return (getline(cin, s));
}

inline void solve(int test)
{
	map<char, char> z;

z[ 'a' ] = 'y';
z[ 'b' ] = 'h';
z[ 'c' ] = 'e';
z[ 'd' ] = 's';
z[ 'e' ] = 'o';
z[ 'f' ] = 'c';
z[ 'g' ] = 'v';
z[ 'h' ] = 'x';
z[ 'i' ] = 'd';
z[ 'j' ] = 'u';
z[ 'k' ] = 'i';
z[ 'l' ] = 'g';
z[ 'm' ] = 'l';
z[ 'n' ] = 'b';
z[ 'o' ] = 'k';
z[ 'p' ] = 'r';
z[ 'q' ] = 'z';
z[ 'r' ] = 't';
z[ 's' ] = 'n';
z[ 't' ] = 'w';
z[ 'u' ] = 'j';
z[ 'v' ] = 'p';
z[ 'w' ] = 'f';
z[ 'x' ] = 'm';
z[ 'y' ] = 'a';
z[ 'z' ] = 'q';
z[ ' ' ] = ' ';

	printf("Case #%d: ", test + 1);

	forn(i, sz(s))
		putchar(z[ s[i] ]);

	puts("");
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int testCnt;

    assert(scanf("%d\n", &testCnt) == 1);

    forn(test, testCnt)
    {
    	assert(read());
		solve(test);
	}

    return 0;
}
