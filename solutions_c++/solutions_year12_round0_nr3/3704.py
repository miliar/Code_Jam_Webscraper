#include <iostream>
#include <set>

using namespace std;
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int A, B;
		cin >> A >> B;

		int d = 1;
		int tmp = A;
		while (tmp >= 10) { d *= 10; tmp /= 10; }

		int answer = 0;
		set<int> checked;
		for (int i = A; i <= B; i++) {
			if (checked.find(i) != checked.end())
				continue;
			int n = i;

			int cnt = 0;
			while (checked.find(n) == checked.end()) {
				if (A <= n && n <= B) {
					checked.insert(n);
					cnt++;
				}
				n = (n % 10) * d + (n / 10);
			}
			if (cnt > 1) answer += cnt * (cnt-1) / 2;
		}
		cout << "Case #" << t << ": " << answer << endl;
	}
}
