#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <vector>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <map>

#define y0 y63475625
#define y1 y28435
#define sqr(x) ((x)*(x))
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define re return

#ifdef ONLINE_JUDGE
#pragma comment(linker, "/STACK:16777216")
#endif

using namespace std;

typedef vector <int> vi;
typedef vector <vi> vvi;
typedef long long ll;
typedef long double ld;
typedef pair <int, int> ii;
typedef vector <ii> vii;

template <class T> T abs(T & a) {
	return a > 0 ? a : -a;
}

template <class T> int sgn(T & a) {
	return a > 0 ? 1 : (a < 0 ? -1 : 0);
}

#ifdef ONLINE_JUDGE
const double M_PI = 2.0 * acos(1.0);
#endif

int main()
{
	int T;
	cin >> T;
	for (int I = 0; I < T; I++) {
		int a[1000], n, x = 0, s = 0;
		cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> a[i];
			x ^= a[i];
			s += a[i];
		}
		cout << "Case #" << I + 1 << ": ";
		if (x == 0) {
			sort(a, a + n);
			cout << s - a[0] << endl;
		} else cout << "NO" << endl;
	}
	return 0;
}
