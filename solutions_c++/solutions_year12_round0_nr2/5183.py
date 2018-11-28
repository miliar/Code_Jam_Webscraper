#include <cstdio>

int main() {

    //freopen("Bout.txt", "w", stdout);

    int T, N, S, p, t, ans, i, j;

    scanf("%d ", &T);

    for (i = 1; i <= T; i++) {
        ans = 0;
        scanf("%d %d %d ", &N, &S, &p);

        for (j = 0; j < N; j++) {
            scanf("%d ", &t);
            if (t >= 3*p-2) {
                ans++;
            }
            else if (t >= 3*p-4 && t>2 && S>0) {
                S--; ans++;
            }
        }//end for

        printf("Case #%d: %d\n", i, ans);

    }//end for

    return 0;
}//end main
