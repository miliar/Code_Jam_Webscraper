#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

int t, x, ans, sum, mini;

int main() {
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    scanf("%d", &t);
    int xx = 1;
    while (t--) {
        ans = 0;
        mini = (int)1e9;
        sum = 0;
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &x);
            ans = ans ^ x;
            mini = min(mini, x);
            sum += x;
        }
        printf("Case #%d: ", xx++);
        if (ans != 0) printf("NO\n");
        else printf("%d\n", sum - mini);
    }
    return 0;
}
