#include<stdio.h>
#include<math.h>
#include<stdlib.h>

int B[128], R[128], x[2], tm[2];

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    
    int T, tt, n, i, ans;
    char str[10];
    
    scanf("%d", &T);
    for(tt = 1; tt <= T; tt++)
    {
        scanf("%d", &n);
        for(i = 0; i < n; i++){
            scanf("%s %d", &str, &B[i]);
            if(str[0] == 'O') R[i] = 0; else R[i] = 1;
        }
        x[0] = x[1] = 1;
        tm[0] = tm[1] = 0;
        for(i = 0; i < n; i++){
            if(i == 0 || R[i] == R[i - 1] || tm[R[i]] + abs(B[i] - x[R[i]]) + 1 > tm[R[i - 1]]){
                tm[R[i]] += abs(B[i] - x[R[i]]) + 1;
                x[R[i]] = B[i];
            }
            else{
                tm[R[i]] = tm[R[i-1]] + 1;
                x[R[i]] = B[i];
            }
        }
        ans = (tm[0] > tm[1]) ? tm[0] : tm[1];
        printf("Case #%d: %d\n", tt, ans);
    }
    
    return 0;
}
