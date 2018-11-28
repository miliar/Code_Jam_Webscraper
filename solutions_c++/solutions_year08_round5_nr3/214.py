#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <utility>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

string input = "C-small-attempt0.in", output = input + "___.out";
ifstream ifs(input.c_str());
ofstream ofs(output.c_str());

const int bin[13] = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 1 << 11, 1 << 12};

char buf[128][128];
int mask[11], cnt1[1 << 10], next[1 << 10], valid[1 << 10];
int dp[11][1 << 10];

int main(void)
{
	int re;
	int m, n;

	for (int i = 0; i < 1024; i++) {
		cnt1[i] = 0;
		next[i] = 0;
		valid[i] = 1;
		for (int j = 0; j < 10; j++) {
			if (i & bin[j]) {
				++cnt1[i];
				if (j > 0) next[i] |= bin[j - 1];
				next[i] |= bin[j + 1];
				if (i & bin[j + 1]) valid[i] = 0;
			}
		}
	}
	ifs >> re;
	for (int ri = 1; ri <= re; ri++) {
		// input
		ifs >> m >> n;
		for (int i = m; i >= 1; i--) {
			mask[i] = 0;
			for (int j = 0; j < n; j++) {
				ifs >> buf[i][j];
				if (buf[i][j] == 'x') {
					mask[i] |= bin[j];
				}
			}
		}
		// doit
		for (int j = 0; j < bin[n]; j++) {
			dp[0][j] = 0;
		}
		for (int i = 1; i <= m; i++) {
			for (int j = 0; j < bin[n]; j++) {
				dp[i][j] = 0;
				if (!valid[j] || (j & mask[i]) != 0) {
					continue;
				}
				for (int k = 0; k < bin[n]; k++) {
					if (valid[k] && (j & next[k]) == 0) {
						dp[i][j] = max(dp[i][j], dp[i - 1][k] + cnt1[j]);
					}
				}
			}
		}
		// output
		cerr << ri << endl;
		ofs << "Case #" << ri <<": " << *max_element(dp[m], dp[m] + bin[n]) << endl;
	}

	return 0;
}
