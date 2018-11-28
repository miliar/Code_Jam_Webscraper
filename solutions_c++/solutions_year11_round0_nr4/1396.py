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


const int maxn = 120;
int dp[maxn][maxn][maxn];

int main() {
    int t, n, now, x, sum, minf, a;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> n;
        int res = 0;
        for (int j = 1; j <= n; ++j) {
            cin >> a; 
            if (j != a) ++res;
        }
        cout << "Case #" << i << ": " << res << ".000000\n";
    }
}
