#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
#include <queue>
#include <ctime>
#include <deque>
#include <stack>
#include <set>

const int INF = 2147483647;
const double EPS = 0.0000001;
const int MOD = 295075153;

using namespace std;

void itoa(int ans, char *buf) {
    int len = 0;
    while(ans > 0) {
        buf[len++] = ans % 10 + '0';
        ans /= 10;
    }
    buf[len] = 0;
    reverse(buf, buf + len);
}

int main() {
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	int q;
	cin >> q;
	for(int t = 1; t <= q; ++t) {
        int a, b, ans, len;
        long long res = 0;
        cin >> a >> b;
        for(int i = a; i < b; ++i) {
            set <int> W;
            char buf[32], newbuf[32];
            itoa(i, buf);
            len = strlen(buf);
            strcpy(newbuf, buf);
            for(int j = 0; j < len - 1; ++j) {
                rotate(newbuf, newbuf + 1, newbuf + len);
                ans = atoi(newbuf);
                if(ans > i && ans <= b && W.find(ans) == W.end()) {
                    ++res;
                    W.insert(ans);
                }
            }
        }

        cout << "Case #" << t << ": " << res << endl;
	}

	return 0;
}
