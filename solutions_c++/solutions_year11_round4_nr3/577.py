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
typedef vector<pii> vii;

bool mless (long long x, int pn, long long n) {
    long long res = 1;
    for (int i = 0; i < pn; ++i) {
        res *= x;
        if (res > n)
            return false;
    }
    return true;
}

int main() {
    vector<char> erat(1e6, 1);
    erat[0] = erat[1] = 0;
    for (int i = 0; i * i < erat.size(); ++i) if (erat[i]) {
        for (int j = i * i; j < erat.size(); j += i)
            erat[j] = 0;
    }
    vi num(erat.size());
    for (int i = 1; i < num.size(); ++i)
        num[i] = num[i - 1] + erat[i];
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        long long n;
        cin >> n;
        cout << "Case #" << test << ": ";
        if (n == 1) {
            cout << 0 << endl;
            continue;
        }
        long long cnt = 1;
        for (int i = 2; i <= 65; ++i) {
            int x = pow((double)n, 1. / (double)i);
            while (!mless(x, i, n))
                --x;
            while (mless(x + 1, i, n))
                ++x;
            cnt += num[x];
        }
        cout << cnt << endl;
    }
    return 0;
}
