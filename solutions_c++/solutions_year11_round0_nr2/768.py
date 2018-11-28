#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

int T, C, D, N;
int comb[26][26], opp[26][26];
int cnt[26];
int que[111];
int qlen;
char buf[111];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++){
        memset(comb, -1, sizeof(comb));
        memset(opp, 0, sizeof(opp));
        memset(cnt, 0, sizeof(cnt));
        qlen = 0;
        scanf("%d", &C);
        while(C--){
            scanf("%s", buf);
            comb[buf[0]-'A'][buf[1]-'A'] = comb[buf[1]-'A'][buf[0]-'A'] = buf[2]-'A';
        }
        scanf("%d", &D);
        while(D--){
            scanf("%s", buf);
            opp[buf[0]-'A'][buf[1]-'A'] = opp[buf[1]-'A'][buf[0]-'A'] = 1;
        }
        scanf("%d%s", &N, buf);
        for(int i = 0; i < N; i++){
            int ch = buf[i]-'A';
            que[qlen++] = ch;
            cnt[ch]++;
            while(qlen >= 2){
                int tmp = comb[que[qlen-1]][que[qlen-2]];
                if(tmp >= 0){
                    cnt[que[qlen-1]]--;
                    cnt[que[qlen-2]]--;
                    cnt[tmp]++;
                    que[qlen-2] = tmp;
                    qlen--;
                } else{
                    break;
                }
            }
            for(int j = 0; j < 26; j++){
                if( ((j!=que[qlen-1] && cnt[j] > 0) || (j==que[qlen-1] && cnt[j] > 1))
                   && opp[j][que[qlen-1]]){
                    memset(cnt, 0, sizeof(cnt));
                    qlen = 0;
                }
            }
//            que[qlen] = 0;
//            puts("...");for(int i = 0 ;i < qlen; i++)printf("%c%c", que[i]+'A', i<qlen-1?' ':'\n');
        }

        printf("Case #%d: ", cas);
        printf("[");
        for(int i = 0; i < qlen; i++){
            if(i > 0)printf(", ");
            printf("%c", que[i]+'A');
        }
        printf("]\n");
    }
    return 0;
}
