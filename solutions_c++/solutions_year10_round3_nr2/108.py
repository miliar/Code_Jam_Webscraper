#include<iostream>
#include<cmath>
#include<string>
using namespace std;
int T;
int C,L,R,P;
int main(){
freopen("B-large.in","r",stdin);
freopen("B-large.out","w",stdout);
    scanf("%d",&T);
    int t=0;
    while (T--){
          scanf("%d%d%d",&L,&R,&C);
          int Ans=0;
          double tt=double(R)/double(L);
          while (tt>C){
                tt=sqrt(tt);
                Ans++;
          }
          printf("Case #%d: %d\n",++t,Ans);
    }
    return 0;
}
