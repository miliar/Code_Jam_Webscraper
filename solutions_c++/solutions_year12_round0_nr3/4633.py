#include <iostream>
#include <algorithm>
#include <fstream>
#include <set>
using namespace std;

ifstream fin("c.in");
ofstream fout("c.out");
int powcount = 8;
int pows[] = { 1, 10, 100, 1000, 10000, 100000, 100000, 1000000 };

int check(int n, int B) {
	set<int> seen;
	int orig = n;
	int *k = lower_bound(pows, pows + powcount, n);
	if (n != *k) k--;

	int ret = 0;

	int a = (n % 10) * (*k); n /= 10;
	while (n > 0) {
		if (seen.find(a + n) == seen.end() && orig < a + n && a + n <= B) {
			ret++;
			seen.insert(a + n);
		}

		a = a / 10 + (n % 10) * (*k);
		n /= 10;
	}

	return ret;
}

int main() {
	int N, A, B, cnt = 0;
	fin >> N;

	for (int i = 0; i < N; i++) {
		cout << i << '\n';
		fin >> A >> B;
		cnt = 0;
		for (int n = A; n < B; n++) {
			cnt += check(n, B);
		}

		fout << "Case #" << i + 1 << ": " << cnt << "\n";
	}

	system("PAUSE");
	return 0;
}