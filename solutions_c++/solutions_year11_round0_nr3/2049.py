#include <stdio.h>

int main() {
    int m[1000], t;
    int n, caso, i, sumXor, sum, min;

    scanf("%d", &n);
    for(caso=1;caso<=n;caso++) {
        scanf("%d", &t);
        sumXor = 0;
        sum = 0;
        min = 1000001;

        for(i=0;i<t;i++) {
            scanf("%d", &m[i]);
            sumXor = sumXor ^ m[i];
            sum += m[i];
            if(min>m[i]) min = m[i];
        }

        if(sumXor != 0)
            printf("Case #%d: NO\n", caso);
        else
            printf("Case #%d: %d\n", caso, sum - min);
    }

    return 0;
}
