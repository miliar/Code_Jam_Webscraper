#include<stdio.h>

int T, N, a[100], i, j, k, x, y, cas, ans;
char s[100];

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    scanf("%d", &T);
    for (cas = 1; cas <= T; cas ++){
        scanf("%d", &N);
        for (i=0; i<N; i++){
            a[i] = 0;
            scanf("%s", s);
            for (j=0;j<N;j++)
               if (s[j] == '1') a[i] = j;
        }
        ans = 0;
        while (true){
            //for (i=0; i<N; i++) printf("a[%d] = %d\n", i, a[i]);
            
            for(i=0;i<N;i++)
               if (a[i] > i) break;
            if (i >= N) break;
            x = i;
            while (true){
                while (x < N && a[x+1] <= x){
                    y = a[x+1];
                    a[x+1] = a[x];
                    a[x] = y;
                    x++;
                    ans++;
                    //for (i=0; i<N; i++) printf("1 a[%d] = %d\n", i, a[i]);
                    if (x < N && a[x] <= x) break;
                }
                if (a[x] <= x || x >= N) break;
                y = x;
                while (y < N && a[y] > x) y++;
                ans += (y-x);
                k = a[y];
                for (i=y;i>x;i--) a[i] = a[i-1];
                a[x] = k;
                //for (i=0; i<N; i++) printf("2 a[%d] = %d\n", i, a[i]);
                x = y;
                if (a[x] <= x || x >= N) break;
            }
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
    
    
}
