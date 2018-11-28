#include<iostream>
#include<string>
#include<cmath>
using namespace std;
const int Maxn=1000;
int g[Maxn],N,R,k,now,Ans;
void Init(){
     
     scanf("%d%d%d", &R, &k, &N);
     for (int i=0;i<N;i++) scanf("%d", &g[i]); 
} 
int main(){
freopen("1.in","r",stdin);
freopen("1.out","w",stdout); 
    int T;
    scanf("%d",&T);
    for (int i=1;i<=T;i++){ 
        Init();
        now=0,Ans=0;
        while (R--){
              int S=0;
              int tmp=now+N;
              while (S+g[now%N]<=k & now!=tmp) S+=g[now%N],now++;
              Ans+=S;
        }
        printf("Case #%d: %d\n", i, Ans);
     }
     return 0;
}
