#include <iostream>
#include <string>

using namespace std;
string W [5000];
int L, D, N;
int isMatched (const string& w, const string& p) {
	int i, j = 0;
	int m [256];
	for (i = 0; i < w.length(); ++i) {
		memset(m, 0, sizeof (m));
		if (p [j] == '(') {
			++j;
			while (p [j] != ')') {
				m [p[j]] = 1;
				++j;
			}
		} else {
			m [p[j]] = 1;
		}
		++j;
		if (!m [w [i]]) return 0;
	}
	return 1;
}

int cnt (const string& p) {
	int res = 0;
	for (int i = 0; i < D; ++i)
		if (isMatched(W [i], p)) ++res;
	return res;
}
int main () {
	cin >> L >> D >> N;
	for (int i = 0; i < D; ++i)
		cin >> 	W [i];
	for (int x = 0; x < N; ++x) {
		string w;
		cin >> w;
		cout << "Case #" << (x + 1) << ": ";
		cout << cnt (w);
		cout << endl;
	}
}
