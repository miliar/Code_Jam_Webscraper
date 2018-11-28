#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAX_LEN = 505;
const char pattern[] = "welcome to code jam";

char s[MAX_LEN];
int memo[25][MAX_LEN];

int f(int i, int j) {
    if (i >= strlen(pattern)) {
        return 1;
    }
    if (j >= strlen(s)) {
        return 0;
    }
    if (memo[i][j] == -1) {
        if (pattern[i] == s[j]) {
            memo[i][j] = (f(i + 1, j + 1) % 10000 + f(i, j + 1) % 10000) % 10000;
        } else {
            memo[i][j] = f(i, j + 1) % 10000;
        }
    }
    return memo[i][j];
}

int main() {
    int n;
    scanf("%d\n", &n);

    for (int t = 1; t <= n; ++t) {
        for (int i = 0; i < strlen(pattern); ++i) {
            for (int j = 0; j < MAX_LEN; ++j) {
                memo[i][j] = -1;
            }
        }
        memset(s, 0, MAX_LEN * sizeof(char));
        fgets(s, MAX_LEN, stdin);
        s[strlen(s) - 1] = 0;
        int result = f(0, 0);
        printf("Case #%d: ", t);
        if (result < 1000)
            printf("0");
        if (result < 100)
            printf("0");
        if (result < 10)
            printf("0");
        printf("%d\n", result);
    }
    return 0;
}
