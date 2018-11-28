#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <memory.h>
#include <sstream>
#include <ctime>

#define oo 1000000005
#define eps 1e-11

#define REP(i,n) for(int i = 0, _n = (n); i < _n; i++)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define FORD(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define FOREACH(it,c) for (__typeof ((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define RESET(c,x) memset (c, x, sizeof (c))

#define sqr(x) ((x) * (x))
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define ALL(c) (c).begin(), (c).end()
#define SIZE(c) (c).size()

using namespace std;

const double PI = 2.0 * acos (0.0);

typedef long long LL;
typedef pair <int, int> PII;

inline int getInt () { int x; scanf ("%d", &x); return x; }
inline LL getLL () { LL x; scanf ("%lld", &x); return x; };
inline int NUM (char c) { return (int)c - 48; }
inline char CHR (int n) { return (char)(n + 48); }
template <class T> inline T MAX (T a, T b) { if (a > b) return a; return b; }
template <class T> inline T MIN (T a, T b) { if (a < b) return a; return b; }
template <class T> inline T ABS (T a) { if (a < 0) return -a; return a; }

inline void OPEN (string s) {
    freopen ((s + ".in").c_str (), "r", stdin);
    freopen ((s + ".out").c_str (), "w", stdout);
}

// ptrrsn_1's template

char a[] = "ejp mysljylc kd kxveddknmc re jsicpdrysiqz";
char b[] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
char c[] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

char at[] = "our language is impossible to understandzq";
char bt[] = "there are twenty six factorial possibilities";
char ct[] = "so it is okay if you want to just give up";

char what[255];

string s;

int main () {
	OPEN("A");
	vector <char> v;
	for (char j = 'a'; j <= 'z'; j++) {
		char ans = -1;
		for (int i = 0; a[i]; i++) {
			if (a[i] == j) {
				ans = at[i];
				break;
			}
		}
		for (int i = 0; b[i]; i++) {
			if (b[i] == j) {
				ans = bt[i];
				break;
			}
		}
		for (int i = 0; c[i]; i++) {
			if (c[i] == j) {
				ans = ct[i];
				break;
			}
		}
		if (ans != -1) {
			what[j] = ans;
		}
	}
	
	int nTC;
	scanf("%d", &nTC);
	getline(cin, s);
	FOR (tc, 1, nTC) {
		printf("Case #%d: ", tc);
		getline(cin, s);
		REP (i, SIZE(s)) {
			if (s[i] == ' ') cout << ' ';
			else cout << what[s[i]];
		}
		cout << endl;
	}
	
		
    return 0;
}
