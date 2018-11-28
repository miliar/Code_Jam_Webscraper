#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <string>
#include <map>
using namespace std;

ifstream fin("B-large.in");
ofstream fout("out.txt");

int p, m[1024], cost[1024][11], dp[1024][11][10];

int work(int s, int pw, int dec) {
	if (dp[s][pw][dec] >= 0) return dp[s][pw][dec];
	if (pw == 1) {
		if (m[s] < dec || m[s + 1] < dec) return -1;
		if (m[s] == dec || m[s + 1] == dec) dp[s][0][dec] = cost[s][1];
		else dp[s][0][dec] = 0;
		return dp[s][0][dec];
	}
	int s1 = work(s, pw - 1, dec + 1);
	int s2 = work(s + (1 << (pw - 1)), pw - 1, dec + 1);
	if (s1 >= 0 && s2 >= 0) dp[s][pw][dec] = s1 + s2;
	s1 = work(s, pw - 1, dec);
	s2 = work(s + (1 << (pw - 1)), pw - 1, dec);
	if (s1 >= 0 && s2 >= 0 && (dp[s][pw][dec] < 0 || dp[s][pw][dec] > s1 + s2 + cost[s][pw]))
		dp[s][pw][dec] = s1 + s2 + cost[s][pw];
	return dp[s][pw][dec];
}

int main() {
	int t;
	fin >> t;
	for (int i = 1; i <= t; ++i) {
		fout << "Case #" << i << ": ";
		fin >> p;
		for (int i = 0; i < (1 << p); ++i) fin >> m[i];
		for (int i = 0; i < p; ++i)
			for (int j = 0; j < (1 << p); j += (1 << (i + 1))) fin >> cost[j][i + 1];
		for (int i = 0; i < (1 << p); ++i)
			for (int j = 0; j <= p; ++j)
				for (int k = 0; k < p; ++k) dp[i][j][k] = -1;
		fout << work(0, p, 0) << endl;
	}
	return 0;
}
