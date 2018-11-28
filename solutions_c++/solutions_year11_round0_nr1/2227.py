#include <cstdio>
#include <cstring>
#define ABS(a,b) ((a-b)>0?(a-b):(b-a))
struct SEQ{
    int loc;
    int cnt;
}seq_o[105],seq_b[105];
int cnt_o,cnt_b;
int T,N;
char c;

int main(){
    scanf("%d",&T);
    for (int i=0;i<T;++i){
        cnt_o = cnt_b = 0;
        for (int j=0;j<104;++j){
            seq_o[j].cnt = seq_b[j].cnt = -1;
        }
        scanf("%d",&N);
        for (int j=0;j<N;++j){
            scanf(" %c",&c);
            if (c == 'O'){
                scanf("%d",&seq_o[cnt_o].loc);
                seq_o[cnt_o++].cnt = j;
            }
            else {
                scanf("%d",&seq_b[cnt_b].loc);
                seq_b[cnt_b++].cnt = j;
            }
        }
        int o,b,pos_o,pos_b,ans=0,d_o,d_b;
        o = b = 0;
        pos_o = pos_b = 1;
        for (int j=0;j<N;++j){
            d_o = ABS(pos_o,seq_o[o].loc);
            d_b = ABS(pos_b,seq_b[b].loc);
            if (seq_o[o].cnt == j){
                pos_o = seq_o[o].loc;
                if (d_o >= d_b){
                    pos_b = seq_b[b].loc;    
                }
                else {
                    pos_b = seq_b[b].loc + d_b - d_o -1;
                }
                ans += d_o+1;
                ++o;
            }
            else {
                pos_b = seq_b[b].loc;
                if (d_o <= d_b){
                    pos_o = seq_o[o].loc;    
                }
                else {
                    pos_o = seq_o[o].loc + d_o - d_b -1;
                }
                ans += d_b+1;
                ++b;
            }
        }
        printf("Case #%d: %d\n",i+1,ans);
    }    
}
