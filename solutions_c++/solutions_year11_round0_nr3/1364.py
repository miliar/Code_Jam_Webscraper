#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
using namespace std;

int f[2000];

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int T, t = 0;
    cin >> T;
    while (t < T) {
        printf("Case #%d: ", ++t);
        int n;
        cin >> n;
        for(int i = 0; i < n; i++)
            cin >> f[i];
        long long sum = f[0];
        for(int i = 1; i < n; i++) sum ^= f[i];
        if (sum == 0) {
            sort(f, f + n);
            for(int i = 1; i < n; i++) {
                sum = sum + f[i];
            }
            cout << sum << endl;
        } else printf("NO\n");
        
    }
    return 0;
}

