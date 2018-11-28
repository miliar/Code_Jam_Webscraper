#include <iostream>
#include <string>
#include <vector>

using namespace std;

string words[5000];

bool mat(string t, string p, int i1, int i2) {
	if (i1 >= t.size() && i2 >= p.size()) return 1;
	if (p[i2] == '(') {
		i2++;
		bool fnd = 0;
		while (p[i2] != ')') {
			if (p[i2] == t[i1]) {
				fnd = 1;
			}
			i2++;
		}
		if (fnd) return mat(t, p, i1+1, i2+1);
		return 0;
	}
	if (p[i2] == t[i1]) return mat(t, p, i1+1, i2+1);
	return 0;
}

int main () {
	int l, d, n;
	int i, j, k;
	cin >> l >> d >> n;
	for (i=0; i<d; i++) {
		cin >> words[i];
	}
	string test;
	for (i=0; i<n; i++) {
		cin >> test;
		int cnt = 0;
		for (j=0; j<d; j++) {
			if (mat(words[j], test, 0, 0)) {
				cnt++;
			}
		}
		cout << "Case #" << i+1 << ": " << cnt << endl;
	}
	return 0;
}
