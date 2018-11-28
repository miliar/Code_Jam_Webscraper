#include <iostream>
#include <cstdio>
#include <vector>
#include <map>

#define SIZE(c) (int) (c).size()

using namespace std;

void solve(int test) {
	int m, n;
	cin >> m;
	vector<string> a(m);
	for (int i = 0; i < m; i++)
		cin >> a[i];
	cin >> n;
	vector<string> b(n);
	for (int i = 0; i < n; i++)
		cin >> b[i];
	map<pair<char, char> , bool> f;
	for (int i = 0; i < n; i++) {
		f[make_pair(b[i][0], b[i][1])] = true;
		f[make_pair(b[i][1], b[i][0])] = true;
	}
	int l;
	string c;
	cin >> l >> c;
	string res = "";
	res += c[0];
	for (int i = 1; i < l; i++) {
		int k = 0;
		for (int j = 0; j < m; j++) {
			if (res[SIZE(res) - 1] == a[j][0] && c[i] == a[j][1]) {
				res[SIZE(res) - 1] = a[j][2];
				k = 1;
				break;
			}
			if (res[SIZE(res) - 1] == a[j][1] && c[i] == a[j][0]) {
				res[SIZE(res) - 1] = a[j][2];
				k = 1;
				break;
			}
		}
		if (k == 1)
			continue;
		for (int j = 0; j < SIZE(res); j++)
			if (f[make_pair(res[j], c[i])]) {
				res = "";
				k = 2;
				break;
			}
		if (k == 2)
			continue;
		res += c[i];
	}
	cout << "Case #" << test << ": [";
	for (int i = 0; i < SIZE(res); i++) {
		cout << res[i];
		if (i + 1 < SIZE(res))
			cout << ", ";
	}
	cout << "]" << endl;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int nTest;
	cin >> nTest;

	for (int i = 0; i < nTest; i++)
		solve(i + 1);

	return 0;
}
