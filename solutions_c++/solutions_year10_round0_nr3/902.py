/*
    Qualification Round 2010 -
    Theme Park
    by Dave Chang
*/
#include <cstdio>
#include <cstring>
using namespace std ;

    int T, R, k, N;
    int g[1000], next_p[1000];
    int money[1000], all;
    int first_use[1000];
    int earn_round , round_num, cir_start;

int main(){
    scanf("%d",&T);
    for(int z=1;z<=T;++z){
        scanf("%d %d %d",&R,&k,&N);
        earn_round = 0;
        round_num = 0;
        cir_start = 0;
        all = 0;
        memset(next_p,0,sizeof(next_p));
        memset(money,0,sizeof(money));
        memset(first_use,0,sizeof(first_use));
        for(int i=0;i<N;++i)
            scanf("%d",&g[i]);
        for(int i=0;i<N;++i)
            all += g[i];
        for(int i=0;i<N;++i){
            int cur = i;
            money[i] = 0;
            while(money[i]<all && money[i]<k){
                int nxt = (cur+1) % N;
                if(money[i]+g[cur]<=k){
                    money[i] += g[cur];
                    next_p[i] = nxt;
                    cur = nxt;
                }
                else break;
            }
        }
        int cur = 0;
        while(true){
            if(first_use[cur]!=0){
                cir_start = 0;
                break;
            }
            earn_round += money[cur];
            ++round_num;
            first_use[cur] = round_num;
            cur = next_p[cur];
            if(next_p[cur]==0) break;
        }
        int result = 0;
        for(int i=0;i!=cir_start, R>0;i = next_p[i]){
            result += money[i];
            --R;
        }
        result += (R / round_num) * earn_round;
        R %= round_num;
        for(int i=0;R>0;i=next_p[i]){
            result += money[i];
        }

        printf("Case #%d: %d\n",z,result);
    }
	return 0 ;
}
