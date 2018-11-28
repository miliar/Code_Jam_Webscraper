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

using namespace std;

#define TASKNAME "a"
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define forn(i, n) for (int i=0; i<(int)n; i++)
#define all(a) a.begin(), a.end()

typedef long double ldb;
typedef long long lld;
typedef unsigned long long uld;
typedef vector<int> vi;
typedef complex<double> cd;

double const eps=1e-9;
ldb const epsl=1e-9;
int const inf=0x3fffffff;
int const infu=0x7fffffff;
lld const infl=0x3fffffffffffffffLL;
uld const inful=0x7fffffffffffffffLL;
template <class T>
inline T sqr(const T &a) {
	return a*a;
}


int main () {
	freopen (TASKNAME".in", "r", stdin);
	freopen (TASKNAME".out", "w", stdout);
	int n, k;
	int t;
	cin >> t;
	for (int it=1; cin >> n >> k; it++) {
		cout << "Case #" << it << ": "; 
		if (k%(1<<n) == (1<<n)-1) cout << "ON\n";
		else cout << "OFF\n";
	}
	return 0;
}