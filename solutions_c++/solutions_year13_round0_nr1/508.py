#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool ok(char c, char f) {
	return f == 'T' || f == c;
}

string check(const vector<string>& f) {
	bool has_free = false;
	vector<int> x(f.size() * 2 + 2), o(f.size() * 2 + 2);
	for (size_t i = 0; i < f.size(); ++i) {
		for (size_t j = 0; j < f.size(); ++j) {
			has_free |= f[i][j] == '.';
			x[i] += ok('X', f[i][j]);
			x[f.size() + j] += ok('X', f[i][j]);
			o[i] += ok('O', f[i][j]);
			o[f.size() + j] += ok('O', f[i][j]);
		}
		x[f.size() + f.size()] += ok('X', f[i][i]);
		x[f.size() + f.size() + 1] += ok('X', f[i][f.size() - 1 - i]);
		o[f.size() + f.size()] += ok('O', f[i][i]);
		o[f.size() + f.size() + 1] += ok('O', f[i][f.size() - 1 - i]);
	}
	if (*max_element(x.begin(), x.end()) == 4)
		return "X won";
	if (*max_element(o.begin(), o.end()) == 4)
		return "O won";
	if (has_free)
		return "Game has not completed";
	return "Draw";
}

void solve() {
	vector<string> f(4);
	for (size_t i = 0; i < f.size(); ++i)
		cin >> f[i];

	static int testid = 0;
	cout << "Case #" << ++testid << ": ";
	cout << check(f) << endl;
}

int main() {
	int t;
	cin >> t;
	while (t--) solve();
	return 0;
}
