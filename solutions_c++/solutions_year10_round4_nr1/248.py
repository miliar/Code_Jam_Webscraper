#include <cstdio>
#include <algorithm>
using namespace std;
#include <iostream>
#include <vector>

int get(int size, int row) {
	if (row < size)
		return row + 1;
	return 2 * size - row - 1;
}

bool diff(int a, int b) {
	if (a == -1) return false;
	if (b == -1) return false;
	return (a != b);
}

bool check(const vector<vector<int> > &a, int start_i, int start_j, int s) {
	int k = a.size();
	for (int i = start_i; i < start_i + s; ++i)
		for (int j = start_j; j < start_j + s; ++j)
			if (diff(a[i][j], a[j][i]))
				return false;
	for (int i = start_i; i < start_i + s; ++i)
		for (int j = start_j; j < start_j + s; ++j)
			if (diff(a[i][j], a[k - j - 1][k - i - 1]))
				return false;
	return true;
}

bool can(int sz, const vector<vector<int> > &a) {
	int k = a.size();
	vector<vector<int> > b;
	b.resize(sz);
		for (int i = 0; i < sz; ++i)
			b[i].assign(sz, -1);
		for (int start_i = 0; start_i < sz - k + 1; ++start_i)
			for (int start_j = 0; start_j < sz - k + 1; ++start_j) {
				for (int i = 0; i < k; ++i)
					for (int j = 0; j < k; ++j)
						b[i + start_i][j + start_j] = a[i][j];
				if (check(b, start_i, start_j, k)) {
//					printf("\n");
//					for (int i = 0; i < b.size(); ++i) {
//						for (int j = 0; j < b[i].size(); ++j)
//							cout << b[i][j] << " ";
//						cout << endl;
//					}
					return true;
				}
				for (int i = 0; i < k; ++i)
					for (int j = 0; j < k; ++j)
						b[i + start_i][j + start_j] = -1;
			}
	return false;
}

void solve() {
	int k;
	cin >> k;
	vector<vector<int> > a(k), b;
	for (int i = 0; i < k; ++i) a[i].resize(k);
	for (int sum = 0; sum <= 2 * k; ++sum)
		for (int i = 0; i < k; ++i)
			for (int j = 0; j < k; ++j)
				if (i + j == sum)
					cin >> a[i][j];
/*	int OMIN = k - 1;
	int OMAX = 4 * k + 10;
	while (OMAX != OMIN + 1) {
		cerr << OMIN << " " << OMAX << endl;
		int tmp = (OMAX + OMIN) / 2;
                if (can(tmp, a))
                	OMAX = tmp;
		else
			OMIN = tmp;                		
	}
	cerr << endl << endl << endl;
	printf("%d\n", OMAX * OMAX - k * k);*/
	for (int sz = 0;; ++sz)
		if (can(sz, a)) {
			printf("%d\n", sz * sz - k * k);
			return;
		}

//even
	int OMIN = k - 1;
	int OMAX = 3 * k + 5;
	if (OMIN % 2 == 1)
		--OMIN;
	if (OMAX % 2 == 1)
		++OMAX;
	while (OMIN != OMAX - 2) {
		cerr << OMIN << " " << OMAX << endl;
		int tmp = (OMIN + OMAX) / 2;
		if (tmp % 2 == 1)
			--tmp;
		if (can(tmp, a))
			OMAX = tmp;
		else
			OMIN = tmp;
	}
	int a1 = OMAX * OMAX - k * k;
//odd
	OMIN = k - 1;
	OMAX = 3 * k + 5;
	if (OMIN % 2 == 0)
		--OMIN;
	if (OMAX % 2 == 0)
		++OMAX;
	while (OMIN != OMAX - 2) {
		cerr << OMIN << " " << OMAX << endl;
		int tmp = (OMIN + OMAX) / 2;
		if (tmp % 2 == 0)
			--tmp;
		if (can(tmp, a))
			OMAX = tmp;
		else
			OMIN = tmp;
	}
	int a2 = OMAX * OMAX - k * k;
	printf("%d\n", min(a1, a2));


}


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cerr << "Test " << i << endl;
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
