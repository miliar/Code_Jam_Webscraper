#include <stdio.h>

int main() {
    int numtest, n, k;
    scanf("%d", &numtest);
    for (int i=1; i<=numtest; i++) {
        scanf("%d %d", &n, &k);
        printf("Case #%d: %s\n", i, ((k+1)%(1<<n)==0 ? "ON": "OFF"));
    }
    return 0;
}
