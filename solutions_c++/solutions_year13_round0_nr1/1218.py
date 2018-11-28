
#include <iostream>
using namespace std;

#define show(x) #x " = " << (x)
#define rep(i,n) for (int i = 0; i < int(n); ++i)
int geti() { int x; cin >> x; return x; }

char a[4], map[4][4];
bool check() {
	char c = '\0';
	rep (i,4) {
		if (a[i] == '.') return false;
		if (a[i] == 'T') continue;
		if (c == '\0')
			c = a[i];
		else
			if (c != a[i]) return false;
	}
	if (c == 'X')
		cout << "X won" << endl;
	else
		cout << "O won" << endl;
	return true;
}

void solve() {
	rep (i,4) rep (j,4) cin >> map[i][j];

	bool blank_exist = false;
	rep (i,4) rep (j,4) if (map[i][j] == '.') blank_exist = true;

	rep (i,4) {
		rep (j,4) a[j] = map[i][j];
		if (check()) return;
	}
	rep (j,4) {
		rep (i,4) a[i] = map[i][j];
		if (check()) return;
	}
	rep (i,4) a[i] = map[i][i];
	if (check()) return;
	rep(i,4) a[i] = map[i][3-i];
	if (check()) return;

	if (blank_exist)
		cout << "Game has not completed" << endl;
	else
		cout << "Draw" << endl;
}

int main() {
	int n = geti();
	rep (i,n) {
		cout << "Case #" << i+1 << ": ";
		solve();
	}
}
