#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <cassert>

using namespace std;

int from, to;

void read () {
	cin >> from >> to;
	assert(from <= to);
}

vector<int> get_digits (int x) {
	vector<int> digits;
	while (x) {
		digits.push_back(x % 10);
		x /= 10;
	}
	reverse(digits.begin(), digits.end());
	return digits;
}

int get_number (vector<int> digits) {
	int x = 0;
	for (int i = 0; i < (int)digits.size(); ++i) {
		x *= 10;
		x += digits[i];
	}
	return x;
}

int count_of_shifts_in_range (int x) {
	vector<int> digits = get_digits(x);
	set<int> was;
	was.insert(x);
	
	int count = 0;
	for (int i = 0; i < (int)digits.size(); ++i) {
		rotate(digits.begin(), digits.begin() + 1, digits.end());
		if (digits[0] != 0) {
			int y = get_number(digits);
			if (x < y && y <= to && was.find(y) == was.end()) {
				++count;
				was.insert(y);
			}
		}
	}
	return count;
}

void sol (int test_number) {
	int count = 0;
	for (int i = from; i <= to; ++i) {
		count += count_of_shifts_in_range(i);
	}
	printf("Case #%d: %d\n", test_number, count);
}

int main () {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	
	int i, t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		read();
		sol(i + 1);
	}
	return 0;
}