#include<iostream>
bool state[32],input[32];
using namespace std;
int main(){
    int T,N,k,t=0;
    scanf("%d",&T);
    while(T--){
        t++;
        scanf("%d%d",&N,&k);
        memset(state,false,sizeof state);
        memset(input,false,sizeof input);
        input[1]=true;
        state[0]=true;input[0]=true;
        for(int i=1;i<=k;i++){
            for(int j=1;j<=N;j++){
                if(input[j])
                    state[j]=!state[j];
                if(state[j-1] && input[j-1])
                    input[j]=true;
                else
                    input[j]=false;

            }
        }
        if(state[N]&&input[N])
            printf("Case #%d: ON\n",t);
        else
            printf("Case #%d: OFF\n",t);
    }
    return 0;
}
