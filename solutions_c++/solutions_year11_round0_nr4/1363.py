#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
using namespace std;

int f[2000];

int main() {
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    int T, t = 0;
    cin >> T;
    while (t < T) {
        printf("Case #%d: ", ++t);
        int n;
        cin >> n;
        int ans = 0, val;
        for(int i = 0; i < n; i++){
            cin >> val;
            if (val != (i + 1))
            ++ans;
        }
        cout << ans << endl;
    }
    return 0;
}


