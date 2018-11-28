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

void solve() {
	int n, l, h; cin >> n >> l >> h;
	vector<int> notes(n);
	for(int i = 0; i < n; i++)
		cin >> notes[i];
	
	for(int i = l; i <= h; i++) {
		bool ok = true;
		for(int j = 0; j < n; j++)
			if(notes[j] % i && i % notes[j]) {
				ok = false;
				break;
			}
		if(ok) {
			cout << i << endl;
			return;
		}
	}
	
	cout << "NO" << endl;
}

int main ( )
{
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);

	int t; cin >> t;
	for(int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
}