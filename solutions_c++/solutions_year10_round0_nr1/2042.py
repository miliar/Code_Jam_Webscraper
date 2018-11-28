

#include <stdio.h>
int main()
{
    int T, CAS = 1;
    int N, K;
freopen("1.txt", "r", stdin);
freopen("a.out", "w", stdout);
    scanf("%d", &T);
    while(T--)
    {
        scanf("%d %d", &N, &K);
        printf("Case #%d: ", CAS++);
        K %= (1<<N);
        if(K == ((1<<N)-1))
            printf("ON\n");
        else printf("OFF\n");
    }
    return 0;
}

