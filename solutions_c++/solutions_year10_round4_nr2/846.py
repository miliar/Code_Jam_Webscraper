#include <stdio.h>
#include <string.h>

int a[1000000];
bool u[1000000];

int sum, ans;

void find(int i, int val)
{
    if(u[i])
        ++sum;
    if(i == 1) {
        if(sum < val) {
            if(!u[i]) {
                u[i] = true;
                ++sum;
                ++ans;
            }
        }
        return;
    }
    else {
        find(i / 2, val);
        if(sum < val) {
            if(!u[i]) {
                u[i] = true;
                ++sum;
                ++ans;
            }
        }
    }
}

int main()
{
    int T, n, i, t, re = 1;
    freopen("B-small-attempt1.in.txt", "r", stdin);
    freopen("out1.txt", "w", stdout);
    scanf("%d", &T);
    while(T--) {
        memset(u, false, sizeof(u));
        scanf("%d", &n);
        for(i = 1; i <= (1 << n); ++i) {
            scanf("%d", &a[i]);
        }
        ans = 0;
        for(i = 1; i <= (1 << n); ++i) {
            sum = 0;
            find((1 << n) - 1 + i, n - a[i]);
        }
        for(i = 1; i < (1 << n); ++i)
            scanf("%d", &t);
        printf("Case #%d: %d\n", re++, ans);
    }
    return 0;
}
