#include <stdio.h>
#include <string.h>

const int maxl = 15 + 5;
const int maxc = 26 + 1;
const int maxd = 5000 + 10;
 
int L, D, N;
char wd[maxd][maxl];
bool can[maxl][maxc];

int main(void)
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    while (scanf("%d%d%d", &L, &D, &N) == 3) {
        for (int i = 0; i < D; ++i)
            scanf("%s", wd[i]);
        for (int i = 0; i < N; ++i) {
            memset(can, 0, sizeof can);
            for (int j = 0; j < L; ++j) {
                char c;
                while (scanf("%c", &c), c!='(' && !(c>='a' && c<='z'));
                if (c == '(') {
                    while (scanf("%c", &c), c!=')')
                        if (c>='a' && c<='z') can[j][c-'a'] = 1;
                } else
                    can[j][c-'a'] = 1;
            }
            int cnt = 0;
            for (int k = 0; k < D; ++k) {
                int j = 0;
                for (; j < L; ++j)
                    if (!can[j][wd[k][j]-'a']) break;
                if (j == L) ++cnt;
            }
            printf("Case #%d: %d\n", i+1, cnt);
        }
    } 
    return 0; 
} 
