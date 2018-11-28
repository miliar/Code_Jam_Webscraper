#include <stdio.h>

int d[1000001];

int A1, A2, B1, B2;

void initialize() {
    d[1] = 1;
    d[2] = 2;
    for (int i = 2, last = 3; i <= 1000000; i++) {
        while (last <= 1000000 && last < d[i] + i) {
            d[last++] = i;
        }
    }
}

long long solve(int x, int y) {
    if (x == 0 || y == 0) {
        return 0;
    }
    long long result = 0;
    for (int i = 1; i <= x; i++) {
        int Min = d[i], Max = d[i] + i - 1;
        if (y < Min) {
            result += y;
        } else {
            result += Min - 1;
        }
        if (y > Max) {
            result += y - Max;
        }
    }
    return result;
}

int main() {
    int caseSize;
    scanf("%d", &caseSize);
    initialize();
    for (int T = 1; T <= caseSize; T++) {
        scanf("%d%d%d%d", &A1, &A2, &B1, &B2);
        A1--;
        B1--;
        printf("Case #%d: %lld\n", T, solve(A2, B2) - solve(A2, B1) - solve(A1, B2) + solve(A1, B1));
    }
    return 0;
}
