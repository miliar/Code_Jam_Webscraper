#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

const int MAXN = 128;
const int MAXM = 128;
char word[MAXN][32];
char gus[MAXM][32];
int pos[MAXN];
bool contain[MAXN][32];

int m, n;

int ex[26], hav[26];
char kn[32];
int calc(char *wd, char *g) {
    memset(pos, 0, sizeof(pos));
    memset(ex, 0, sizeof(ex));
    memset(hav, 0, sizeof(hav));
    int len = strlen(wd);
    int i, j;
    for (i = 0 ; i < len ; i++) kn[i] = '_';
    kn[i] = 0;
    for (i = 0 ; i < n ; i++)
        if (strlen(word[i]) != len) pos[i] = 0;
        else pos[i] = 1;
    int pc = 0, lose = 0;
    while (1) {
        /*
        int tot = 0;
        for (i = 0 ; i < n ; i++)
            tot += pos[i];
        if (tot == 1) break;
        */
        for (i = 0 ; i < n ; i++) {
            if (pos[i] && contain[i][g[pc]-'a'])
                break;
        }
        if (i == n) {++pc; continue;}
        // guess g[pc];
        int flg = 0;
        for (i = 0 ; i < len ; i++)
            if (wd[i] == g[pc]) {
                flg = 1;
                kn[i] = g[pc];
            }
        if (strcmp(kn, wd) == 0)
            break;
        if (flg == 0) {
            ++lose;
            ex[g[pc]-'a'] = 1;
        } else {
            hav[g[pc]-'a'] = 1;
        }
        // mark the impossible ones
        for (i = 0 ; i < n ; i++) {
            if (!pos[i]) continue;
            for (j = 0 ; word[i][j] ; j++) {
                if (ex[word[i][j]-'a']) {
                    pos[i] = 0;
                    break;
                }
                if (kn[j] != '_' && kn[j] != word[i][j]) {
                    pos[i] = 0;
                    break;
                }
                if (hav[word[i][j]-'a'] && kn[j] == '_') {
                    pos[i] = 0;
                    break;
                }
            }
        }
        ++pc;
    }
    return lose;
}

int main() {
    freopen("b-small-attempt1.in","r",stdin);
    freopen("b-small-attempt1.out","w",stdout);
    int T, ca, i, j, t;
    scanf("%d",&T);
    for (ca = 1 ; ca <= T ; ++ca) {
        scanf("%d%d",&n,&m);
        memset(contain, 0, sizeof(contain));
        for (i = 0 ; i < n ; i++) {
            scanf("%s",word[i]);
            for (j = 0 ; word[i][j] ; ++j)
                contain[i][word[i][j]-'a'] = true;
        }
        for (i = 0 ; i < m ; i++)
            scanf("%s",gus[i]);
        printf("Case #%d:",ca);
        for (t = 0 ; t < m ; ++t) {
            int best = -1, ans = 0;
            for (i = 0 ; i < n ; i++) {
                int tmp = calc(word[i], gus[t]);
                if (tmp > best) {
                    best = tmp;
                    ans = i;
                }
            }
            printf(" %s",word[ans]);
        }
        printf("\n");
    }
    return 0;
}
