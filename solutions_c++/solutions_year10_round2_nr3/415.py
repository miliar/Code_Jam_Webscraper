#include<iostream>
#include<vector>

using namespace std;

int c(int n, int k, int mod, vector<vector<int >> * binCoefs) {
	if ((*binCoefs)[n][k] != 0) {
		return (*binCoefs)[n][k];
	}
	if ((n == 0) || (k == 0) || (k == n)) {
		(*binCoefs)[n][k] = 1;
		return 1;
	}
	(*binCoefs)[n][k] = (c(n - 1, k, mod, binCoefs) + c(n - 1, k - 1, mod, binCoefs)) % mod;
	return (*binCoefs)[n][k];
}

int main() {
	int t;
	int mod = 100003;
	cin >> t;
	for (int test = 0; test < t; ++test) {
		int n;
		cin >> n;
		vector<vector<int> > results(n);
		vector<vector<int> > binCoefs(n);
		for(int i = 0; i < n; ++i) {
			results[i].resize(n);
			binCoefs[i].resize(n);
			for(int j = 0; j < n; ++j) {
				binCoefs[i][j] = 0;
			}
		}
		results[0][0] = 1;
		for (int number = 2; number <= n; ++number) {
		results[number - 1][1] = 1;
		//cout << "res " << number << " " << 1 << " " << results[number - 1][1] << endl;
			for(int len = 2; len < number; ++len) {
				results[number - 1][len] = 0;
				for (int pos = 1; pos < len; ++pos) {
					if (number - len - 1 >= len - pos - 1) {
					results[number - 1][len] = (results[number - 1][len] + 
						results[len - 1][pos] * c(number - len - 1, len - pos - 1, mod, &binCoefs)) % mod;
					}
				}
				//cout << "res " << number << " " << len << " " << results[number - 1][len] << endl;
			}
		}
		int res = 0;
		for (int i = 1; i < n; ++i) {
			res = (res + results[n - 1][i]) % mod;
		}
		cout << "Case #" << test + 1 << ": " << res << endl;
		
	}
	return 0;
}