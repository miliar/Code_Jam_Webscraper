#include <cstdio>
int p[120][2], ss, ans, p_len;

void dfs(int i, int cur_s, int sum) {
    if (i == p_len) {
        if (cur_s == ss && sum > ans) {
            ans = sum;
        }
        return ;
    }
    if (cur_s > ss) {
        return ;
    }

    
    dfs(i + 1, cur_s + 0, sum + p[i][0]);
    dfs(i + 1, cur_s + 1, sum + p[i][1]);
}


int main() {
    freopen("B-small-attempt3.in", "r", stdin);
    freopen("B-small-attempt3.out", "w", stdout);
    int ct, T, pp, x, t, r, n, res, i;
    scanf("%d",&T);
    for (ct = 1; ct <= T; ct++) {
        scanf("%d %d %d",&n, &ss, &pp);
       // printf("%d %d %d\n",n, ss, pp);
        
        res = 0;
        p_len = 0;
        for (i = 0; i < n; i++) {
            scanf("%d", &x);
           // printf("%d\n",x);
            r = x % 3;
            t = x / 3;
            if (x == 0) {
                if (pp == 0) {
                    res++;
                }   
    
                continue;
            }
            
            if (x == 1) {
                if (pp <= 1) {
                    res++;
                }
                
                continue;
            }
            
            if (r == 1) {
                if ( (t + 1) >= pp ) {
                    p[p_len][0] = 1;
                    p[p_len][1] = 1;
                }
                else {
                    p[p_len][0] = 0;
                    p[p_len][1] = 0;                
                }
            } else {

                if (r == 0) {
                   if (t >= pp) {
                       p[p_len][0] = 1;
                       p[p_len][1] = 1;
                   }
                   else  {
                        p[p_len][0] = 0;
                        if (t + 1 >= pp) {
                            p[p_len][1] = 1;
                        } else {
                            p[p_len][1] = 0;
                        }
                   }
                } else if (r == 2) {
                   if (t + 1 >= pp) {
                       p[p_len][0] = 1;
                       p[p_len][1] = 1;
                   }
                   else  {
                        p[p_len][0] = 0;
                        if (t + 2 >= pp) {
                            p[p_len][1] = 1;
                        } else {
                            p[p_len][1] = 0;
                        }
                   }
                }   
               
                
              // printf("%d %d %d %d %d %d\n",x, t, r, pp, p[p_len - 1][0],p[p_len - 1][1]);
            }     
             p_len++;     
        }
        
        ans = 0;
        dfs(0, 0, 0);
        //printf("r:%d %d\n",res, ans);
        printf("Case #%d: %d\n",ct, ans + res);
    }
    return 0;
}