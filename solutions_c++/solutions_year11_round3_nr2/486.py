#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <complex>
#define MAXN 1005
using namespace std;
double cost[MAXN];
bool mark[MAXN];
double res,t;
int L,N,C;
double cal(){
    double s=0,c=N;
    for(int i=0;i<N;i++){
        if(s+cost[i]*2<=t){
            s+=cost[i]*2;
        }
        else{
            double d=cost[i]*2-(t-s);
            s=t;
            if(mark[i])s+=d/2;
            else s+=d;
            c=i+1;
            break;
        }
    }
    for(int i=c;i<N;i++){
        if(mark[i])s+=cost[i];
        else s+=cost[i]*2;
    }
    return s;
}
int main(){
    int T;
    freopen("B-small-attempt1.in","r",stdin);
    freopen("bsmall_at1.txt","w",stdout);
    scanf("%d",&T);
    for(int k=1;k<=T;k++){
        scanf("%d%lf%d%d",&L,&t,&N,&C);
        res=1e15;
        for(int i=0;i<C;i++){
            scanf("%lf",&cost[i]);
        }
        for(int i=C;i<N;i++){
            cost[i]=cost[i%C];
        }
        memset(mark,false,sizeof(mark));
        if(L==0){
            double ss=0;
            for(int i=0;i<N;i++){
                ss+=cost[i]*2;
            }
            res=ss;
        }
        else if(L==1){
            for(int i=0;i<N;i++){
                mark[i]=true;
                double r=cal();
                if(r<res)res=r;
                mark[i]=false;
            }
        }
        else{
            for(int i=0;i<N;i++){
                for(int j=i+1;j<N;j++){
                    mark[i]=mark[j]=true;
                    double r=cal();
                    if(r<res)res=r;
                    mark[i]=mark[j]=false;
                }
            }
        }
        printf("Case #%d: %.0lf\n",k,res);
    }
    return 0;
}
