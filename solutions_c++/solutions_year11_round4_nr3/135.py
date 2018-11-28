#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

const int N = 1000000;
int a[N], su[N];

int main() {
    int tt, cas, tot = 0; long long n;
    for (int i = 0; i < N; i ++) a[i] = true;
    for (int i = 2; i < N; i ++) if (a[i])
        for (int j = i + i; j < N; j += i) a[j] =false;
    for (int i = 2; i < N; i ++)
        if (a[i]) su[tot ++] = i;
    cin >> tt;
    for (cas = 1; cas <= tt; cas ++) {
        cin >> n;
        int ans = (n == 1 ? 0 : 1);
        for (int i = 0; i < tot; i ++) {
            long long t = (long long)su[i];
            int cnt = 0;
            while (t <= n / su[i]) {
                cnt ++; t *= su[i];
            }
            if (cnt == 0) break;
            ans += cnt;
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}

