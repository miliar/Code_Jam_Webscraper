#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int r[1010], d[1000100], s[1000100];

int main() {
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int T, ct = 1, m, t, n, c, i, j, k, u, v, sum, max_d;
    int tmp, res, ans;
    scanf("%d",&T);
    while (T--) {
        scanf("%d %d %d %d",&m, &t, &n, &c);
        sum = 0;
        for (i = 0; i < c; ++i) {
             scanf("%d",r+i);
             
             k = 0;
             while (1) {
                 u = k * c + i;
                 v = u + 1;
                 if (0<= u && u <= n && 0<= v && v <= n) {
                     d[u] = r[i];
                     sum += d[u];
                 }
                 else break;
                 
                 k++;
             }
        }
        
        memset(s, 0, sizeof(s));
        for (i = 0; i < n; ++i) {
            if (i == 0) s[i] = d[i];
            else {
                s[i] = s[i-1] + d[i];
            } 
        }
        //printf("%d\n",sum);
        
        printf("Case #%d: ",ct++);
        if (m == 0) {
           printf("%d\n",sum * 2);
        }
        else if (m == 1) {
            ans = sum * 2;
            for (i = 0; i < n; ++i) {
                tmp = s[i] * 2; 
                if (tmp > t) {
                    if (i > 0) {
                        tmp = s[i - 1] * 2;
                        if ( tmp > t) {
                            res = tmp + d[i] + (sum - s[i]) * 2;
                        }
                        else  {
                            res = tmp + (  (t - tmp) + d[i] - 0.5 * (t - tmp)  ) + (sum - s[i]) * 2;
                        }
                    }
                    else {
                        res = ( t + d[i] - 0.5 * t) + (sum - s[i]) * 2;
                    }
                    
                    ans = min(ans, res);
                }
            }
            printf("%d\n",ans);
        }
        else if (m == 2) {
            ans = sum * 2;
            for (i = 0; i < n; ++i) {
                tmp = s[i] * 2; 
                if (tmp > t) {
                    if (i > 0) {
                        tmp = s[i - 1] * 2;
                        if ( tmp > t) {
                            res = tmp + d[i];
                        }
                        else  {
                            res = tmp + (  (t - tmp) + d[i] - 0.5 * (t - tmp)  );
                        }
                    }
                    else {
                        res = ( t + d[i] - 0.5 * t);
                    }
                    
                    max_d = -1; 
                    for (j = i + 1; j < n; ++j) {
                        if (max_d < d[j]) max_d = d[j];
                    }
                    res += ((sum - s[i]) * 2 - max_d);
                    
                    ans = min(ans, res);
                }
            }  
            printf("%d\n",ans);           
        }
    }
    return 0;
}
