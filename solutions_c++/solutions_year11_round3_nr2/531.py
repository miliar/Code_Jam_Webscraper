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
	int l, n, c; ll t; cin >> l >> t >> n >> c;
	
	vector<int> len(c);
	for(int i = 0; i < c; i++) {
		cin >> len[i];
		len[i] *= 2;
	}

	vector<ll> dist(n);
	for(int i = 0; i < n; i++)
		dist[i] = len[i % c] + (i ? dist[i - 1] : 0);

	ll minTime = dist[n - 1];
	if(l > 0)
		for(int i = 0; i < n; i++)
			if(t < (i ? dist[i - 1] : 0) + len[i % c]) {
				ll timeStep = max(0ll, t - (i ? dist[i - 1] : 0));
				ll win = (len[i % c] - timeStep) / 2;
				minTime = min(minTime, dist[n - 1] - win);
				if(l > 1)
					for(int j = i + 1; j < n; j++) {
						ll newDist = dist[j - 1] - timeStep + len[j % c];
						ll newTimeStep = max(0ll, t - newDist);
						ll newWin = max(0ll, (len[j % c] - newTimeStep) / 2);
						
						minTime = min(minTime, dist[n - 1] - win - newWin);
					}
			}
	cout << minTime << endl;
}

int main ( )
{
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);

	int t; cin >> t;
	for(int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
}