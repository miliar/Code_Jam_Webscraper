#include <cstdio>
#include <cstring>

using namespace std;

int L, D, N;

char dic[5000][20];
char mask[26];
char valid[5000];


int work() {
    memset(valid, 1, D);
    for (int i = 0; i < L; i++) {
        char c;
        memset(mask, 0, 26);
        scanf("%c", &c);
        while (c == '\n' || c == '\r') scanf("%c", &c);
        if (c == '(') {
            while (1) {
                scanf("%c", &c);
                if (c == ')') break;
                mask[c - 'a'] = 1;
            }
        } else {
            mask[c - 'a'] = 1;
        }

        for (int j = 0; j < D; j++) {
            valid[j] &= mask[dic[j][i] - 'a'];
        }
    }

    int ans = 0;
    for (int i = 0; i < D; i++) {
        ans += valid[i];
    }
    return ans;
}

int main() {
    scanf("%d %d %d", &L, &D, &N);

    for (int i = 0; i < D; i++) {
        scanf("%s", dic[i]);
    }

    for (int i = 0; i < N; i++) {
        int ans = work();
        printf("Case #%d: %d\n", i, ans);
    }

    return 0;
}
