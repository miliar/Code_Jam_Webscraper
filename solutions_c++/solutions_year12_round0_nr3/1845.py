#include <stdio.h>

void dotest(int numtest) {
    int A, B;
    scanf("%d %d", &A, &B);
    int res = 0;
    int pow10 = 1;
    int t = A;
    while(t>=10) {
        t/=10;
        pow10*=10;
    }
    for(int i = A; i<=B; i++) {
        int x = i;
        while(true) {
            x = (x/10) + (x%10) * pow10;
            if (x==i) break;
            if(x>i && x<=B) res++;
        }
    }
    printf("Case #%d: %d\n", numtest, res);
}

int main() {
    int T;
    scanf("%d", &T);
    for(int i = 0; i<T; i++) {
        dotest(i+1);
    }
    return 0;
}

