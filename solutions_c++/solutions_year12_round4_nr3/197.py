#include <iostream>
#include <cstdio>
#include <set>
#include <stack>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <cmath>
#include <memory.h>
#include <algorithm>
#include <cstdlib>
#include <cassert>
#include <sstream>
#include <fstream>
using namespace std;


#define pb push_back
#define mp make_pair

typedef long long li;
typedef vector<li> vi;
typedef pair<int, int> pi;
void solve();

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	ios_base::sync_with_stdio(false);
	int t;
	cin >> t;
	string s;
	getline(cin, s);
	cout << fixed;
	cout.precision(30);
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
		cout << '\n';
	}
	return 0;
}

void solve() {
	int n;
	cin >> n;
	int r[5111];
	int t[5111];
	//	int first[5111];
	long long delta[5111];
	for (int i = 0; i < n - 1; ++i) {
		cin >> r[i];
	}

	stack<int> s;
	for (int i = 0; i < n - 1; ++i) {
		if (!s.empty() && s.top() == i + 1)
			s.pop();
		if (!s.empty() && r[i] > s.top()) {
			cout << "Impossible";
			return;
		}
		if (s.empty() || r[i] < s.top())
			s.push(r[i]);

	}
	t[n] = 1000000000;
	/*	for(int z=n-1;z>0;--z){
			//t[z] = t[r[z-1]] - 1;
			first[z] = z;
			first[r[z-1]] = z;
		}
	 * 
	 */
	delta[n] = 1;
	for (int z = n - 1; z > 0; --z) {
		if (r[z - 1] == n) {
			delta[z] = 1;
		} else {
			int next = r[z - 1];
			int nextnext = r[next - 1];
			delta[z] = (delta[next] * (next - z) + (nextnext - next) ) / (nextnext - next);
		}
		t[z] = t[r[z - 1]] - delta[z];
	}


	bool bad = false;
	while (true) {
		bool ok = true;
		for (int i = 1; i < n; ++i) {
			int best = i + 1;
			for (int j = i + 2; j <= n; ++j) {
				if ((t[j] - t[i]) *(long long) (best - i) > (j - i) * (long long) (t[best] - t[i]))
					best = j;
			}
			if (best != r[i - 1]) {
				ok = false;
				if (!bad) {
					cerr << "bad" << endl;
					bad = true;
				}
				if(best > r[i-1])
					delta[i]++;
				else
					delta[best]++;
				for (int z = n - 1; z > 0; --z) {
					t[z] = t[r[z - 1]] - delta[z];
				}
			}
			
		}
		if (!ok)
			continue;
		cerr << "ans" << endl;
		for (int z = 1; z <= n; ++z) {
			cout << t[z] << ' ';
		}
		return;


	}
}
