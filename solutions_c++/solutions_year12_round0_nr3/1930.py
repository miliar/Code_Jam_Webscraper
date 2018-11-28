#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <map>

using namespace std;

const int INF = (~0U>>2);
const double eps = 1e-6;

#define rep(i, n) for (int i = 0; i < n; i++)
#define SZ(a) (int)(a.size())
#define foreach(i, a) for (__typeof(a.begin()) it = a.begin(); it != a.end(); it++)

int A, B;

void solve() {
    scanf("%d %d", &A, &B);
    int res = 0;
    for (int i = A; i <= B; i++) {
        int a = i;
        int dit[10], dn = 0, mod = 1;
        while (a) {
            dit[dn++] = a % 10;
            a /= 10;
            mod *= 10;
        }
        a = i;
        map<int, bool> S;
        int yes = 1;
        for (int j = dn - 1; j >= 0; j--) {
            a = (a * 10 + dit[j]) % mod;
            if (A <= a && a <= B) {
                S[a] = 1;
                if (a < i) yes = 0;
            }
        }
        if (yes && SZ(S) > 1) {
            //printf("%d\n", i);
            res += (SZ(S) - 1) * SZ(S) / 2;
        }
    }
    printf("%d\n", res);
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int testN;
    scanf("%d", &testN);
    for (int i = 1; i <= testN; i++) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
