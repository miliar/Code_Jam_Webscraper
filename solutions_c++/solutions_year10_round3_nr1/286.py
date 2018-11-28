#include <iostream>
#include <vector>

using namespace std;

int main() {
	int T;
	cin >> T;

	for (int nc = 1;nc <= T;++nc) {
		int n;
		cin >> n;
		vector<int> a(n),b(n);
		for (int i = 0;i < n;++i) 
			cin >> a[i] >> b[i];
		int count = 0;
		for (int i = 0;i < n;++i) {
			for (int j = i + 1;j < n;++j) {
				if ((a[i] - a[j]) * (b[i] - b[j]) < 0)
					count++;

			}
		}
		cout << "Case #" << nc << ": " << count << endl;
	}
	return 0;
}