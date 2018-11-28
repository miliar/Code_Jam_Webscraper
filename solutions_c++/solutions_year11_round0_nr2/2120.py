#include <cstdio>
#include <cstring>

int query[30],cnt;
char com[10][10],seq[30]={'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'},ans[105];
bool opp[10][10];
int ans_l,ans_s;

void init(){
    for (int i=0;i<105;++i)
        ans[i] = 0;
    memset(com,0,sizeof(com));
    memset(opp,0,sizeof(opp));
    for (int i=0;i<26;++i)
        query[i] = -1;
    query['Q' - 65] = 0;
    query['W' - 65] = 1;
    query['E' - 65] = 2;
    query['R' - 65] = 3;
    query['A' - 65] = 4;
    query['S' - 65] = 5;
    query['D' - 65] = 6;
    query['F' - 65] = 7;
    cnt = 8;
}

int T,C,D,N,t1,t2,t3;
char s[3],temp_c;

int main(){
    scanf("%d",&T);
    for (int i=0;i<T;++i){
        init();
        scanf("%d",&C);    
        for (int j=0;j<C;++j){
            scanf("%s",s);
            t1 = query[s[0]-65];
            t2 = query[s[1]-65];
            seq[cnt] = s[2];
            com[t1][t2] = com[t2][t1] = seq[cnt];
            t3 = query[s[2]-65] = cnt++;
        }
        scanf("%d",&D);
        for (int j=0;j<D;++j){
            scanf("%s",s);
            t1 = query[s[0]-65];
            t2 = query[s[1]-65];
            opp[t1][t2] = opp[t2][t1] = 1;
        }
        scanf("%d",&N);
        ans_s = ans_l = 0;
        for (int j=0;j<N;++j){
            scanf(" %c",&temp_c);
            if (ans_s != ans_l && query[temp_c-65] < 8 && query[ans[ans_l-1]-65] < 8 && com[query[temp_c-65]][query[ans[ans_l-1]-65]])
                ans[ans_l-1] = com[query[temp_c-65]][query[ans[ans_l-1]-65]];
            else {
                ans[ans_l++] = temp_c;
                if (query[temp_c-65] < 8)
                    for (int k=ans_l-2;k>=ans_s;--k)
                        if (query[ans[k]-65] < 8 && opp[query[ans[k]-65]][query[ans[ans_l-1]-65]])
                            ans_s = ans_l;
            }
        }
        printf("Case #%d: [",i+1);
        for (;ans_s<ans_l-1;++ans_s)
            printf("%c, ",ans[ans_s]);
        if (ans_s < ans_l)
            printf("%c",ans[ans_s]);
        printf("]\n");
    }
}
