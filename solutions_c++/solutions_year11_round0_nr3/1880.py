#include <cstdio>
#include <iostream>
#include <queue>
#include <string>
#include <algorithm>

using namespace std;

int n, f[1002];

void solve() {
    sort(f, f+n);
    int tor = f[0], sum = 0;
    for (int i=1; i<n; i++) {
        tor ^= f[i];
        sum += f[i];
    }
    if (tor == 0)
        printf("%d\n", sum);
    else
        puts("NO");
}

int main() {
    
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    
    int cas, T = 1;
    scanf("%d", &cas);
    while (cas --) {
        scanf("%d", &n);
        for (int i=0; i<n; i++)
            scanf("%d", &f[i]);
        printf("Case #%d: ", T++);
        solve();
    }
    return 0;
}
