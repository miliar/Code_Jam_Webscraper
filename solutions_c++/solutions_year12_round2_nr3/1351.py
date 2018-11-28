#include <iostream>
#include <fstream>
#include <map>

using namespace std;

int main() {
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);

	int T;
	cin >> T;
	for (int x = 1; x <= T; x++) {
		int res = 0;
		map<int, int> s;

		int N; cin >> N; int a[N];
		for (int i = 0; i < N; i++) cin >> a[i];
		int s1 = -1, s2 = -1;
		for (int i = 1; i < (1 << N); i++) {
			int sum = 0;
			for (int j = 0; j < N; j++) {
				if ((i & (1 << j)) != 0) {
					sum += a[j];
				}
			}
			if (s.find(sum) != s.end()) {
				if ((i & s[sum]) == 0) {
					s1 = i;
					s2 = s[sum];
					break;
				}
			} else {
				s[sum] = i;
			}
		}
		cout << "Case #" << x << ":";
		if (s1 != -1 && s2 != -1) {
			cout << endl;
			for (int i = 0; i < N; i++) {
				if ((s1 & (1 << i)) != 0) {
					cout << a[i] << " ";
				}
			}
			cout << endl;
			for (int i = 0; i < N; i++) {
				if ((s2 & (1 << i)) != 0) {
					cout << a[i] << " ";
				}
			}
			cout << endl;
		} else {
			cout << "Impossible" << endl;
		}
	}
}
