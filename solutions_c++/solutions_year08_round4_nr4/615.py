#include <algorithm>
#include <cstdio>

using namespace std;

int rle(char* s) {
    int res = 0, pos = 0;
    while (s[pos] != '\0') {
        res += 1;
        do {
            pos += 1;
        } while (s[pos - 1] == s[pos]);
    }
    return res;
}

int main() {
    int N;
    scanf("%d", &N);
    for (int c = 1; c <= N; c ++) {
        int k;
        char S[50001], T[50001];
        scanf("%d %s", &k, S);
        int perm[k];
        for (int i = 0; i < k; i ++) {
            perm[i] = i;
        }
        int res = 50000;
        do {
            int pos = 0;
            while (S[pos] != '\0') {
                for (int i = 0; i < k; i ++) {
                    T[pos + i] = S[pos + perm[i]];
                }
                pos += k;
            }
            T[pos] = '\0';
            res <?= rle(T);
        } while (next_permutation(perm, perm + k));
        printf("Case #%d: %d\n", c, res);
    }
    return 0;
}
