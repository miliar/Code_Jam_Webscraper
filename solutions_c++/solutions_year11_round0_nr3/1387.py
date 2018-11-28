#include <iostream>
#include <stdio.h>
#include <string.h>
#include <map>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

int main() {
    freopen("C-large.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int tt;
    cin >> tt;
    for (int ii = 1; ii <= tt; ii++) {
        int n;
        int a[1010];
        cin >> n;
        for (int i = 0; i < n; i++)
            cin >> a[i];
        int chans = 0;
        for (int i = 0; i < n; i++)
            chans ^= a[i];
        if (chans != 0) {
            cout << "Case #" << ii << ": " << "NO" << endl;
            continue;
        }
        int minval = 200000;
        int res = 0;
        for (int i = 0; i < n; i++) {
            res += a[i];
            minval = min(minval, a[i]);
        }
        cout << "Case #" << ii << ": " << res-minval << endl;
    }
    return 0;
}
