#include <iostream>

int T, N, C[1050];
bool cmp(int a, int b) { return a>b; }
int highbit(int a) {
    for (int i=25;i>=0;i--) {
        if (((1<<i)&a)!=0)
            return i;
    }
    return 0;
}
int main () {
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);

    scanf("%d", &T);
    for (int t=1;t<=T;t++) {
        scanf("%d", &N);
        for (int i=0;i<N;i++)
            scanf("%d", &C[i]);
        int A = 0, B = 0, aa, bb, mm = -1;
        for (int s=1;s<(1<<N)-1;s++) {
            A = 0, B = 0, aa = 0, bb = 0;
            for (int i=0;i<N;i++) {
                if (((1<<i)&s)!=0) aa += C[i], A ^= C[i];
                else bb+= C[i], B ^= C[i];
            }
            if (A == B && aa> mm) {
                mm = aa;
            }
        }
        if (mm == -1) {
            printf ("Case #%d: NO\n", t);
        } else {
            printf ("Case #%d: %d\n", t, mm);
        }
    }
}
