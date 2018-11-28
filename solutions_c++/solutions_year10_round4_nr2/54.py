#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

#define tiao system("pause")

int p;
int t[11111];
long long f[11111][50];
int T;
int cost[11111];
int all;
const long long inf = 123456789123LL;

long long dp(int n, int k)
{
    if (n <= (1 << p))
    {
        if (k >= t[n]) return 0;
        else return inf;
    }    
    
    if (f[n][k] != -1) return f[n][k];
    
    int left = all - ((all - n) * 2 + 1);
    int right = all - ((all - n) * 2);
    
    return f[n][k] = min(dp(left, k) + dp(right, k), 
                        dp(left, k+1) + dp(right, k+1) + t[n]);
}

int main(void)
{
//    freopen("B-small-attempt0.in", "r", stdin);
//    freopen("B-small-attempt0.out", "w", stdout);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
      
    int i,j,k,ci,cici,cicici;
    
    scanf("%d", &T);
    for (cicici=1; cicici<=T; cicici++)
    {
        scanf("%d", &p);
        
        for (i=1; i<(1<<(p+1)); i++)
        {
            scanf("%d", &t[i]);
            if (i <= (1 << p)) t[i] = p - t[i];
        }
        all = 1 << (p + 1) ;
        memset(f, -1, sizeof(f));        
        
        cout << "Case #" << cicici << ": " << dp(all-1, 0) << '\n';
//        printf("Case #%d: %d\n", cicici, dp(all-1, 0));
    }    
//    tiao;
    return 0;
}
