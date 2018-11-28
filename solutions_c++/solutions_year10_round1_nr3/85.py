#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

const int maxn = 1000000 + 5;
const double S = (sqrt(5.0) - 1) / 2.0;

int L[maxn], R[maxn], len[maxn], spec[maxn];

int inter(int a, int b, int c, int d) {
    int l = max(a, c);
    int r = min(b, d);
    return ((l > r) ? 0 : r - l + 1);
}
int main() {
    for(int i = 1; i <= 1000000; i ++)
        spec[i] = (int)(i * S);

    L[1] = len[1] = 1;
    for(int i = 2; i <= 1000000; i ++) {
        len[i] = len[i - 1] + 1;
        L[i] = L[i - 1] + ((spec[i] == spec[i - 1]) ? 0 : 1);
    }

    for(int i = 1; i <= 1000000; i ++)
        R[i] = L[i] + len[i] - 1;
    
    freopen("C-large.in", "r", stdin);
    int T, test = 1;
    long long res;

    for(scanf("%d", &T); T; T --) {
        int a, b, c, d;

        scanf("%d%d%d%d", &a, &b, &c, &d);
        res = (long long)(b - a + 1) * (long long)(d - c + 1);
        for(int i = a; i <= b; i ++)
           res -= inter(c, d, L[i], R[i]); 

        cout << "Case #" << test ++ << ": " << res << endl; 
    }

    return 0;
}

