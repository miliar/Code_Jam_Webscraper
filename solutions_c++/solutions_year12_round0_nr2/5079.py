#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int T;
int n, m, p, t[11];
int ans;

void rec(int l, int M, int cans) {
    if (l == n) {
        if (M != m) return;
        ans = max(ans, cans);
        return;
    }
    
    for (int i = 0; i <= t[l]; ++i)
        for (int j = i; j <= i + 2; ++j) {
            int k = t[l] - i - j;
            if (k < j) continue;
            if (k > i + 2) continue;
            
            int add = 0;
            if (k >= p) add = 1;
            
            if (i + 2 == k) rec(l + 1, M + 1, cans + add);
            else rec(l + 1, M, cans + add); 
        }
}

int main() {
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    
    cin >> T;
    for (int nT = 1; nT <= T; ++nT) {
        cin >> n >> m >> p;
        for (int i = 0; i < n; ++i) cin >> t[i];
        ans = 0;
        rec(0, 0, 0);
        
        printf("Case #%d: %d\n", nT, ans);
    }
    
    return 0;
}
