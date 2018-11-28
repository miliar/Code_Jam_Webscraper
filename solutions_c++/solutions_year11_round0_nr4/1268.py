#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

#if defined (__GNUC__) && (__GNUC__ <= 2)
#include <hash_map>
#include <hash_set>
#else
#include <ext/hash_map>
#include <ext/hash_set>
using namespace __gnu_cxx;
#endif
using namespace std;

// for loops
#define FOR(i, b, e) for (int i = (b), _e = e; i < _e; i ++)
#define REP(i, n) FOR(i, 0, (n))
#define FOR_REV(i, rb, b) for (int i = (rb), _b = (b); i >= _b; i --)

// for each
#define sz size()
template<class T> inline int size(const T &c) { return c.sz; }
#define FOR_EACH(i, c) REP(i, size(c))

// iterating stl containers
#define itype(c) __typeof((c).begin())
#define ITER(it, c) for(itype(c) it = (c).begin(); it != (c).end(); it ++)

// sort and reverse containers
#define pb push_back
#define pf push_front
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define REVERSE(c) reverse(all(c))

// vectors and string streams
typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i >> x; return x; }
template <class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

// special values
#define PI acos(-1.)
#define EPS 1e-308
#define INT_INF static_cast<int>((1LL << (sizeof(int) * 8 - 1)) - 1)

const int MAX_N = 1001;
double a[MAX_N];
double c[MAX_N][MAX_N];
double p[MAX_N];
double b[MAX_N];

double fa(int n) {
	if (a[n] > 0) { return a[n]; }
	if (n==1) { return a[1] = 0; }
	else if (n == 2) { return a[2] = 1; }
	else {
		if(a[n-1] < 0){fa(n-1);}
		if(a[n-2] < 0){fa(n-2);}
		return a[n] = (n-1) * (a[n-1]+a[n-2]);
	}
}

double fc(int n, int m) {
	if (c[n][m] > 0 || n < m) { return 0; }
	if (m == 0 || m == n || n==1){ return c[n][m] = 1; }
	else if (m == 1){ return c[n][m] = n;} 
	else{
		if (c[n-1][m] < 0){fc(n-1, m);}
		if (c[n-1][m-1] < 0){fc(n-1, m-1);}
		return c[n][m] = c[n-1][m] + c[n-1][m-1];
	}
}

double fp(int n) {
	if (p[n] > 0) { return p[n]; }
	else if (n == 0 || n == 1){return p[n] = 1;}
	else { return p[n] = fp(n-1) * n;}
}

double fb(int m) {
	if (b[m] >= 0.0) return b[m];
	if (m < 1) { return -1; }
	if (m == 1) { return b[1] = 0; }
	double tmp_b = 0;
	for (int k = 1; k <= m; k ++) {
		tmp_b += (fc(m, k) * fa(m - k) * fb(m - k)) / fp(m);
	}
	return b[m] = (tmp_b + 1) / (1 - fa(m) / fp(m));
}

int main() {
	int T, case_num = 0;
	cin >> T;
	while (T != case_num ++) {
		double ans = 0;
		int N;
		cin >> N;
		int *array = new int[N];
		bool *used = new bool[N];
		REP(i, N) {
			cin >> array[i];
			array[i] --;
			used[i] = false;
		}

		//
		for (int i=0;i<MAX_N;i++)
		{
			a[i] = p[i] = b[i] = -1;
		}
		for (int i=0;i<MAX_N;i++)
			for(int j=0;j<MAX_N;j++)
		{
			c[i][j] = -1;
		}

		REP(i, N) {
			if (!used[i]) {
				used[i] = true;
			} else {
				continue;
			}
			int group_size = 1;
			int link_index = i;
			while (array[link_index] != i) {
				link_index = array[link_index];
				used[link_index] = true;
				group_size ++;
			}
			ans += fb(group_size);
		//	cerr << fb(group_size) << "\n";
		}
		delete used;
		delete array;
		cout << "Case #" << case_num << ": " << ans << "\n";
	}
	return 0;
}
