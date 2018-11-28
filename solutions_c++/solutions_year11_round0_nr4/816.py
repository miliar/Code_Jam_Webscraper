
#include <map>
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cassert>
using namespace std;

map<vector<int>, int> cache;

string next() {
	string res;
	cin >> res;
	return res;
}

int parseInt(string s) {
	int res;
	sscanf(s.c_str(), "%d", &res);
	return res;
}

int main() {
	int testsCount = parseInt(next());
	for (int test = 0; test < testsCount; ++test) {
		int len = parseInt(next());
		vector<int> perm(len);
		for (int i = 0; i < len; ++i)
			perm[i] = parseInt(next());
		int res = 0;
		for (int i = 0; i < len; ++i)
			if (perm[i] != i + 1) {
				++res;
			}
		printf("Case #%d: %.6lf\n", test + 1, res + 0.0);
	}
	return 0;
}