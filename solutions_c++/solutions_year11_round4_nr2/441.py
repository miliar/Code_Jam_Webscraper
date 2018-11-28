#include <stdio.h>

int nR, nC;
int board[20][20];

int min(int a, int b) {
    if (a < b) return a;
    return b;
}

bool possible(int sR, int sC, int eR, int eC) {
    double sumR = 0.0;
    double sumC = 0.0;

    double midR = (double)(eR + sR) / 2.0;
    double midC = (double)(eC + sC) / 2.0;
    for (int i = sR; i <= eR; ++i) {
        for (int j = sC; j <= eC; ++j) {
            if (i == sR && j == sC ||
                i == sR && j == eC ||
                i == eR && j == sC ||
                i == eR && j == eC) continue;

            sumR += (double)(i - midR) * (double)board[i][j];
            sumC += (double)(j - midC) * (double)board[i][j];
        }
    }
    return (sumR < 10e-9 && sumR > -10e-9 && sumC < 10e-9 && sumC > -10e-9);
}

int main(void) {
    int nCases;
    scanf("%d", &nCases);
    for (int cC = 0; cC < nCases; ++cC) {
        int w;
        scanf("%d%d%d", &nR, &nC, &w);
        char input[20];
        for (int i = 0; i < nR; ++i) {
            scanf("%s", input);
            for (int j = 0; j < nC; ++j) {
                board[i][j] = input[j] - '0';
            }
        }

        int maxSize = 0;
        for (int sR = 0; sR <= nR - 3; ++sR) {
            for (int sC = 0; sC <= nC - 3; ++sC) {
                int max = min(nR - sR, nC - sC);
                if (max <= maxSize || max < 3) continue;
                for (int i = 3; i <= max; ++i) {
                    if (possible(sR, sC, sR + i - 1, sC + i - 1)) {
                        if (maxSize < i)
                            maxSize = i;
                    }
                }
            }
        }
        printf("Case #%d: ", cC + 1);
        if (!maxSize)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", maxSize);
    }
    return 0;
}
