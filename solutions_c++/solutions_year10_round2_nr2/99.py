#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <functional>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <ctime>
#include <cassert>
#include <queue>
#include <stack>
#include <cstdarg>
#include <list>
#include <deque>
#include <stack>
#include <bitset>
#include <numeric>
#include <utility>
#include <cmath>
using namespace std;

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define forn(i, n) for (int i=0; i<int(n); i++)
#define all(a) a.begin(), a.end()

typedef long double ldb;
typedef long long lld;
typedef vector<int> vi;
typedef complex<double> cd;

double const eps=1e-9;
ldb const epsl=1e-9;
int const inf=0x3fffffff;
lld const infl=0x3fffffffffffffffLL;
template <class T>
inline T sqr(const T &a) {
	return a*a;
}


int main () {
	freopen("in.txt", "r", stdin);
	freopen ("out.txt", "w", stdout);

	int nt;
	cin >> nt;
	for (int it=1; it<=nt; it++) {
		int n, k, t, b;
		cin >> n >> k >> b >> t;
		vector<int> x(n), v(n);
		for (int i=0; i<n; i++)
			cin >> x[i];
		for (int i=0; i<n; i++)
			cin >> v[i];
		reverse(all(x));
		reverse(all(v));
		int num=0, res=0, br=0;
		for (int i=0; num<k && i<n; i++) {
			if (x[i]+v[i]*t>=b)
				num++, res+=br;
			else br++;
		}

		cout << "Case #" << it << ": ";
		(num==k ? cout << res : cout << "IMPOSSIBLE");
		cout << endl;
	}

	return 0;
}