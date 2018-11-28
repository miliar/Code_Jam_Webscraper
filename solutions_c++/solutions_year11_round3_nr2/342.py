#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;

long long x[1001000];
long long y[1001000];

void solve()
{
    int l, n, c;
    long long t;
    
    cin >> l >> t >> n >> c;
    for(int i = 0; i < c; i++) {
        cin >> y[i];
    }
    long long sum = 0;
    long long ny;
    long long xny;
    
    long long ans = 0;
    for(int i = 0, j = 0; i < n; i++) {
        ny = y[j] * 2;
        sum += y[j] * 2;
        ans += y[j] * 2;
        j++;
        if (j == c)j = 0;
        
        if (sum >= t) {
            xny = sum - t;
            if (xny > ny)xny = ny;
            x[i] = xny / 2;
        } else {
            x[i] = 0;
        }
    }
    sort(x, x + n);
    for(int i = n -1; i >= n - l; i--) {
        ans -= x[i];
    }
    cout << ans << endl;
}
 
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    
    for (int i = 1; i <= T; i++)
    {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
