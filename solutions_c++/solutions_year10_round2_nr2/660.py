#include <iostream>
using namespace std;

const int N = 100;
int p[N], v[N];
int main()
{
	freopen("data.in", "r", stdin);
	freopen("result.out", "w", stdout);
	int tn, curt;
	cin >> tn;
	for(curt = 1; curt <= tn; ++curt) {
		int ans = 0;
		int n, k, b, t;
		cin >> n >> k >> b >> t;
		int i, j;
		for(i = 0; i < n; ++i) cin >> p[i];
		for(i = 0; i < n; ++i) cin >> v[i];

		for(i = 0; i < n; ++i) p[i] += v[i] * t;
		int sum = 0, c = 0;
		for(i = n-1; i >= 0; --i) {
			if(sum == k) break;
			if(p[i] < b) c++;
			else {
				sum++;
				ans += c;
			}
		}

		cout << "Case #" << curt << ": ";
		if(sum < k) cout << "IMPOSSIBLE" << endl;
		else  cout << ans << endl;
	}
	return 0;
}