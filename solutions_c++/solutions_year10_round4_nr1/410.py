#include <cstdio>
#include <cstring>

typedef int Diamond[250][250];
Diamond src, dest;

inline int getCi(int k, int i) {
    if (i <= k)
        return i;
    return k * 2 - i;
}

bool verify(Diamond mat, int k) {
    int i, j;
    for (i = 1; i <= k * 2 - 1; i++) {
        int ci = getCi(k, i);
        for (j = 1; j <= ci; j++) {
            if (mat[i][j] == -1)
                continue;
            if (mat[i][j] != mat[i][ci + 1 - j])
                return false;
            if (mat[i][j] != mat[2 * k - i][j])
                return false;
        }
    }
    return true;
}

void copyPos(Diamond from, Diamond to, int k1, int k2, int X, int Y) {
    memset(to, -1, sizeof(Diamond));
    /*
    int ci;
    // verify middle-right
    ci = getCi(k2, k1 + Y);
    if (X + k1 > ci)
        throw 1;
    // verify top
    ci = getCi(k2, Y + 1);
    if (X + 1 > ci)
        throw 1;
        */
    
    int pi, pj, i, j;
    pj = X;
    for (i = 1, pi = Y + i; i <= k1 * 2 - 1; i++, pi++) {
        if (pi > k2 * 2 - 1)
            throw 1;
        if (pj < 0)
            throw 1;
        int ci = getCi(k1, i);
        int c2i = getCi(k2, pi);
        for (j = 1; j <= ci; j++) {
            to[pi][j + pj] = from[i][j];
            if (j + pj > c2i)
                throw 1;
        }
        if (i >= k1)
            pj++;
        if (pi >= k2)
            pj--;
    }
}

bool fillMat(Diamond mat, int k) {
    int i, j;
    bool flag = true;
    while (flag) {
        flag = false;
        for (i = 1; i <= k * 2 - 1; i++) {
            int ci = getCi(k, i);
            for (j = 1; j <= ci; j++) {
                if (mat[i][j] != -1)
                    continue;
                if (ci + 1 - j != j && mat[i][ci + 1 - j] != -1) {
                    mat[i][j] = mat[i][ci + 1 - j];
                    flag = true;
                    continue;
                }
                if (2 * k - i != i && mat[2 * k - i][j] != -1) {
                    mat[i][j] = mat[2 * k - i][j];
                    flag = true;
                    continue;
                }
            }
        }
    }
    return true;
}

void printMat(Diamond mat, int k) {
    int i, j;
    for (i = 1; i <= k * 2 - 1; i++) {
        int ci = getCi(k, i);
        for (j = 1; j <= ((k > i) ? (k - i) : (i - k)); j++)
            printf(" ");
        for (j = 1; j <= ci; j++) {
            printf("%2d", mat[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

int t, T, k;
int i, j, len, result;

int main() {
    scanf("%d", &T);
    for (t = 1; t <= T; t++) {
        scanf("%d", &k);
        memset(src, -1, sizeof(Diamond));
        for (i = 1; i <= k * 2 - 1; i++) {
            int ci = getCi(k, i);
            for (j = 1; j <= ci; j++)
                scanf("%d", &src[i][j]);
        }
        //printf("Case #%d: %d\n", t, result);
        //printMat(src, k);
        //continue;
        for (len = k; len < k * 3; len++) {
            for (i = 0; i <= (len - k) * 2; i++) {
                for (j = 0; j <= len * 2; j++) {
                    try {
                        copyPos(src, dest, k, len, j, i);
                        fillMat(dest, len);
                        //printMat(dest, len);
                        if (verify(dest, len)) {
                        //    printf("got!!!\n");
                            goto out;
                        }
                    } catch (int) {
                        continue;
                    }
                }
            }
        }
        printf("error!!!\n");
out:
        //copyPos(src, dest, k, k, 0, 0);
        //printMat(src, k);
        //printMat(dest, len);
        result = len * len - k * k;
        printf("Case #%d: %d\n", t, result);
        //return 0;
    }
}
