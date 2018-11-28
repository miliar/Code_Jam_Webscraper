#include <iostream>
#include <set>
using namespace std;

int tens[20];

int dig(int a) {
	int r = 0;
	while (a) a /= 10, ++r;
	return r;
}

int rot(int i, int n, int k) {
	// k=2: aaaaabb -> bbaaaaa
	return i/tens[k] + (i%tens[k]) * tens[n-k];
}

int main() {
	tens[0] = 1;
	for (int i = 1; i < 20; ++i) tens[i] = tens[i-1]*10;

	int T, C = 1, a, b;
	cin >> T;
	while (T-- && cin >> a >> b) {
		int n = dig(a), r = 0;
		for (int i = a; i <= b; ++i) {
			set<int> rr;
			for (int k = 1; k < dig(a); ++k) {
				int j = rot(i, n, k);
				if (j > i && j <= b)
					rr.insert(j);
			}
			r += rr.size();
		}

		cout << "Case #" << C++ << ": " << r << endl;
	}
}
