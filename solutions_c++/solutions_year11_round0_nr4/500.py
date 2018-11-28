#include <cstdio>

int main() {
    int t, T;
    scanf("%d", &T);
    for (t = 1; t <= T; t++) {
        int n;
        int i;
        int ans = 0;
        int temp;
        
        scanf("%d", &n);
        for (i = 0; i < n; i++) {
            scanf("%d", &temp);
            ans+=(temp-1 != i);
        }
        
        printf("Case #%d: %lf\n", t, double(ans));
    }
}
            
        
