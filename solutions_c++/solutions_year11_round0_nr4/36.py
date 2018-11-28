#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		int N;
		cin >> N;
		int a[1000], b[1000];
		for (int i = 0; i < N; i++) {
			cin >> a[i];
			b[i] = a[i];
		}
		sort(b, b+N);
		int match = 0;
		for (int i = 0; i < N; i++) {
			if (a[i] == b[i]) match++;
		}
		
		int res = N-match;
		
		cout << "Case #" << icase << ": " << res << endl;
	}
	return 0;
}
