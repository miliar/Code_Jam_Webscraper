/**
	Copyright 2011 Wei Xueliang
**/
#include <iostream>
#include <string>
#include <cmath>
#include <cstdio>
#include <map>
using namespace std;

int T;
int N;
short int x[100];

void addx(int c) {
	int i = 0;
	while (c > 0) {
		short int d = c % 2;
		x[i] += d;
		x[i] %= 2;

		c /= 2;
		i++;
	}
}

int main() {
	cin >> T;

	for (int ti = 1; ti <= T; ti++) {
		cin >> N;

		memset(x, 0, sizeof(x));
		int min1 = 100000000;
		int sum = 0;

		for (int i = 0; i < N; i++) {
			int c;
			cin >> c;
			sum += c;
			if (c < min1) {
				min1 = c;
			}
			addx(c);
		}
		bool found = false;
		for (int i = 0; i < 100; i++) {
			if (x[i] != 0) {
				found = true;
				break;
			}
		}
		if (found) {
			cout << "Case #" << ti << ": NO" << endl;
		}
		else {
			cout << "Case #" << ti << ": " << sum - min1 << endl;
		}
	}
	return 0;
}
