#include<iostream>
#include<cstdio>
#include<map>
#include<cmath>

using namespace std;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int T,N;
    scanf("%d",&T);
    for(int I=1;I<=T;I++){
        int lastO=1,lastB=1;
        int lastTimeO=0,lastTimeB=0,time=0;
        scanf("%d",&N);
        char ch;
        char str[10];
        int v;
        for(int i=0;i<N;i++){
            scanf("%s%d",str,&v);
            ch=str[0];
            if(ch=='O'){
                int x=max(0,abs(lastO-v)-(time-lastTimeO));
                time+=x+1;
                lastO=v;
                lastTimeO=time;
//                cout<<time<<endl;
            }
            else{
                int x=max(0,abs(lastB-v)-(time-lastTimeB));
                time+=x+1;
                lastB=v;
                lastTimeB=time;
  //              cout<<time<<endl;
            }
        }
        printf("Case #%d: %d\n",I,time);
    }
    return 0;
}
                
