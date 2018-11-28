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
	int n, m; cin >> n >> m;
	vector<vector<char> > table(n, vector<char>(m));
	for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++)
			cin >> table[i][j];

	for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++) {
			if(table[i][j] == '#') {
				if(i < n - 1 && table[i + 1][j] == '#'
					&& j < m - 1 && table[i][j + 1] == '#'
					&& table[i + 1][j + 1] == '#') {
						table[i][j] = table[i + 1][j + 1] = '/';
						table[i + 1][j] = table[i][j + 1] = '\\';
				} else {
					cout << "Impossible" << endl;
					return;
				}
			}
		}
	
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++)
			cout << table[i][j];
		cout << endl;
	}
}

int main ( )
{
 	freopen("A-large.in", "r", stdin);
 	freopen("A-large.out", "w", stdout);

	int t; cin >> t;
	for(int i = 1; i <= t; i++) {
		cout << "Case #" << i << ":" << endl;
		solve();
	}
}