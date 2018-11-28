#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <string>
#include <map>
using namespace std;

ifstream fin("C-small-attempt0.in");
ofstream fout("out.txt");

int dp[501][501], choose[501][501];

int wchoose(int n, int k) {
	if (n < k || k < 0) return 0;
	if (choose[n][k] >= 0) return choose[n][k];
	return choose[n][k] = (wchoose(n - 1, k - 1) + wchoose(n - 1, k)) % 100003;
}

int work(int n, int d) {
	if (n < d + 1) return 0;
	if (dp[n][d] >= 0) return dp[n][d];
	dp[n][d] = 0;
	for (int x = d + 1 + d; x <= n; ++x) {
		dp[n][d] += wchoose(x - 2 - d, d - 1) * work(n - d, x - d - 1);
		dp[n][d] %= 100003;
	}
	return dp[n][d];
}

int main() {
	int t, n;
	for (int i = 0; i < 501; ++i)
		for (int j = 0; j < 501; ++j) {
			dp[i][j] = -1;
			choose[i][j] = -1;
		}
	for (int i = 0; i < 500; ++i) {
		choose[i][i] = choose[i][0] = 1;
		dp[i + 1][i] = 1;
	}
	fin >> t;
	for (int i = 1; i <= t; ++i) {
		fout << "Case #" << i << ": ";
		fin >> n;
		int s = 0;
		for (int d = 1; d < n; ++d) {
			s += work(n, d);
			s %= 100003;
		}
		fout << s << endl;
	}
	return 0;
}
