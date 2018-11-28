#include <cstdio>

using namespace std;


int main() {
    int t, tCase, r, c, i, j, count;
    char v[64][64];

    scanf("%d", &t);
    for (tCase = 1; tCase <= t; tCase++) {

        scanf("%d %d", &r, &c);
        getchar();
        for (i = 0; i <= r; i++) {
            for (j = 0; j <= c; j++) {
                v[i][j] = '0';
            }
        }
        for (i = 1; i <= r; i++) {
            for (j = 1; j <= c; j++) {
                scanf("%c", &v[i][j]);
            }
            getchar();
        }

        count = 0;
        for (i = 1; i <= r; i++) {
            for (j = 1; j <=c ; j++) {
                if (v[i][j] == '#') {
                    count++;
                }
                if (v[i-1][j-1] == '#' && v[i-1][j] == '#' && v[i][j-1] == '#' && v[i][j] == '#') {
                    v[i-1][j-1] = '/';
                    v[i-1][j] = '\\';
                    v[i][j-1] = '\\';
                    v[i][j] = '/';
                    count -= 4;
                }
            }
        }

        if (!count) {
            printf("Case #%d:\n", tCase);
            for (i = 1; i <= r; i++) {
                for (j = 1; j <= c; j++) {
                    printf("%c", v[i][j]);
                }
                printf("\n");
            }
        } else {
            printf("Case #%d:\nImpossible\n", tCase);
        }

    }

    return 0;
}
