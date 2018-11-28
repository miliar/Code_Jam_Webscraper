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
	int n; cin >> n;
	vector<vector<char> > t(n, vector<char>(n));
	for(int i = 0; i < n; i++)
		for(int j = 0; j < n; j++)
			cin >> t[i][j];
	
	vector<double> wp(n, 0), owp(n, 0), oowp(n, 0);
	
	vector<int> tot(n, 0);
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < n; j++)
			if(i != j && t[i][j] != '.') {
				tot[i]++;
				if(t[i][j] == '1')
					wp[i]++;
			}
	}
	
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < n; j++)
			if(j != i && t[i][j] != '.')
				owp[i] += (wp[j] - (t[j][i] == '1')) / (tot[j] - (t[j][i] != '.'));
		owp[i] /= tot[i];
	}
		
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < n; j++)
			if(i != j && t[i][j] != '.')
				oowp[i] += owp[j];
		oowp[i] /= tot[i];
	}
	
	for(int i = 0; i < n; i++)
		wp[i] /= tot[i];
	
	cout << fixed;
	for(int i = 0; i < n; i++) {
		cout << setprecision(8) << 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
		if(i != n - 1) cout << endl;
	}
}

int main ( )
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int t; cin >> t;
	for(int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": " << endl;
		solve();
		cout << endl;
	}
}