#include <cstdio>

int main() {
    int T, N, K;
    scanf("%d", &T);
    for(int caso = 1; caso <= T; ++caso) {
        scanf("%d%d", &N, &K);
        printf("Case #%d: ", caso);
        if((K%(1<<N)) == ((1<<N) - 1))
            printf("ON\n");
        else
            printf("OFF\n");
    }
    return 0;
}
