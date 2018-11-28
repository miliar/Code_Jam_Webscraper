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
	int n, t[2] = {0}, a = 0, p[2]; cin >> n;
	p[0] = p[1] = 1;

	for(int i = 0; i < n; i++) {
		char r; int q; cin >> r >> q;
		int b = r == 'O' ? 0 : 1;

		t[b] += abs(p[b] - q) + 1;
		if(t[b] <= t[!b])
			t[b] = t[!b] + 1;
		p[b] = q;

		a = b;
	}
	
	return t[a];
}

int main ( )
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int T; cin >> T;
	for(int test = 1; test <= T; test++) {
		cout << "Case #" << test << ": " << solve() << endl;
	}
}