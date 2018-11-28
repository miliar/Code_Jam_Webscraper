#pragma comment(linker, "/STACK:16777216")

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <functional>
#include <numeric>

using namespace std;

template<class T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }

typedef long long ll;

#define eps 1e-10
#define inf 0x3f3f3f3f
#define INF 0x3f3f3f3f3f3f3f3fLL

#define fr(x,y,z) for(int(x)=(y);(x)<(z);(x)++)
#define cast(x,t) *({stringstream ss;static t __ret;ss<<x,ss>>__ret;&__ret;})
#define rep(x,n) for(int x = 0; x < (n); x++)

#define dbg(x) cout << #x << " == " << x << endl
#define print(x) cout << x << endl

// var
const int maxn = 100 + 10;
char tab[maxn][maxn];
int n;

int read() {
	scanf("%d",&n);
	rep(i,n) scanf("%s",tab[i]);
	return 1;
}

double wp[maxn], owp[maxn], oowp[maxn];

void _wp(int x) {
	int total = 0, ct = 0;
	rep(i,n) if(tab[x][i] != '.') {
		total++;
		if(tab[x][i] == '1') ct++;
	}
	wp[x] = total ? double(ct) / total : 0;
}

void _owp(int x) {
	double total = 0; int ct = 0;
	rep(i,n) if(tab[x][i] != '.') {
		int _total = 0, _ct = 0;
		rep(j,n) if(tab[i][j] != '.' && j != x) {
			_total++;
			if(tab[i][j] == '1') _ct++;
		}
		double temp = _total ? double(_ct) / _total : 0;
		total += temp, ct++;
	}
	owp[x] = ct ? total / ct : 0;
}

void _oowp(int x) {
	int total = 0; double ct = 0;
	rep(i,n) if(tab[x][i] != '.') {
		total++;
		ct += owp[i];
	}
	oowp[x] = total ? double(ct) / total : 0;
}

void process() {
	rep(i,n) _wp(i);
	rep(i,n) _owp(i);
	rep(i,n) _oowp(i);
	static int caso = 1;
	printf("Case #%d:\n",caso++);
	rep(i,n) {
		printf("%.7lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
	}
}


int main() {
	// solve
	int t; cin >> t;
	while(t-- && read()) {
		process();
	}
	return 0;
}

