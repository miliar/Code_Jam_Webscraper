#include <vector>
#include <cstdio>
#include <iostream>
#include <map>
using namespace std;
const int MAXN = 11111;
int a[MAXN];
int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int n, s, t;
	int T;
	cin >> T;
	for (int cas = 1; cas <= T; cas++) {
		cin >> n >> s >> t;
		for (int i = 0; i < n; i++) {
			cin >> a[i];
        }
		int ans = 0;
		for (int i = 0; i < n; i++) {
			if (t == 0 && a[i] >= 0) {
                ans++;
			} else if (t == 1 && a[i] > 0) {
                ans++;
            } else if (a[i] > (t - 1) * 3) {
                ans++;
			} else if (t >= 2 && a[i] > (t - 2) * 3 + 1 && s > 0) {
				s--;
				ans++;
			}
		}
		printf("Case #%d: ", cas);
		cout << ans << endl;
		//cout<<"Case #"<<cas<<": "<<ans<<endl;
	}
	return 0;
}

