#include <iostream>
#include <cstdio>
using namespace std;

int t, n;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        cin >> n;
        int res = 0, sum = 0, mn = -1, nw;
        while (n--) {
              cin >> nw;
              res ^= nw;
              sum += nw;
              if (mn == -1 || nw < mn) mn = nw;
        }
        cout << "Case #" << tc << ": ";
        if (res) cout << "NO\n";
        else cout << sum - mn << endl;
    }
    return 0;
}
