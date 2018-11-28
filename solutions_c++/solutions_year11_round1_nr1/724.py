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

string solve() {
	ll n, tod, all; cin >> n >> tod >> all;
	
	if((all == 0 && tod > 0) || (all == 100 && tod < 100))
		return "Broken";
	
	vector<ll> r; r.reserve(600);
	ll d = 1;
	while(d <= n) {
		ll k = d;
		while(k <= n) {
			r.push_back(k);
			k *= 2;
		}
		d *= 5;
	}
	
	sort(r.begin(), r.end());
	
	int m = r.size();
	for(int i = 0; i < m; i++)
		for(int j = i; j < m; j++) {
			ll tod_s = r[i];
			
			if((tod * tod_s) % 100 == 0) {
				return "Possible";
			}
		}
	
	return "Broken";
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