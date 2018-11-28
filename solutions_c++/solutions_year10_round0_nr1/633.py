#include"iostream"
using namespace std;
int data[31]={1};
int main(){
    int T,N,K;
    for(int i=1;i<=30;i++){
       data[i]=data[i-1]*2;
    }
    freopen("A-large.in","r",stdin);
    freopen("out2.txt","w",stdout);
    scanf("%d",&T);
    for(int i=1;i<=T;i++){
        scanf("%d%d",&N,&K);
        if((K+1)%data[N]==0)printf("Case #%d: ON\n",i);
        else printf("Case #%d: OFF\n",i);
    }
    return 0;
}
