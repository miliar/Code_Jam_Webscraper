#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <bitset>
#include <functional>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>

#include <ext/numeric>
#include <ext/functional>

using namespace std;
using namespace __gnu_cxx;

int n;
int a[16];

int main() {
    int ts;
    cin >> ts;
    for (int tc = 1; tc <= ts; ++tc) {
        cin >> n;
        int res = -1;
        for (int i = 0; i < n; ++i) cin >> a[i];
        for (int i = 1; i < (1 << n); ++i) {
            int xors[2];
            xors[0] = 0;
            xors[1] = 0;
            int sum = 0;
            for (int k = 0; k < n; ++k) {
                int b = (i >> k) & 1;
                xors[b] ^= a[k];
                if (!b) sum += a[k];
            }
            if (xors[0] == xors[1] && sum > res) res = sum;
        }
        cout << "Case #" << tc << ": ";
        if (res == -1) cout << "NO" << endl;
        else cout << res << endl;
    }


    return 0;
}