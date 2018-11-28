#include <iostream>
#include <string>
#include <cstdio>
#include <algorithm>
#include <set>
using namespace std;

inline int Length(int x) {
	int res = 0;
	while (x) {
		x /= 10;
		++res;
	}
	return res;
}

inline int Shift(int x, const int LEN) {
	char buf[10];
	itoa(x, buf, 10);
	int len = strlen(buf);
	if (len < LEN) {
		for (int i = 0; i < len; ++i) {
			buf[LEN - i - 1] = buf[len - i - 1];
			buf[len - i - 1] = '0';
		}
		len = LEN;
	}
	int res = 0;
	for (int i = 0; i < len; ++i) {
		res = 10 * res + (buf[(len - 1 + i) % len] - '0');
	}
	return res;
}

long long Rotate(int x, int b) {
	set<int> S;
	int mi = x;
	long long res = 0;
	int len = Length(x);
	for (int i = 0; i < len; ++i) {
		x = Shift(x, len);
		if (mi < x && x <= b) {
			if (S.insert(x).second) {
				++res;
			}
		}
	}
	return res;}

long long Solve(int a, int b) {
	long long res = 0;
	for (int i = a; i <= b; ++i) {
		res += Rotate(i, b);
	}
	return res;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: ", i);
		int a, b;
		cin >> a >> b;
		cout << Solve(a, b) << endl;
	}
	return 0;
}