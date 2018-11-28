#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

#define MAX 500000

short dp[11][MAX];
bool vis[11][MAX];
short mask[10*MAX];

short solve(int b, int a) {
	if (a < MAX) {
		short r = dp[b][a];
		if (r >= 0) return r;
		if (vis[b][a]) return dp[b][a] = 0;
		vis[b][a] = 1;
	}
	short t = 0;
	int oa = a;
	while (a) {
		t += (a%b)*(a%b);
		a /= b;
	}
	if (t == oa) {
		if (oa < MAX) {
			return dp[b][oa] = 0;
		}
		return 0;
	}
	if (oa < MAX) return dp[b][oa] = solve(b, t);
	else return solve(b, t);
}

int main () {
	int i, j;
	for (i=2; i<=10; i++) {
		dp[i][1] = 1;
		dp[i][0] = 0;
		for (j=2; j<MAX; j++) dp[i][j] = -1;
		for (j=2; j<MAX; j++) solve(i, j);
	}
	int T;
	cin >> T;
	string str;
	int cse = 0;
	getline(cin, str);
	for (i=2; i<10*MAX; i++) {
		mask[i] = 0;
		for (j=2; j<=10; j++) {
			if (solve(j, i)) {
				mask[i] += 1<<j;
			}
		}
	}
	while (T--) {
		getline(cin, str);
		stringstream ss(str);
		vector<int> v;
		while (ss >> i) {
			v.push_back(i);
		}
		int ans = -1;
		int mk = 0;
		for (i=0; i<v.size(); i++) {
			mk += 1 << v[i];
		}
		for (i=2; i<30*MAX; i++) {
			bool fnd = 1;
			if (i >= 10*MAX) {
				for (j=0; j<v.size(); j++) {
					if (!solve(v[j], i)) {
						fnd = 0;
						break;
					}
				}
				if (fnd) {
					ans = i;
					break;
				}
			}
			else {
				if ((mask[i]&mk) == mk) {
					ans = i;
					break;
				}
			}
		}
		cout << "Case #" << ++cse << ": " << ans << endl;
		cerr << cse << endl;
	}
	return 0;
}
