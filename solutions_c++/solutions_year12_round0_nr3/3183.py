#include <stdio.h>
#include <math.h>

int recycle(int n, int rDigits, int nDigits) {
    int filter = pow(10, rDigits);
    return n / filter + ( n % filter ) * pow(10, nDigits - rDigits);
}

int doCase(int A, int B) {
    int result = 0;
    int nDigits = 0;
    for(int n=A; n > 0; n = n / 10) {
        nDigits++;
    }

    //printf("nDigits %d\n", nDigits);

    for(int i=A; i < B; i++) {
        for(int j=1; j < nDigits; j++) {
            int recycled = recycle(i, j, nDigits);
            if( i < recycled && recycled <= B ) {
                result++;
                //printf("N:%d M:%d\n", i, recycled);
            }
        }
    }

    return result;
}

int main() {
    int T;
    scanf("%d", &T);

    for(int i=0; i < T; i++) {
        int A, B;

        scanf("%d %d", &A, &B);
        printf("Case #%d: %d\n", i+1, doCase(A, B));
    }
    return 0;
}
