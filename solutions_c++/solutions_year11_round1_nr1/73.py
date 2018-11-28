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

const int maxn = 121, maxp = 21;
string s;

int main() {
    int v = 0, i, t;
    bool a;
    ll n, d, g;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> n >> d >> g;
        if (!d && !g) a = 1;
        else if (d != 100 && g == 100) a = 0;
        else if (!d && g) a = 1;
        else if (d && !g) a = 0;
        else a = (100 / __gcd(d, 100ll) <= n);
        cout << "Case #" << i << ": " << (a ? "Possible" : "Broken") << endl;
    }
}
