#include <cstdio>

using namespace std;

char s[100][100], t[100][100];

int main() {
    int T; scanf("%d", &T);
    for (int tt = 0; tt < T; ++tt) {
        int n, k; scanf("%d %d", &n, &k);
        for (int i = 0; i < n; ++i) {
            scanf("%s", s[i]);
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                t[i][j] = s[n - 1 - j][i];
            }
        }
/*        for (int i = 0; i < n; ++i) {
            printf("%s\n", t[i]);
        }
        putchar('\n');*/
        for (int j = 0; j < n; ++j) {
            for (int i = n - 1, k = n - 1; i >= 0; --i) {
                while ((k >= 0) && (t[k][j] == '.')) --k;
                if (k < 0) t[i][j] = '.';
                else t[i][j] = t[k][j];
                --k;
            }
        }
/*        for (int i = 0; i < n; ++i) {
            printf("%s\n", t[i]);
        }
        putchar('\n');*/
        bool R = false, B = false;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) if (t[i][j] != '.') {
                if (i + k <= n) {
                    bool f = true;
                    for (int l = 0; l < k; ++l) {
                        if (t[i + l][j] != t[i][j]) {
                            f = false;
                            break;
                        }
                    }
                    if (f) {
                        if (t[i][j] == 'R') {
                            R = true;
                        } else {
                            B = true;
                        }
                    }
                }
                if (j + k <= n) {
                    bool f = true;
                    for (int l = 0; l < k; ++l) {
                        if (t[i][j + l] != t[i][j]) {
                            f = false;
                            break;
                        }
                    }
                    if (f) {
                        if (t[i][j] == 'R') {
                            R = true;
                        } else {
                            B = true;
                        }
                    }
                }
                if ((i + k <= n) && (j + k <= n)) {
                    bool f = true;
                    for (int l = 0; l < k; ++l) {
                        if (t[i + l][j + l] != t[i][j]) {
                            f = false;
                            break;
                        }
                    }
                    if (f) {
                        if (t[i][j] == 'R') {
                            R = true;
                        } else {
                            B = true;
                        }
                    }
                }
                if ((i + k <= n) && (j - k >= -1)) {
                    bool f = true;
                    for (int l = 0; l < k; ++l) {
                        if (t[i + l][j - l] != t[i][j]) {
                            f = false;
                            break;
                        }
                    }
                    if (f) {
                        if (t[i][j] == 'R') {
                            R = true;
                        } else {
                            B = true;
                        }
                    }
                }
                if (R && B) break;
            }
            if (R && B) break;
        }
        
        if (R && B) printf("Case #%d: Both\n", tt + 1);
        else if (B) printf("Case #%d: Blue\n", tt + 1);
        else if (R) printf("Case #%d: Red\n", tt + 1);
        else printf("Case #%d: Neither\n", tt + 1);
    }
    return 0;
}
