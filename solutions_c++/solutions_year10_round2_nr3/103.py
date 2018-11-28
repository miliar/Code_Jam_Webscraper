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


int const mod=100003, N=505;
int c[N][N];
lld r[N][N], rs[N];


int main () {
	freopen("in.txt", "r", stdin);
	freopen ("out.txt", "w", stdout);

	int nt;
	cin >> nt;
	for (int i=0; i<N; i++)
		c[i][0]=c[0][i]=1;
	for (int i=1; i<N; i++)
		for (int j=1; j<N; j++)
			c[i][j]=(c[i-1][j]+c[i][j-1])%mod;
	for (int n=2; n<N; n++) {
		rs[n]=r[n][1]=1;
		for (int k=2; k<n; k++) {
			for (int m=k-1; m>=1 && n-k-k+m>=0; m--)
				r[n][k]+=(lld)r[k][m]*c[k-m-1][n-k-k+m];
			rs[n]+=r[n][k]%=mod;
		}
		rs[n]%=mod;
	}
	for (int it=1; it<=nt; it++) {
		int n; cin >> n;
		cout << "Case #" << it << ": " << rs[n] << endl;
	}

	return 0;
}