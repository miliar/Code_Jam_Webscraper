#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
using namespace std;

const int base = 10009;

char P[10][10];
int Pn, Pl[10], cnt[26], dn[25][26], dnl[25], re, K, N;
char str[1000], dic[25][100], dct[25][26];

void pharse(char *s)
{
    int len = strlen(s);
    Pn = 0;
    for (int i = 0; i < len;) {
        int j = i;
        Pl[Pn] = 0;
        for (; s[j] && s[j]!='+'; ++j) {
            P[Pn][Pl[Pn]] = s[j];
            Pl[Pn]++;
        }
        i = j + 1;
        ++Pn;
    }
}


void search(int dep)
{
    if (dep == 0) {
        int sm = 0;
        for (int i = 0; i < Pn; ++i) {
            int tp = 1;
            for (int j = 0; j < Pl[i]; ++j)
                tp = (tp * cnt[P[i][j]-'a']) % base;
            sm = (sm + tp) % base;
        }
        re = (re + sm) % base;
        return;
    }
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < dnl[i]; ++j)
            cnt[dct[i][j]] += dn[i][j];
        search(dep-1);
        for (int j = 0; j < dnl[i]; ++j)
            cnt[dct[i][j]] -= dn[i][j];
    }
}

int main(void)
{
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int tot;
    scanf("%d", &tot);
    for (int cas = 1; cas <= tot; ++cas) {
        printf("Case #%d:", cas);
        
        scanf("%s %d", str, &K);
        pharse(str);
        scanf("%d", &N);
        for (int i = 0; i < N; ++i) {
            scanf("%s", dic[i]);
            memset(dn[i], 0, sizeof dn[i]);
            for (int j = 0; j < strlen(dic[i]); ++j)
                ++dn[i][dic[i][j]-'a'];
            dnl[i] = 0;
            for (int j = 0; j < 26; ++j) if (dn[i][j] > 0) {
                dct[i][dnl[i]] = j;
                dn[i][dnl[i]] = dn[i][j];
                dnl[i]++;
            }
        }
        
        for (int k = 1; k <= K; ++k) {
            memset(cnt, 0, sizeof cnt);
            re = 0;
            search(k);
            printf(" %d", re);
        }
        printf("\n");
    } 
    return 0; 
}
