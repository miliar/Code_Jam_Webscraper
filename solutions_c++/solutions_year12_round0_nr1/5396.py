#include <ctime>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>

#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <functional>
#include <map>
#include <set>
#include <fstream>
#include <queue>
#include <bitset>
#include <numeric>
#include <iterator>
#include <complex>


using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); ++i)
#define repd(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define forn(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)
#define fornd(i, a, b) for (int i = (int)(b); i >= (int)(a); --i)
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define fill(a, x) memset(a, x, sizeof(a))
#define pb push_back
#define mp make_pair
#define log(a, x) cout << a << " : " << x << endl;

typedef unsigned int uint;
typedef double dbl;
typedef long long ll;
typedef unsigned long long ull;
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <string> vs;
typedef pair <int, int> pii;
typedef pair <dbl, dbl> pdd;
typedef unsigned char byte;
typedef complex<double> base;

template <class T> T inline sqr(T x) { return x * x; }
template <class T> inline T myAbs( T a ) { return a > 0 ? a : -a; }

#ifndef ONLINE_JUDGE
#include "prettyprint.cpp"
#endif

int trans[26] = {24, 7, 4, 18, 14, 2, 21, 23, 3, 20, 8, 6, 11, 1, 10, 17, 25, 19, 13, 22, 9, 15, 5, 12, 0, 16};

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
//	int a[30];
//	fill(a,-1);
//	string s1,s2;
//	
//	rep(t,3) {
//		getline(cin, s1);
//		getline(cin, s2);
//		rep(i,sz(s1)) {
//			if (isalpha(s1[i]))
//				a[s1[i]-'a'] = s2[i]-'a';
//		}
//	}
//	a[25] = 'q'-'a';
//	a['q'-'a'] = 'z' - 'a';
//	rep(i,30) {
//		cout << a[i] << ", ";
//		if (a[i] == -1)
//			cout << "(" << char(i+'a') << ") ";
//	}
//	
//	bool use[30];
//	zero(use);
//	rep(i,26) {
//		use[a[i]] = true;
//	}
//	cout << endl;
//	rep(i,26) {
//		if (!use[i]) {
//			cout << char(i+'a') << endl;
//		}
//	}
	int T = 0;
	string s;
	cin >> T;
	scanf("\n");
	rep(test, T) {
		getline(cin, s); 
		rep(i,sz(s)) {
			if (isalpha(s[i])) {
				s[i] = trans[s[i]-'a']+'a';
			}
		}
		cout << "Case #" << test+1 << ": " << s << endl;
	}
	
    return 0;
}
