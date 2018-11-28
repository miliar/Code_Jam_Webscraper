#include <cstdio>

int main() {
    int t, T;
    scanf("%d", &T);
    for (t = 1; t <= T; t++) {
        int n, total = 0, xxor = 0, min = 1000001;
        int i;
        int temp;
        scanf("%d", &n);
        for (i = 0; i < n; i++) {
            scanf("%d", &temp);
            xxor^=temp;
            if (temp < min)
                min = temp;
            total+=temp;
        }
        printf("Case #%d: ", t);
        if (xxor)
            printf("NO\n");
        else
            printf("%d\n", total-min);
    }
}
        
