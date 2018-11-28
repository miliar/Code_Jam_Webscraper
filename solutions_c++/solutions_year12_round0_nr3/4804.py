// Michal Lazowik

#include <cstdio>
#include <cstdlib>
#include <cstring>

const int MAX = 1000;
const int LEN = 11;

// Function taken from "Algorytmika praktyczna" (Piotr Stanczyk)
bool cycEq(const char *s1, const char *s2) {
    int n = strlen(s1), i = 0, j = 0, k = 0;
    
    while (i < n && j < n && k < n) {
        k = 1;
        while (k <= n && s1[(i + k) % n] == s2[(j + k) % n])
            k++;
        if (k <= n)
            if (s1[(i + k) % n] > s2[(j + k) % n])
                i += k;
            else j += k;
    }
    
    return k > n;
}

long long comp(int a, int b) {
    long long wyn = 0;
    char one[LEN], two[LEN];

    for (int i = a; i <= b; i++) {
        for (int j = a; j < i; j++) {
            sprintf(one, "%d", i);
            sprintf(two, "%d", j);
            // itoa(i, one, 10);
            // itoa(j, two, 10);
            if (cycEq(one, two))
                wyn++;
        }
    }

    return wyn;
}

int main() {
    int q, a, b;

    scanf("%d", &q);
    for (int i = 0; i < q; i++) {
        scanf("%d%d", &a,&b);
        printf("Case #%d: %lld\n", i+1, comp(a, b));
    }

    return 0;
}
