#include <cstdio>
#include <cstring>

int prevcount[10];

int main() {
    int t;
    char n[25];
    scanf("%d", &t);

    for (int c = 1; c <= t; ++c) {
        memset(prevcount, 0, sizeof(prevcount));
        scanf("%s", &n);

        int cur = strlen(n) - 2;
        int prev = strlen(n) - 1;
        prevcount[n[prev] - '0']++;

        while (cur >= 0 && n[cur] >= n[prev]) {
            --cur;
            --prev;
            prevcount[n[prev] - '0']++;
        }

        if (cur >= 0) {
            int i = n[cur] - '0' + 1;
            prevcount[n[cur] - '0']++;
            while (!prevcount[i])
                ++i;
            prevcount[i]--;
            n[cur] = i + '0';
            int j = 0;
            i = cur + 1;
            while (i < strlen(n)) {
                while (prevcount[j]) {
                    n[i++] = j + '0';
                    prevcount[j]--;
                }
                ++j;
            }
            printf("Case #%d: %s\n", c, n);
        } else {
            int k;
            for (k = 1; k < 10; ++k) {
                if (prevcount[k]) {
                    break;
                }
            }
            printf("Case #%d: %d0", c, k);
            prevcount[k]--;
            int j = 0;
            int i = 0;
            while (j < 10) {
                while (prevcount[j]) {
                    printf("%d", j);
                    prevcount[j]--;
                }
                ++j;
            }
            printf("\n");
        }
    }
    return 0;
}
