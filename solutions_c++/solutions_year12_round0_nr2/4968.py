#include <cstdio>
#include <iostream>
#include <fstream>

using namespace std;

void solveTestCase(void) {
	int n, s, p, k;
	int ok = 0, pot = 0;
	cin >> n >> s >> p;
	int ok_lim = 3 * p - 2;
	int pot_lim = 3 * p - 4;
	switch (p) {
	case 0:
		ok_lim = 0;
		pot_lim = 100500;
		break;
	case 1:
		ok_lim = 1;
		pot_lim = 100500;
		break;
	default:
		break;
	}
	cerr << ok_lim << " " << pot_lim << endl;
	for (int i = 0; i < n; ++i) {
		cin >> k;
		ok += k >= ok_lim;
		pot += k < ok_lim && k >= pot_lim;
	}
	ok += pot < s ? pot : s;
	cout << ok << endl;
}

void solveTheProblem(void) {
	int n;
	scanf("%d%*c", &n);
	for (int i = 0; i < n; ++i) {
		printf("Case #%d: ", i + 1);
		solveTestCase();
	}
}

int main(void) {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solveTheProblem();
	return 0;
}