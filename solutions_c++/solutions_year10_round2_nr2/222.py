#include <cstdio>
#include <cmath>
#include <iostream>

using namespace std;
typedef unsigned long long ull;
void func();

int main() {
  freopen("in.in", "r", stdin);
  freopen("output.out", "w", stdout);

  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; i++) {
  	cout << "Case #" << i << ":";
  	func();
  }

  fclose(stdin);
  fclose(stdout);
}

	ull x[55];
	ull v[55];
	ull n,k,b,t;
	bool r[55];
// WRITE ALL CODE BELOW THIS
void func() {
	cin >> n >> k >> b >> t;
	for (int i = 0; i < n; i++)
		cin >> x[i];
	ull kposs = 0;
	for (int i = 0; i < n; i++) {
		cin >> v[i];
		if (x[i] + v[i]*t < b)
			r[i] = false;
		else {
			r[i] = true;
			kposs++;
		}
	}
	if (kposs < k) {
		cout << " IMPOSSIBLE\n";
	} else {
		ull hurdles = 0;
		ull res = 0;
		for (int i = n-1; i >= 0 && k > 0; i--) {
			if (!r[i]) {
				hurdles++;
				continue;
			}
			res += hurdles;
			k--;
		}
		cout << " " << res << endl;
	}
}
