#include <cstdio>
#include <cstring>
using namespace std;

int N, M;
int ct[110][26];
char W[110][13];
int len[110];
int mark[110];
char L[30];

void init() {
    scanf("%d", &N);
    scanf("%d", &M);
    memset(ct, 0, sizeof(ct));
    for (int i=0;i<N;i++) {
        scanf("%s", W[i]);
        len[i] = strlen(W[i]);
        for (int j=0;j<len[i];j++)
            ct[i][W[i][j]-'a'] ++;
    }
}

int GetValue(int c) {
    for (int i=0;i<N;i++) mark[i] = 1;
    for (int i=0;i<N;i++) if (len[i] != len[c]) mark[i] = 0;
    int s = 0;
    for (int i=0;i<26;i++) {
        int flag = 0;
        for (int j=0;j<N;j++)
            if (mark[j] && ct[j][L[i]-'a'] > 0) {
                flag = 1;
                break;
            }
        if (flag) {
            if (ct[c][L[i]-'a'] == 0) s ++;
            for (int k=0;k<N;k++)
                if (mark[k]) {
                    int conflict = 0;
                    for (int p=0;p<len[k];p++)
                        if ((W[k][p] == L[i] && W[c][p] != L[i]) ||
                            (W[k][p] != L[i] && W[c][p] == L[i])) {
                            conflict = 1;
                            break;
                        }
                    if (conflict) mark[k] = 0;
                }
        }
    }
    return s;
}

void work() {
    int ans, ansp;
    for (int i=0;i<M;i++) {
        scanf("%s", L);
        ans = 0;
        ansp = 0;
        for (int j=0;j<N;j++) {
            int t = GetValue(j);
            //printf("%d\n", t);
            if (t > ans) {
                ans = t;
                ansp = j;
            }
        }
        printf(" %s", W[ansp]);
    }
    printf("\n");
}

int main() {
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int T;
    scanf("%d", &T);
    for (int ti=1;ti<=T;ti++) {
        printf("Case #%d:", ti);
        init();
        work();
    }
    return 0;
}
