#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>
using namespace std;

int main() {
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tot, n, w, s, num = 0;
    scanf("%d", &tot);
    while (num < tot) {
        ++num;
        scanf("%d%d%d", &n, &s, &w);
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            int val;
            scanf("%d", &val);
            if (val > (w-1)*3)  ++ans;
            else if (val >= (w-2)*3+2 && val >= w) {
                if (s > 0) {
                    --s;
                    ++ans;
                }
            }
        }
        printf("Case #%d: %d\n", num, ans);
    }
}
