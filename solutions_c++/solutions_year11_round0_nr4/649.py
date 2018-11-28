#include <iostream>
using namespace std;

const int maxn = 1010;

int n;
int a[maxn];

int main() {
	int tc;
	cin >> tc;
	for (int tt = 1; tt <= tc; tt++) {
		cin >> n;
		int cnt = n;
		for (int i = 0; i < n; i++) {
			cin >> a[i];
			if (a[i] == i + 1)
				cnt--;
		}
		
		printf("Case #%d: %.6lf\n", tt, 1.0 * cnt);
	}

}
