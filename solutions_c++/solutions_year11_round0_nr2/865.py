#include <algorithm>
#include <iostream>
#include <sstream>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <vector>
#include <string>
#include <set>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstring>

#define sz(a) (int)a.size()
#define all(a) a.begin(), a.end()
#define rall(a) a.rbegin(), a.rend()
#define llong long long
#define zero(a) fabs(a) < 1e-9
#define resz(a, n) a.clear(), a.resize(n)
#define same(a, n) memset(a, n, sizeof(a))
#define make(a, b) make_pair(a, b)

using namespace std;

int main() {
	int test;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		map< pair< char, char >, char > p, q;
		int c, d;
		cin >> c;
		for (int i = 0; i < c; i++) {
			string temp;
			cin >> temp;
			p[make(temp[0], temp[1])] = p[make(temp[1], temp[0])] = temp[2];
		}
		cin >> d;
		for (int i = 0; i < d; i++) {
			string temp;
			cin >> temp;
			q[make(temp[0], temp[1])] = q[make(temp[1], temp[0])] = 1;
		}
		int n;
		string com, ans;
		cin >> n >> com;
		for (int i = 0; i < n; i++) {
			if (ans.empty())
				ans += com[i];
			else {
				if (p.find(make(com[i], ans[sz(ans) - 1])) != p.end()) {
					char t = p[make(com[i], ans[sz(ans) - 1])];
					ans.erase(ans.end() - 1);
					ans += t;
				}
				else {
					for (int j = 0; j < sz(ans); j++)
						if (q.find(make(ans[j], com[i])) != q.end()) {
							ans.clear();
							break;
						}
					if (!ans.empty())
						ans += com[i];
				}
			}
		}
		cout << "Case #" << t << ": [";
		if (ans.empty())
			cout << "]";
		else {
			for (int i = 0; i < sz(ans); i++) {
				cout << ans[i];
				if (i == sz(ans) - 1)
					cout << "]";
				else
					cout << ", ";
			}
		}
		cout << endl;
	}
	return 0;
}

