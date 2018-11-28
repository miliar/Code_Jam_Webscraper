#include <iostream>
#include <vector>

using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int l, d, n;
	scanf("%d%d%d", &l, &d, &n);
	char pat[10000];
	cin.getline(pat, 10000);
	vector<string> w;
	for (int i = 0; i < d; ++i) {
		cin.getline(pat, 10000);
		w.push_back(pat);
	}
	bool a[20][30];
	for (int test = 0; test < n; ++test) {
		cin.getline(pat, 10000);
		int len = strlen(pat);
		memset(a, 0, sizeof(a));
		bool f = false;
		int k = 0;
		for (int i = 0; i < len; ++i) {
			if (pat[i] == '(') {
				if (i != 0)
					k++;
				f = true;
			} else if (pat[i] == ')') {
				f = false;
			} else {
				if (!f && i != 0)
					k++;
				a[k][pat[i]] = true;
			}
		}
		int ans = 0;
		for (int i = 0; i < w.size(); ++i) {
			int j;
			for (j = 0; j < w[i].length(); ++j) {
				if (!a[j][w[i][j]])
					break;
			}
			if (j == w[i].length())
				++ans;
		}
		printf("Case #%d: %d\n", test + 1, ans);
	}

	return 0;
}

