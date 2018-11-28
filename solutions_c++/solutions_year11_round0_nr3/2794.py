#include <iostream>
#include <cmath>
#include <string>
#include <algorithm>
#include <fstream>
using namespace std;

int main() {
	ifstream cin("C-small.in");
	ofstream cout("C-small.out");
	int T;
	cin >> T;
	for (int c = 1; c <= T; c++) {
		cout << "Case #" << c << ": ";
		int N;
		cin >> N;
		int C[100];
		int xor = 0;
		for (int i = 0; i < N; i++) {
			cin >> C[i];
			xor ^= C[i];
		}
		int res = -1;
		for (int i = 0; i < (1<<N)-1; i++) {
			int hopa = 0;
			int xhopa1 = 0, xhopa2 = 0;
			for (int t = 0; t < N; t++) {
				if (i & (1<<t)) {
					hopa += C[t];
					xhopa1 ^= C[t];
				} else
					xhopa2 ^= C[t];
			}
			if (xhopa1 == xhopa2)
				res = max(res, hopa);
		}
		if (res == -1)
			cout << "NO" << endl;
		else
			cout << res << endl;
	}

	return 0;
}