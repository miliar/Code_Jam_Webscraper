#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;

long long sum[5][110];

struct thing{
    long long s;
    int p;
}a[110], b[110];

int main()
{
    int _, tt = 1;
    freopen("in.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &_);
    while(_--){
        int n, m;
        long long ans = 0, now;
        scanf("%d%d", &n, &m);
        sum[1][0] = sum[2][0] = sum[3][0] = 0;
        memset(sum, 0, sizeof(sum));
        memset(a, 0, sizeof(a));
        memset(b, 0, sizeof(b));
        for(int i = 1; i <= n; i++) scanf("%lld%d", &a[i].s, &a[i].p);
        for(int i = 1; i <= m; i++) scanf("%lld%d", &b[i].s, &b[i].p);
        if(a[1].p == a[2].p){
            a[1].s += a[2].s;
            if(n == 3){
                a[2].p = a[3].p;
                a[2].s = a[3].s;
            }
            else{
                a[2].p = 0;
                a[2].s = 0;
            }
            n--;
        }
        if(n == 3 && a[2].p == a[3].p){
            a[2].s += a[3].s;
            a[3].p = 0;
            a[3].s = 0;
            n--;
        }
        for(int i = 1; i <= m; i++){
            for(int j = 1; j <= n; j++){
                if(b[i].p == a[j].p) sum[j][i] = sum[j][i - 1] + b[i].s;
                else sum[j][i] = sum[j][i - 1];
            }
        }
        for(int i = 0; i <= m; i++){
            for(int j = i; j <= m; j++){
                long long temp = sum[1][i] - min(a[1].s, sum[1][i]);
                now = min(a[1].s, sum[1][i]) + min(a[2].s, (sum[2][j] - sum[2][i])) + min(a[3].s, (sum[3][m] - sum[3][j]));
                if(a[1].p == a[3].p && n == 3) now += max(0LL, (min((a[3].s - min(a[3].s, (sum[3][m] - sum[3][j]))), temp) - min(a[2].s, (sum[2][j] - sum[2][i]))));
                if(now > ans) ans = now;
                //printf("%d %d %lld\n", i, j, now);
            }
        }
        printf("Case #%d: %lld\n", tt++, ans);
    }
}
