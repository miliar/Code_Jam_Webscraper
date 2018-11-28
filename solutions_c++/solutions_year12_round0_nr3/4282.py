#include <cstdio>
#include <cstring>
using namespace std;

#define SIZE 20

static inline int is_recycled(char* n, char* m, size_t len) {
    for (int i = 1; i < len; i++) {
        if (n[i] != '0' && m[len - i] != '0' &&
                strncmp(&n[0], &m[len - i], i) == 0 &&
                strncmp(&n[i], &m[0], len - i) == 0) {
            //printf("=> n=%s, m=%s, \n", n, m);
            return 1;
        }
    }
    return 0;
}

static int solve(int A, int B) {
    if (A == B)
        return 0;

    static char n[SIZE], m[SIZE];
    size_t len;
    int count = 0;

    for (int a = A; a <= B; a++) {
        for (int b = a + 1; b <= B; b++) { // A <= n < m <= B
            sprintf(n, "%d", a);
            sprintf(m, "%d", b);
            len = strlen(n); // length of n and m is same
            count += is_recycled(n, m, len);
        }
    }

    return count;
}

int main() {
    int T, A, B;
    scanf("%d\n", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d %d\n", &A, &B);
        printf("Case #%d: %d\n", t, solve(A, B));
    }
    return 0;
}
