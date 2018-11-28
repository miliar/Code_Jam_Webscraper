#include <cstdio>

using namespace std;

inline int gcd (int a, int b) {
    int t;
    while (b != 0) {
        t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int main () {
    int T, N;
    unsigned long long L, H;
    int tab[100];
    bool bflag, flag;
    
    scanf ("%d", &T);
    for (int t = 1; t <= T; ++t) {
        printf ("Case #%d: ", t);
        scanf ("%d %llu %llu", &N, &L, &H);
        for (int n = 0; n < N; ++n) {
            scanf ("%d", tab + n);
        }
        bflag = false;
        int i;
        for (i = L; i <= H; ++i) {
            flag = true;
            for (int n = 0; n < N; ++n) {
                if (tab[n] % i && i % tab[n]) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                bflag = true;
                break;
            }
        }
        if (bflag) {
            printf ("%d\n", i);
        } else {
            puts ("NO");
        }
    }
    return 0;
}
