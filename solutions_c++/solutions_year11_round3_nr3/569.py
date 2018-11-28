#include <cstdio>
#define MaxN 10010


int T;
int N, L, H;
int a[MaxN];


int main () {
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    scanf("%d\n", &T);
    
    for (int xxx = 1; xxx <= T; xxx++) {
        scanf("%d%d%d\n", &N, &L, &H);
        for (int i = 0; i < N; i++)
            scanf("%d", &a[i]);
            
        bool found = false;
        int ats = 0;
            
        for (int i = L; i <= H && !found; i++) {
            bool good = true;
            for (int j = 0; j < N && good; j++) {
                if (a[j] % i != 0 && i % a[j] != 0)
                    good = false;
            }
            if (good) {
                found = true;
                ats = i;
            }
            
        }
        if (found)
            printf("Case #%d: %d\n", xxx, ats);
        else
            printf("Case #%d: NO\n", xxx);
    }
    return 0;    
}
