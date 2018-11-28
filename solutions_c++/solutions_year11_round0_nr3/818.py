
#include <map>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <cassert>
#include <iostream>
#include <algorithm>
using namespace std;

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
		int n = parseInt(next());
		int totalSum = 0;
		int totalXor = 0;
		vector<int> nums(n);
		for (int i = 0; i < int(nums.size()); ++i) {
			nums[i] = parseInt(next());
			totalSum += nums[i];
			totalXor ^= nums[i];
		}
		if (totalXor != 0)
			printf("Case #%d: NO\n", test + 1);
		else
			printf("Case #%d: %d\n", test + 1, totalSum - *min_element(nums.begin(), nums.end()));
	}
	return 0;
}