#include <stdio.h>
#include <algorithm>

using namespace std;

int n;
int a[10000],b[10000],c[10000];

struct node {
    int where, type;
    } data[20000];
int dp;

bool operator < (const node& a, const node& b) {
    return a.where < b.where || a.where == b.where && a.type < b.type;
    }

int main () {
    int ct = 0, t;
    
    freopen("a2.in", "r", stdin);
    freopen("a2.out", "w", stdout);
    
    for (scanf("%d", &t); t > 0; t --) {
        scanf("%d", &n);
        for (int i = 0; i < n; i ++)
            scanf("%d%d%d", a + i, b + i, c + i);
        int ans = 0;
        for (int i = 0; i <= 10000; i ++) {
            int re = 0;
            dp = 0;
            for (int j = 0; j < n; j ++)
                if (a[j] <= i && b[j] <= 10000-i-c[j]) {
                    data[dp].where = b[j];
                    data[dp].type = 0;
                    dp ++;
                    data[dp].where = 10000-i-c[j];
                    data[dp].type = 1;
                    dp ++;
                    }
//            if (dp != 0)printf("i = %d, dp = %d\n", i, dp);
            sort(data, data + dp);
//            for (int j = 0; j < dp; j ++)
//                printf("%d,%d  ",data[j].where, data[j].type);
//            printf("\n");
            for (int j = 0; j < dp; j ++) {
                if (data[j].type == 0)
                    re ++;
                else
                    re --;
                ans >?= re;
                }
            }
        printf("Case #%d: %d\n", ++ ct, ans);
        }
   
    return 0;
    }
