#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main() {
	int T;
	cin >> T;

	for (int t=1;t<=T;t++) {
		int N;
		int x;
		cin >> N;
		int ops=0;
		for (int i=1;i<=N;i++) {
			cin >> x;
			if (x!=i) ops++;
		}
		cout << "Case #" << t << ": ";
		cout << ops;
		cout << endl;
	}
	return 0;
}
