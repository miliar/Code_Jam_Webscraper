#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)

typedef long long int64;
typedef pair <int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;
const string task = "";

template <class T> T sqr (T x) {return x * x;}

string s[4];

int xWin() {
	puts("X won");
	return 0;
}

int oWin() {
	puts("O won");
	return 0;
}

bool check(string s, char ch) {
	forn(i, s.size())
		if (s[i] != ch && s[i] != 'T') return 0;
	return 1;
}

int solve(){
	forn(i, 4)
		cin >> s[i];
	forn(i, 4) {
		if (check(s[i], 'X')) return xWin();
		if (check(s[i], 'O')) return oWin();
		string now = "";
		forn(j, 4)
			now += s[j][i];
		if (check(now, 'X')) return xWin();
		if (check(now, 'O')) return oWin();
	}
	{
		string now = "";
		forn(j, 4)
			now += s[j][j];
		if (check(now, 'X')) return xWin();
		if (check(now, 'O')) return oWin();
	}
	{
		string now = "";
		forn(j, 4)
			now += s[3 - j][j];
		if (check(now, 'X')) return xWin();
		if (check(now, 'O')) return oWin();
	}
	bool done = 1;
	forn(i, 4)
		forn(j, 4)
			if (s[i][j] == '.')
				done = 0;
	if (done)
		puts("Draw");
	else
		puts("Game has not completed");

}

int main ()
{
	int n;
	cin >> n;

	forn(i, n){
		printf("Case #%d: ", i + 1);
		solve();
	}

	
	return 0;
}
