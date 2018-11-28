#include <iostream>
#include <map>

using namespace std;

void solve() {
	int a, b, nd = 1;
	long long res = 0;
	cin >> a >> b;
	for (int t = a; t > 0; t /= 10) nd *= 10; 
	nd /= 10;
	map<int, bool> reps;
	for (int n = a; n < b; n++) {
		for (int d = 10; d <= nd; d *= 10) {
			int temp = (n%d)*(nd/d)*10 + n/d;
			if (temp <= b && n < temp) {
				if (!reps[temp]) {
					reps[temp] = true;
					res++;
				}
			}
		}
		reps.clear();
	}
	cout << res;
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int T;
	cin >> T;

	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": "; 
		solve(); 
		cout << endl;
	}

	return 0;
}