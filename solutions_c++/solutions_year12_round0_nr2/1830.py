#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <bitset>
#include <cstdio>
#include <queue>

using namespace std;

__int64 ans, n, s, p;

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
		ans = 0;
		cin >> n >> s >> p;
        vector <int> t(n);
        for (int i = 0; i < n; ++i) {
            cin >> t[i];
        }

        for (int i = 0; i < n; ++i) {
            int a, b, c;
            a = b = c = t[i] / 3;
            if (t[i] % 3 > 0)
                ++a;
            if (t[i] % 3 > 1)
                ++b;

            if (a >= p) {
                ++ans;
            } else {
                if (s > 0 && a + 1 >= p && a + 1 <= 10) {
                    if (t[i] % 3 == 0 && b > 0) {
                        ++ans;
                        --s;
                    } else
                    if (t[i] % 3 == 2 && b > 0) {
                        ++ans;
                        --s;
                    }
                }
            }
        }
		
		cout << "Case #" << test << ": " << ans << endl;
	}
	return 0;
}