#include <iostream>
#include <map>
#include <utility>
using namespace std;

int A[200], n, p;
map<pair<int, int>, int> MM;
const int inf = 1000000;

int g(int t, bool s) {
	int x = t/3, y = t%3;
	if (!s) return x+(!!y) >= p;
	if (y == 2) return x + 2 >= p;
	return x + 1 >= p;
}

int f(int i, int s) {
	if (MM.find(make_pair(i, s)) != MM.end()) return MM[make_pair(i, s)];
	int &res = MM[make_pair(i, s)];

	if (i == n) return res = !s ? 0 : -inf;
	res = g(A[i], false) + f(i+1, s);
	if (s && A[i] >= 2 && A[i] <= 28) res = max(res, g(A[i], true) + f(i+1, s-1));
	return res;
}

int main() {
	int T, C = 1;
	cin >> T;
	int s;
	while (T-- && cin >> n >> s >> p) {
		for (int i = 0; i < n; ++i)
			cin >> A[i];

		MM.clear();
		cout << "Case #" << C++ << ": " << f(0, s) << endl;
	}
}
