#include <fstream>
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

ifstream fin("input");
ofstream fout("output");

void solve() {
	int n;
	fin >> n;
	vector<int> a(n);
	for (int i = 0; i < n; i++) {
		fin >> a[i];
	}
	int res_xor = 0;
	for (int i = 0; i < n; i++) {
		res_xor ^= a[i];
	}
	if (res_xor != 0) {
		fout << "NO" << endl;
		return;
	}
	fout << accumulate(a.begin(), a.end(), 0) - *min_element(a.begin(), a.end()) << endl;
}

int main() {
	int t;
	fin >> t;
	for (int i = 0; i < t; i++) {
		fout << "Case #" << i + 1 << ": ";
		solve();
	}
	return 0;
}
