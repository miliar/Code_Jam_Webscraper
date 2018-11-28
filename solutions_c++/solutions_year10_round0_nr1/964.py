#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	freopen("g:\\A-small-attempt0.in", "r", stdin);
	freopen("g:\\A-small-attempt0.out", "w", stdout);
	int n, k;
	int t;
	int ca = 0;
	cin >> t;
	while(t--) {
		ca++;
		cin >> n >> k;
		cout << "Case #" << ca << ": ";
		int maxn = (1 << n);
		k = k % maxn;
		if (k == maxn - 1) {
			cout << "ON" << endl;
		}else{
			cout << "OFF" << endl;
		}
	}
	return 0;
}
