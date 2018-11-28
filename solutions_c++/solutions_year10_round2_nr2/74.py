#include <cstdio>

int C,N,K,B,T,x[50],v[50];

int main() {
    int i,j,cas=1,ans=0,cnt=0;

    scanf("%d", &C);
    while(C--) {
        scanf("%d%d%d%d", &N, &K, &B, &T);
        for(i=0; i<N; i++)
            scanf("%d", &x[i]);
        for(i=0; i<N; i++)
            scanf("%d", &v[i]);
        ans = 0;
        cnt = 0;
        for(i=N-1; i>=0; i--) {
            if(v[i]*T < B-x[i])
                cnt++;
            else {
                ans += cnt;
                K--;
                if(K == 0)
                    break;
            }
        }
        printf("Case #%d: ", cas++);
        if(K > 0)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", ans);
    }
    return 0;
}

