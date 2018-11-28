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
int const N=10;
int n, a[1<<N], c[1<<N], mx[1<<N];
int getmx(int k) {
	if (k+k>=1<<n) {
		int t=k+k-(1<<n);
		return max(c[t],c[t+1]);
	}
	return max(getmx(k+k), getmx(k+k+1));
}
int go(int k) {
	if (k+k>=1<<n) {
		int t=k+k-(1<<n);
		c[t]++;
		c[t+1]++;
		return mx[k]=a[k];
	}
	return mx[k]=max(go(k+k)+go(k+k+1), a[k]);
}
void rep(int k) {
	if (mx[k]==a[k]) {
		a[k]=0;
		return;
	}
	rep(k+k);
	rep(k+k+1);
}


int main () {
	freopen (TASKNAME".in", "r", stdin);
	freopen (TASKNAME".out", "w", stdout);
	int nt;
	cin >> nt;
	for (int it=1; it<=nt; it++) {
		int res=0;
		cin >> n;
		for (int i=0; i<1<<n; i++) {
			cin >> c[i];
			c[i]=n-c[i];
		}
		for (int k=1<<n-1; k>=1; k>>=1)
			for (int i=k; i<k+k; i++) {
				cin >> a[i];
				res+=a[i];
			}
		for (int i=1; i<(1<<n); i++) 
			for(;;) {
				int m=getmx(i);
				if (m<n) {
					res-=go(i);
					rep(i);
				}
				else break;
			}
		cout << "Case #" << it << ": " << res << endl; 
	}
	return 0;
}