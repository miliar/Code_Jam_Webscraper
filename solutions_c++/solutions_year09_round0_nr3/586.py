#include <cstdio>

using namespace std;

const char str[20] = "welcome to code jam";

#define MAXN 512
#define MOD 10000
char input[MAXN];
int nr[20][MAXN];

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf(" %[^\n]\n", input);
        int N = 0;
        for (; input[N]; N++) {
            nr[0][N] = (input[N] == str[0]);
            if (N) {
                nr[0][N] += nr[0][N - 1];
            }
            nr[0][N] %= MOD;
        }

        for (int i = 1; i < 19; i++) {
            for (int j = i; j < N; j++) {
                nr[i][j] = nr[i - 1][j - 1] * (input[j] == str[i]);
                nr[i][j] += nr[i][j - 1];
                nr[i][j] %= MOD;
            }
        }
        printf("Case #%d: %04d\n", t, nr[18][N - 1]);
    }

    return 0;
}


