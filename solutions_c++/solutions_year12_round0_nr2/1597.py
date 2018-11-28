#include <iostream>
#include <cstdio>
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

const int INF = 2147483647;
const double EPS = 0.0000001;
const int MOD = 295075153;

using namespace std;

int main() {
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	int q;
	cin >> q;
	for(int t = 1; t <= q; ++t) {
        int n, s, p, ans = 0;
        cin >> n >> s >> p;
        vector <int> A(n);
        for(int i = 0; i < n; ++i)
            cin >> A[i];

        for(int i = 0; i < n; ++i)
            if(A[i] >= p * 3 - 2)
                ++ans;
            else if(A[i] >= p * 3 - 4 && s > 0 && p > 1) {
                ++ans;
                --s;
            }

        cout << "Case #" << t << ": " << ans << endl;
	}

	return 0;
}
