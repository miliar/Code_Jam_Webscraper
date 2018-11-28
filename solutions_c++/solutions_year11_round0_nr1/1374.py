#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(void) {
	int T;
	cin >> T;
	for (int testNo = 1; testNo <= T; testNo++) {
		cout << "Case #" << testNo << ": ";
		int N;
		cin >> N;
		int p1 = 1, p2 = 1;
		int m1 = 0, m2 = 0;
		while (N--) {
			string str; int ps;
			cin >> str >> ps;
			if (str[0] == 'O') {
				m1 = max(m2 + 1, m1 + abs(ps - p1) + 1);
				p1 = ps;
			} else {
				m2 = max(m1 + 1, m2 + abs(ps - p2) + 1);
				p2 = ps;
			}
		}
		cout << max(m1, m2) << endl;
	}
}
