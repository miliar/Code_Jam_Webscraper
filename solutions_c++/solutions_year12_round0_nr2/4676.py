#include <iostream>
using namespace std;

main() {
	int tc, n, s, p, x, cur;
	cin >> tc;
	for(int t = 1; t <= tc; ++t) {
		int ans = 0;
		cin >> n >> s >> p;
		while(n--) {
			cin >> x;
			if(x < 2) cur = x;
			else if(x > 28) cur = 10;
			else {
				int mod = x % 3;
				cur = x / 3 + (mod > 0);
				if(!(mod & 1) && s && cur == p - 1) {
					++cur;
					--s;
				}
			}
			if(cur >= p) ++ans;
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
