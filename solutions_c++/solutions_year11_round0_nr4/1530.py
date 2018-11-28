#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	for (int j = 0; j < t; j++) {
		int n;
		cin >> n;
		int s = 0;
		for (int i = 0; i < n; i++) {
			int a;
			cin >> a;
			if (a != i + 1) {
				s++;
			}
		}
		cout << "Case #" << j + 1 << ": " << s << endl;
	}
}

