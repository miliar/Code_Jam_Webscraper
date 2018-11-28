#include"stdio.h"
#include"string.h"
#include"iostream"
#include"algorithm"
using namespace std;
int T,R,K,N,pp[10001];

void solve(){
    int i;
    for(int k=1;k<=R-1;k++){
        for(i=1;i<=N;i++) pp[k*N+i]=pp[i];
    }
    int tot=0,sum=0,num=0;
    i=1;
    for(int k=1;k<=R;k++){
        sum=0;num=0;
        for(;;){
            if(sum+pp[i]<=K&&num<N){
                num++;
                sum+=pp[i];
                i++;
            }
            else{
                break;
            }
        }
        tot+=sum;
    }
    printf("%d\n",tot);
}

int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for(int i=1;i<=T;i++){
        scanf("%d%d%d",&R,&K,&N);
        for(int i=1;i<=N;i++) scanf("%d",&pp[i]);
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}
