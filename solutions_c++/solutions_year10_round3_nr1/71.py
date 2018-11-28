
#include <vector>
#include <cstdio>
#include <iostream>
using namespace std;

int main() {
	int cases;
	cin >> cases;
	for (int cas = 0; cas < cases; ++cas) {
		int n;
		cin >> n;
		vector<int> a(n);
		vector<int> b(n);
		for (int i = 0; i < n; ++i)
			cin >> a[i] >> b[i];
		int res = 0;
		for (int i = 0; i < n; ++i)
			for (int j = i + 1; j < n; ++j)
				if ((a[i] < a[j]) ^ (b[i] < b[j])) {
					++res;
				}
		printf("Case #%d: %d\n", cas + 1, res);
	}
	return 0;
}