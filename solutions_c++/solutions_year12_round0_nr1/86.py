#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>
#include <iostream>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <cctype>
#include <sstream>
#include <cassert>
#include <bitset>
#include <memory.h>
#include <complex>

using namespace std;

#pragma comment(linker, "/STACK:200000000")

typedef long long int64;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define fore(i, a, n) for(int i = (int)(a); i < (int)(n); i++)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) (int(a.size()) - 1)
#define all(a) a.begin(), a.end()

const double EPS = 1E-9;
const int INF = 1000000000;
const int64 INF64 = (int64) 1E18;
const double PI = 3.1415926535897932384626433832795;

const string cons[10] = {
"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv",
"y qee",
"z",
"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up",
"a zoo",
"q"
};

map<char, char> ma;

int main() {
#ifdef RADs_project
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
	
	forn(tt, 5) {
		string s1 = cons[tt];
		string s2 = cons[tt + 5];

		forn(i, s1.size())
			if (s1[i] != ' ')
				ma[s1[i]] = s2[i];
	}
/*
	cout << (int)ma.size() << endl;

	for (map<char, char>::iterator i = ma.begin(); i != ma.end(); i++)
		cout << i->fs << ' ' << i->sc << endl;
*/

	int tt;
	scanf("%d\n", &tt);
	forn(i, tt) {
		string s;
		getline(cin, s);

		forn(j, s.size())
			if (s[j] != ' ')
				s[j] = ma[s[j]];

		printf("Case #%d: %s\n", i + 1, s.c_str());
	}

	return 0;
}