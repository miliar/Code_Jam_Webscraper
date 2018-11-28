#include <stdio.h>
#include <string.h>
char word[5100][20], s[1000];
int pattern[20][26];
int main() {
    int i, j, k, a, cases = 0;
    int l, d, n, par;
    scanf("%d%d%d", &l, &d, &n);
    for (i = 0; i < d; ++i) {
        scanf("%s", word[i]);
    }
    for (i = 0; i < n; ++i) {
        scanf("%s", s);
        par = k = 0;
        memset(pattern, 0, sizeof(pattern));
        
        for (j = 0; s[j]; ++j) {
            if (s[j] == '(') {
                par = 1;
            } else if (s[j] == ')') {
                ++k;
                par = 0;
            } else if (par) {
                pattern[k][s[j]-'a']= 1;
            } else {
                pattern[k++][s[j]-'a']= 1;
            }
        }
        int tot = 0;
        if (k != l) {
            puts("error");
        }
        for (j = 0; j < d; ++j) {
            for (k = 0; k < l; ++k) {
                if (!pattern[k][word[j][k]-'a']) {
                    break;
                }
            }
            if (k >= l) {
                ++tot;
            }
        }
        printf("Case #%d: %d\n", ++cases, tot);
    }
    return 0;
}