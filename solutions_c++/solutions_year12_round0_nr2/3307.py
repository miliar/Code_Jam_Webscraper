#include <iostream>

using namespace std;

int a[105][105];
int b[105];
int c[105];
int t;
int n, s;
int p;

int solve(int n, int s){
//cout << "solve " << n << " " << s << endl;
	if (n == -1 && s == 0) return 0;
	if (n + 1 < s) return -1000;
	if (s < 0) return -1000;

	if (a[n][s]) return a[n][s];
	int ans1 = solve(n - 1, s - 1);
	int ans2 = solve(n - 1, s);
	if (c[n] >= p) ++ans1;
	if (b[n] >= p) ++ans2;
	if (c[n] == -100) ans1 = -1000;
//cout << "!" << n << " " << s << " " << ans1 << " " << ans2 << endl;
	a[n][s] = max(ans1, ans2);
//cout << "ans" << n << " " << s <<  " " << a[n][s] << endl;
	return a[n][s];
}

int main(){
	cin >> t;
	for (int _i = 0; _i < t; ++_i){
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		memset(c, 0, sizeof(c));
		cin >> n >> s >> p;
		for (int i = 0; i < n; ++i){
			int x;
			cin >> x;
			b[i] = x / 3;
			if (x % 3) ++b[i];
			c[i] = 2 + (x - 2) / 3;
			if (x < 2 || x > 28) c[i] = -100;
//cout << b[i] << " " << c[i] << endl;
		}
		cout << "Case #" << _i + 1 << ": " << solve(n - 1, s) << endl;
	}
	return 0;
}