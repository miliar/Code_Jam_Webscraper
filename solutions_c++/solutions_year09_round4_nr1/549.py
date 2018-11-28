#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

const int MAXN = 110;

int n;
string matrix[MAXN];

int last_one(string& s) {
	for (int i = s.size() - 1; i >= 0; --i) {
		if (s[i] == '1') {
			return i;
		}
	}
	return -1;
}

int main() {
	int n_tests;

	scanf("%d", &n_tests);
	for (int test = 1; test <= n_tests; ++test) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			cin >> matrix[i];
		}

		int res = 0;
		for (int i = 0; i < n; ++i) {
			if (last_one(matrix[i])>i) {
				for (int j = i + 1; j < n; ++j) {
					if (last_one(matrix[j])<=i) {
						for (int k = j; k > i; --k) {
							++res;
							swap(matrix[k], matrix[k-1]);
						}
						break;
					}
				}
			}
		}

		printf("Case #%d: %d\n", test, res);
	}

	return 0;
}
