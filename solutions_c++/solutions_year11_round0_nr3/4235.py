#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>

#define all(x) (x).begin(), (x).end()

typedef long long int64;

using namespace std;

int main() {
    freopen ("input.txt", "rt", stdin);
    freopen ("output.txt", "wt", stdout);
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        int t;
        cin >> t;
        vector <int> a(t);
        int sum = 0, res = 0;;
        for (int j = 0; j < t; ++j) {
            cin >> a[j];
            sum += a[j];
            res = res ^ a[j];
        }
        if (res != 0) {
            cout << "Case #" << i + 1 << ": NO" << endl;
            continue;
        }
        sort(all(a));
        cout << "Case #" << i + 1 << ": " << sum - a[0] << endl;
    }
    //int x;
    //cin >> x;
    return 0;
}
