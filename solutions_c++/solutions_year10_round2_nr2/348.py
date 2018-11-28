#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <string>
#include <map>
using namespace std;

ifstream fin("B-large.in");
ofstream fout("out.txt");

int main() {
	int c, t, b, n, k, x[50], v[50], dp[51][51];
	fin >> c;
	for (int i = 1; i <= c; ++i) {
		fout << "Case #" << i << ": ";
		fin >> n >> k >> b >> t;
		for (int j = 0; j < n; ++j) fin >> x[j];
		for (int j = 0; j < n; ++j) fin >> v[j];
		for (int j = 0; j <= n; ++j)
			for (int l = 0; l <= k; ++l) dp[j][l] = -1;
		dp[0][0] = 0;
		for (int j = 0; j < n; ++j) {
			for (int l = 0; l <= k; ++l)
				if (dp[j][l] >= 0) dp[j + 1][l] = dp[j][l] + k - l;
			if (x[n - 1 - j] + v[n - 1 - j] * t < b) continue;
			for (int l = 0; l < k; ++l)
				if (dp[j][l] >= 0 && (dp[j + 1][l + 1] < 0 || dp[j + 1][l + 1] > dp[j][l]))
					dp[j + 1][l + 1] = dp[j][l];
		}
		if (dp[n][k] < 0) fout << "IMPOSSIBLE" << endl;
		else fout << dp[n][k] << endl;
	}
	return 0;
}
