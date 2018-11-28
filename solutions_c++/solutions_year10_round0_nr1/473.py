#include <fstream>
using namespace std;
ifstream cin("input.txt");
ofstream cout("output.txt");
int main() {
	int n, k, t;
	cin >> t;
	for (int tt = 0; tt < t; tt++) {
		cin >> n >> k;
		bool ans = true;
		for (int i = 0; i < n && ans; i++) {
			ans &= (k % 2 == 1);
			k /= 2;
		}
		cout << "Case #" << (tt + 1) << ": ";
		if (ans) cout << "ON\n"; else cout << "OFF\n";
	}
	return 0;
}