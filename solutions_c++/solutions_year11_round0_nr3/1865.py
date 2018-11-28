#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <set>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <map>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<double> vd;
typedef pair<int, int> pii;

int main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        int n;
        cin >> n;
        int mi = 1e7, sum = 0, xr = 0;
        for (int i = 0; i < n; ++i) {
            int c;
            cin >> c;
            sum += c;
            mi = min(mi, c);
            xr ^= c;
        }
        cout << "Case #" << test << ": ";
        if (xr || n < 2) {
            cout << "NO\n";
        } else {
            cout << sum - mi << endl;
        }
    }
    return 0;
}
