#include <stdio.h>
#include <string.h>

#define NMAX 128

int n, s, p;
int A[NMAX];

int main() {
    int tests;
    scanf("%d", &tests);
    for (int test = 1; test <= tests; test++) {
        scanf("%d %d %d", &n, &s, &p);
        for (int i = 0; i < n; i++) {
            scanf("%d", A+i);
        }
        int output = 0;
        for (int i = 0; i < n; i++) {
            if ((A[i] + 2) / 3 >= p) {
                output++;
            } else if (s) {
                if (A[i] != 0 && (A[i] + 4) / 3 >= p) {
                    output++;
                    s--;
                }
            }
        }
        printf("Case #%d: %d\n", test, output);
    }
    return 0;
}

