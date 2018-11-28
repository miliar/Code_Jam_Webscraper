#include <iostream>

using namespace std;
typedef long long ll;

ll r, k;
int n;
ll g[2048];
ll arr[2048];
ll val[2048];

int main(){
	int t; cin >> t;
	for (int zzz = 1; zzz <= t; zzz++){
		cin >> r >> k >> n;
		for (int i = 0; i < n; i++)
			cin >> g[i];
		ll total = 0;
		for (int i = 0; i < n; i++)
			total += g[i];
		for (int i = 0; i < n; i++)
			arr[i] = -1;
		int curr = 0;
		ll ti = 0;
		ll ans = 0;
		while (arr[curr] == -1 && ti < r){
			//cout << "ti = " << ti << ", ans = " << ans << ", curr = " << curr << endl;
			arr[curr] = ti;
			val[curr] = ans;
			ll sum = 0;
			int i;
			for (i = curr; sum + g[i] <= k && (i != curr || sum == 0); i = (i + 1) % n){
				sum += g[i];
			}
			//cout << "new curr = " << i << endl;
			curr = i;
			ans += sum;
			ti++;
		}
		if (ti < r){
			ll per = ti - arr[curr];
			ll diff = ans - val[curr];
			assert(diff % total == 0);
			ans += (r-ti)/per*diff;
			ti += (r-ti)/per*per;
			while (ti < r){
				ll sum = 0;
				int i;
				for (i = curr; sum + g[i] <= k && (i != curr || sum == 0); i = (i + 1) % n){
					sum += g[i];
				}
				curr = i;
				ans += sum;
				ti++;
			}
		}
		cout << "Case #" << zzz << ": " << ans << endl;
	}

	return 0;
}
