#include<iostream>
#include <cstring>
#include <stdio.h>
#include <cmath>
#include <iomanip>
using namespace std;

const int maxn = 10100;
int d[maxn], l[maxn], f[maxn];
int D;
int T, n;

void solve()
{
        f[0] = d[0];
        for (int i = 0; i < n; ++i) {
            int range = d[i] + f[i];
            for (int j = i + 1; j < n && range >= d[j]; j++) {
                f[j] = max(f[j],min(d[j] - d[i], l[j]));
            }
        }
        bool ans = false;
        for (int i = n - 1;i >= 0; --i) {
            if (d[i] + f[i] >= D) {
                ans = true;
                break;
            }
        }
        if (ans) cout<<"YES";
            else cout<<"NO";

}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin >> T;
    for (int test = 1; test <= T; test++) {
        cout << "Case #" << test << ": ";
        memset(f, 0, sizeof (f));
        cin>>n;
        for(int i = 0; i < n; i++)
            cin>>d[i]>>l[i];
        cin>>D;
        
        solve();
        
        cout << endl;
    }
    return 0;
}
