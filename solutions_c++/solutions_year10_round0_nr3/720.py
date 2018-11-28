#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

typedef long long ll;
int g[10000];
int idx[10000];
ll sum[10000];

int main() {
	int t; cin>>t;
	for (int c = 1; c <= t; c++) {
		int r, k, n; scanf("%d%d%d", &r, &k ,&n);
		for (int i = 0; i < n; i++) scanf("%d", &g[i]);
		ll total = 0;
		for (int s = 0, e = 0; s < n; s++) {
			while (e < s+n && total + g[e%n] <= k) {
				total += g[e%n];
				e++;
			}
			sum[s] = total;
			idx[s] = e%n;
			total -= g[s];
		}
		int first = 0, cycle = 1;
		vector<bool> used(n);
		int i;
		ll ans = 0;
		for (i = 0; !used[i]; i = idx[i]) {
			used[i] = true;
			if (first++ < r) ans += sum[i];
		}
		int end = i;
		ll cyclesum = sum[i];
		for (i = idx[i]; i != end; i = idx[i]) {
			cyclesum += sum[i];
			cycle++;
		}
		r -= first;
		if (r > 0) {
			ans += cyclesum * (r/cycle);
			int mod = r % cycle;
			int j = 0;
			for (i = end; j < mod; i = idx[i], j++) {
				ans += sum[i];
			}
		}
		cout<<"Case #"<<c<<": "<<ans<<endl;
	}
	return 0;
}
