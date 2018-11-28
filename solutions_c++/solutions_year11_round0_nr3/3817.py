#include <iostream>
#include<cstdio>
#include<cstring>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
 //   freopen("C-small-attempt0.in", "r", stdin);
  //  freopen("out.txt", "w", stdout);
    int cas;
    scanf("%d", &cas);
    for (int i = 0; i < cas; i++) {
        int n;
        int minn = 1000010;
        int sum = 0;
        int total = 0;
        scanf("%d", &n);
        for (int j = 0; j < n; j++) {
            int t;
            scanf("%d", &t);
            sum ^= t;
            minn = min(minn, t);
            total += t;
        }
        if (sum == 0)
            printf("Case #%d: %d\n", i + 1, total - minn);
        else printf("Case #%d: NO\n", i + 1);
    }
    return 0;
}
