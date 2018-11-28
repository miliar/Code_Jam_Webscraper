#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <list>
#include <string>
#include <vector>

using namespace std;

void mysort(vector<int> &a, int l, int r) {
	int i = l;
	int j = r;
	int x = a[(l + r) / 2];
	do {
	//cout << l << " " << r << " " << i << " " << j << " " <<x << endl;
		while (a[i] < x) ++i;
		while (a[j] > x) --j;
		if (i <= j) {
			swap(a[i], a[j]);
			++i; --j;
		}
	} while (i <= j);
	if (i < r) mysort(a, i, r);
	if (l < j) mysort(a, l, j);
}

void Solve(string &s) {
	vector<int> nums(s.size());
	for(int i = 0; i < s.size(); ++i) {
		nums[i] = s[i] - '0';
	}
	int i = nums.size() - 2;
	while (i >= 0 && nums[i] >= nums[i + 1]) {
		--i;
	}
	int num = nums[i];
	if (i < 0) {
		mysort(nums, 0, nums.size() - 1);
		int j = 0;
		while (nums[j] == 0) {
			++j;
		}
		cout << nums[j] << 0;
		for(int i = 0; i < j; ++i) {
			cout << 0;
		}
		for(int i = j + 1; i < nums.size(); ++i) {
			cout << nums[i];
		}
		cout << endl;
	} else {
		mysort(nums, i + 1, nums.size() - 1);
		int j = i + 1;
		while (j < nums.size() - 1 && nums[i] >= nums[j]) {
			++j;
		}
		swap(nums[i], nums[j]);
		for(int i = 0; i < nums.size(); ++i) {
			cout << nums[i];
		}
		cout << endl;
	}
}

int N;

void Init() {
	cin >> N;
	for(int i = 0; i < N; ++i) {
		string s;
		cin >> s;
		cout << "Case #" << i + 1 << ": ";
		Solve(s);
	}
}

int main() {
	Init();
	return 0;
}
