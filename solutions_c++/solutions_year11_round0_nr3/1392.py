#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

#define mp make_pair
#define pb push_back
#define ll long long
#define mp make_pair



int main() {
    int t, n, now, xo, a, sum, minf;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> n;
        now = 0, xo = 0, sum = 0, minf = 20000000;
        for (int j = 0; j < n; ++j) {
            cin >> a;
            sum += a;
            minf = min(minf, a);
            xo ^= a;
        }        
        cout << "Case #" << i << ": ";
        if (xo) cout << "NO\n"; else 
           cout << sum - minf << endl;
    }
}
