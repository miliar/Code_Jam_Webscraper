#include <iostream>
#include <algorithm>
using namespace std;

const int MAXN = 2000;
int f[MAXN], n, m, l;

void process() {
	cin >> m >> n >> l;
	for (int i = 0; i < l; i++)
		cin >> f[i];

	int res = 0;
	sort(f, f+l);
	reverse(f, f+l);
	for (int i = 0; i < l; i++)
		res += (i/n+1) * f[i];
	cout << res << endl;
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i+1 << ": ";
		process();
	}
}

