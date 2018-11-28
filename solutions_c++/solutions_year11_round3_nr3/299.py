#include <cstdio>
#include <cstdlib>

int note[111];

int main(void) {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int i, j, L, H, N, t, T;

    scanf("%d", &T);

    for (t=1; t<=T; t++) {
        scanf("%d %d %d", &N, &L, &H);

        for (i=1; i<=N; i++) {
            scanf("%d", &note[i]);
        }

        for (i=L; i<=H; i++) {
            for (j=1; j<=N; j++) {
                if ( i%note[j] && note[j]%i ) break;
            }
            if ( j > N ) break;
        }

        printf("Case #%d: ", t);
        if ( i > H ) printf("NO\n");
        else printf("%d\n", i);
    }

    return 0;
}

