#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <cstring>
#include <string>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <limits>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;

const double pi = acos(-1.0);
const int inf = numeric_limits<int>::max();

#define DEBUG1D(a, x1, x2) { cout << #a << ":"; for(int _i = (x1); _i < (x2); _i++){ cout << " " << a[_i]; } cout << endl; }
#define DEBUG2D(a, x1, x2, y1, y2) { cout << #a << ":" << endl; for(int _i = (x1); _i < (x2); _i++){ for(int _j = (y1); _j < (y2); _j++){ cout << (_j > y1 ? " " : "") << a[_i][_j]; } cout << endl; } }

int solve() {
	int n, m = inf, s = 0, x = 0; cin >> n;
	
	for(int i = 0; i < n; i++) {
		int c; cin >> c;
		m = min(m, c);
		s += c;
		x ^= c;
	}
	
	if(!x) return s - m;
	else return 0;
}

int main ( )
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	
	int T; cin >> T;
	for(int test = 1; test <= T; test++) {
		int s = solve();
		cout << "Case #" << test << ": ";
		if(s) cout << s << endl;
		else cout << "NO" << endl;
	}
}