#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int i, h, t, a1, a2, n, j, a[20000];
bool f;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> t;
    for (h = 1; h <= t; ++h) {
        cin >> n >> a1 >> a2;
        for (i = 1; i <= n; ++i)
            cin >> a[i];
        cout << "Case #" << h << ": ";
        for (i = a1; i <= a2; ++i) {
            f = true;
            for (j = 1; j <= n; ++j)
                if (a[j] % i != 0 && i % a[j] != 0)
                    f = false;
            if (f) {
                cout << i << endl;
                break;
            }
        }
        if (!f) cout << "NO\n";
    }

    return 0;
}
