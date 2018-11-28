#include <cstdio>
#include <cstring>

using namespace std;

char S[501];
int T[501][20];

char msg[] = "welcome to code jam";

int main() {
    for (int j = 0; j <= 19; j++)
        T[0][j] = 0;
    for (int i = 0; i <= 500; i++)
        T[i][0] = 1;
    int N; scanf("%d\n", &N);
    for (int c = 1; c <= N; c++) {
        gets(S);
        int len = strlen(S);
        for (int i = 1; i <= len; i++) {
            for (int j = 1; j <= 19; j++) {
                T[i][j] = T[i-1][j];
                if (S[i-1] == msg[j-1]) {
                   T[i][j] += T[i][j-1];
                   T[i][j] %= 10000;
                }
            }
        }
        printf("Case #%d: %04d\n", c, T[len][19]);
    }
    return 0;
}
