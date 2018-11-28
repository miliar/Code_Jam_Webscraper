#include<iostream>
using namespace std;
int g[1001];
int main(){
    int T,R,k,N,t=0;
    scanf("%d",&T);
    while(T--){
        t++;
        scanf("%d%d%d",&R,&k,&N);
        for(int i=0;i<N;i++)
            scanf("%d",&g[i]);
        int roller=0,euros=0;
        for(int i=0;i<R;i++){
            int temp=0,no=0;
            while(temp+g[roller%N]<=k && no<N){
                temp+=g[roller%N],roller++;
                no++;
            }
            euros+=temp;
        }
        printf("Case #%d: %d\n",t,euros);
    }
    return 0;
}
