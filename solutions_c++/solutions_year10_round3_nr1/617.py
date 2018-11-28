#include <iostream>

using namespace std;



int main() {
	int t;
	cin >> t;
	for (int cs = 1; cs <= t; cs++) {
		int n;
		cin >> n;

		int a[1024], b[1024];
		for (int i = 0; i < n; i++) {
			cin >> a[i] >> b[i];
		}

		int res = 0;
		for (int i = 0; i < n; i++) {
			for (int j = i+1; j < n; j++) {
				if ((a[i] > a[j] && b[i] < b[j]) || (a[i] < a[j] && b[i] > b[j])) {
					res++;
				}
			}
		}

		cout << "Case #" << cs << ": " << res << endl;
	}
}
