#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
	freopen("data.in", "r", stdin);
	freopen("result.out", "w", stdout);
	int tn, curt;
	cin >> tn;
	for(curt = 1; curt <= tn; ++curt) {
		long long L, P, C;
		cin >> L >> P >> C;
		long long a = 0;
		while(L < P) {
			a++;
			L *= C;
		}
		int ans = 0;
		long long t = 1;
		while(t < a) {
			ans++;
			t *= 2;
		}
		cout << "Case #" << curt << ": ";
		cout << ans << endl;
	}
	return 0;
}