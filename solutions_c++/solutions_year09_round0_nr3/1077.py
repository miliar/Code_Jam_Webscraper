#include <cstdio>
#include <cstring>

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int n;
    scanf("%d\n", &n);
    for (int nT = 0; nT < n; ++nT) {
        const char pattern[20] = "welcome to code jam";

        const size_t MAXLEN = 10000;
        char line[MAXLEN];
        gets(line);
        int len = strlen(line);

        int counts[20][MAXLEN];
        memset(counts, 0, sizeof(counts));
        counts[0][0] = 1;
        for (size_t i = 0; i < 19; ++i) {
            int prevSum = 0;
            for (size_t j = 0; j < len; ++j) {
                prevSum = (prevSum + counts[i][j]) % 10000;
                if (line[j] == pattern[i])
                    counts[i + 1][j] = prevSum;
            }
        }
        int res = 0;
        for (size_t i = 0; i < len; ++i)
            res += counts[19][i];
        printf("Case #%d: %.4d\n", nT + 1, res % 10000);
    }
    
    return 0;
}
