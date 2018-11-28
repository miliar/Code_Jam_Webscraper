#include <cstdio>
#include <cstring>

char *welcome = "welcome to code jam";
int count[2][64];
char word[512];

int main() {
    int N;
    FILE *f = fopen("c.in", "rt");
    fscanf(f, "%d\n", &N);

    for (int t = 0; t < N; ++t) {
        fgets(word, 512, f);
        memset(count[0], 0, 64 * sizeof(int));
        count[0][0] = 1;
        int prv, nxt;
        for (int i = 0; word[i] != 0 && word[i] != '\n'; ++i) {
            prv = i % 2;
            nxt = (i + 1) % 2;
            memcpy(count[nxt], count[prv], 64 * sizeof(int));
            for (int j = 0; j < 19; ++j) {
                if (word[i] == welcome[j]) {
                    count[nxt][j + 1] += count[prv][j];
                    count[nxt][j + 1] %= 10000;
                }
            }
            count[nxt][0] = 1;
            /*
            for (int j = 0; j < 20; ++j) {
                fprintf(stderr, "%d ", count[nxt][j]);
            }
            fprintf(stderr, "\n");
            */
        }
        printf("Case #%d: %04d\n", t + 1, count[nxt][19]);
    }
    fclose(f);
    return 0;
}
