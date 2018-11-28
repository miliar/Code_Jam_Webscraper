#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
vector<int> a;

int main() {
	int testCnt;
	cin >> testCnt;

	for (int T = 1; T <= testCnt; ++T) {
		cout << "Case #" << T << ": ";
		int N, L, H;
		cin >> N >> L >> H;
		a.clear();
		for (int i = 0; i < N; ++i) {
			int t;
			cin >> t;
			a.push_back(t);
		}
		int r = -1;
		for (int i = L; i <= H; ++i) {
			bool fl = true;
			for (int j = 0; j < N; ++j)
				if (a[j] % i != 0 && i % a[j] != 0) {
					fl = false;
					break;
				}
			if (fl) {
				r = i;
				break;
			}
		}
		if (r != -1)
			cout << r << endl;
		else
			cout << "NO" << endl;

	}

	return 0;
}