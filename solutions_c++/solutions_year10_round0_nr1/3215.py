#include <cstdio>
#include <cstring>

int main() {
    int T,N,K,i,cas=1;
    bool flag;

    scanf("%d", &T);
    while(T--) {
        scanf("%d%d", &N, &K);
        flag = 1;
        for(i=0; i<N; i++)
            if((K & 1 << i) == 0)
                flag = 0;
        printf("Case #%d: ", cas++);
        if(!flag)
            printf("OFF\n");
        else
            printf("ON\n");
    }
    return 0;
}
