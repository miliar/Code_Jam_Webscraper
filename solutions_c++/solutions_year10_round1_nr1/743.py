#include <iostream>
#include <vector>
using namespace std;

typedef vector<vector<int> > matrix;

int solve(matrix & t, int k) {
	int i, j, rep = 0, n = t.size();
	long long unsigned racc, bacc, masq = (1ull << k) - 1ull;
	for (i = 0; i < n; ++i) {
		racc = 0ull, bacc = 0ull;
		for (j = 0; j < n; ++j) {
			switch (t[i][j]) {
			case 1: racc |= 1ull; break;
			case 2: bacc |= 1ull; break;
			}
			if ((racc & masq) == masq) rep |= 1;
			if ((bacc & masq) == masq) rep |= 2;
			racc <<= 1;
			bacc <<= 1;
		}
	}
	for (i = 0; i < n; ++i) {
		racc = 0ull, bacc = 0ull;
		for (j = 0; j < n; ++j) {
			switch (t[j][i]) {
			case 1: racc |= 1ull; break;
			case 2: bacc |= 1ull; break;
			}
			if ((racc & masq) == masq) rep |= 1;
			if ((bacc & masq) == masq) rep |= 2;
			racc <<= 1;
			bacc <<= 1;
		}
	}
	for (i = -n+1; i < n; ++i) {
		racc = 0ull, bacc = 0ull;
		for (j = 0; i+j < n; ++j) {
			if (i + j < 0) continue;
			switch (t[i+j][j]) {
			case 1: racc |= 1ull; break;
			case 2: bacc |= 1ull; break;
			}
			if ((racc & masq) == masq) rep |= 1;
			if ((bacc & masq) == masq) rep |= 2;
			racc <<= 1;
			bacc <<= 1;
		}
	}
	for (i = -n+1; i < n; ++i) {
		racc = 0ull, bacc = 0ull;
		for (j = 0; i-j >= 0; ++j) {
			if (i - j >= n) continue;
			switch (t[i-j][j]) {
			case 1: racc |= 1ull; break;
			case 2: bacc |= 1ull; break;
			}
			if ((racc & masq) == masq) rep |= 1;
			if ((bacc & masq) == masq) rep |= 2;
			racc <<= 1;
			bacc <<= 1;
		}
	}
	return rep;
}

void gravity(matrix & t) {
	int i, j, last, n = t.size();
	for (j = 0; j < n; ++j) {
		last = 0;
		for (i = 0; i < n; ++i) {
			if (t[i][j] == 0)
				continue;
			swap(t[last][j], t[i][j]);
			++last;
		}
	}
}

void print(matrix & t) {
	int i, j, n = t.size();
	for (i = n - 1; i >= 0; --i) {
		for (j = 0; j < n; ++j) {
			switch (t[i][j]) {
			case 0: cout << "."; break;
			case 1: cout << "R"; break;
			case 2: cout << "B"; break;
			}
		}
		cout << endl;
	}
}

int main(void) {
	int ntest, num, n, k, i, j, rep;
	matrix t;
	char c;
	for (cin >> ntest, num = 1; num <= ntest; ++num) {
		cin >> n >> k;
		t.resize(n, vector<int> (n, 0));
		for (i = n - 1; i >= 0; --i) {
			for (j = n - 1; j >= 0; --j) {
				cin >> c;
				switch (c) {
				case '.': t[j][i] = 0; break;
				case 'R': t[j][i] = 1; break;
				case 'B': t[j][i] = 2; break;
				}
			}
		}
		gravity(t);
		//print(t);
		rep = solve(t,k);
		cout << "Case #" << num << ": ";
		switch (rep) {
		case 0 : cout << "Neither" << endl; break;
		case 1 : cout << "Red" << endl; break;
		case 2 : cout << "Blue" << endl; break;
		case 3 : cout << "Both" << endl; break;
		}
		t.clear();
	}
}
