#include <cstdio>
#include <cstdlib>
#include <string>

using namespace std;

int t, r, c, n;
int g[1000];
long long ans;

int main()
{
    int i, j, ptr, cnt, group_cnt;
    
    scanf("%d", &t);
    for (i = 0; i < t; i++) {
        scanf("%d %d %d", &r, &c, &n);
        for (j = 0; j < n; j++)
            scanf("%d", g + j);
        ans = 0;
        ptr = 0;
        for (j = 0; j < r; j++) {
            cnt = 0;
            group_cnt = 0;
            while (cnt + g[ptr] <= c && group_cnt < n) {
                cnt += g[ptr];
                ptr = (ptr + 1) % n;
                group_cnt++;
            }
            ans += cnt;
            if (ptr == 0)
                break;
        }
        if (j < r) {
            int jj = j + 1;
            long long _ans = ans;
            while (j + jj < r) {
                j += jj;
                ans += _ans;
            }
            for (j++ ; j < r; j++) {
                cnt = 0;
                group_cnt = 0;
                while (cnt + g[ptr] <= c && group_cnt < n) {
                    cnt += g[ptr];
                    ptr = (ptr + 1) % n;
                    group_cnt++;
                }
                ans += cnt;
            }    
        }
        printf("Case #%d: %I64d\n", i + 1, ans);
    }
    
    return (0);
}

    
