#include <cstdio>
#include <cstdlib>
#include <cassert>
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
typedef pair<double, double> pdd;

ll gcd (ll a, ll b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        ll n, p1, p2;
        cin >> n >> p1 >> p2;
        ll d1 = gcd(100, p1), d2 = gcd(100, p2);
        cout << "Case #" << test << ": ";
//        cerr << endl << d1 << " " << d2 << endl;
//        bool ok = false;
//        for (int k = 1; k <= n / (100 / d1); ++k)
//            if (!((k * p1 / d1) % (p2 / d2)))
//                ok = true;
        if (p1 > 0 && p2 == 0 || n < (100 / d1) || p2 == 100 && p1 < 100) {
            cout << "Broken\n";
        } else {
            cout << "Possible\n";
        }
    }
    return 0;
}
