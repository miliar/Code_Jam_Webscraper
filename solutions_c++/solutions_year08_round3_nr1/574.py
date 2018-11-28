#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int tn;
	cin >> tn;
	for(int ti = 0; ti < tn;) {
		int p, k, l;
		cin >> p >> k >> l;
		int *f = new int[l];
		for(int i = 0; i < l; i++)
			cin >> f[i];
		sort(f, f + l);
		reverse(f, f + l);
		long long r = 0;
		for(int i = 0; i < l; i++)
			r += f[i] * (i / k + 1);
		cout << "Case #" << ++ti << ": " << r << endl;
	}
	return 0;
}
