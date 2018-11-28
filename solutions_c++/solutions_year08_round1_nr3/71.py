#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

#define MOD 1000

int n;
int a=6,b=1,c=-4,d=0;
int aa,bb,cc,dd;
int ta,tb,tc,td;
int work(int K){
    if(n==0)return 2;
    aa=1;bb=0;cc=0;dd=1;
    a=6,b=1,c=-4,d=0;
    for(int k=K;k>0;k=k/2){
         if(k&1){
            ta=(aa*a+bb*c)%MOD;
            tb=(aa*b+bb*d)%MOD;
            tc=(cc*a+dd*c)%MOD;
            td=(cc*b+dd*d)%MOD;    
            aa=ta;bb=tb;cc=tc;dd=td; 
         }
         ta=(a*a+b*c)%MOD;
         tb=(a*b+b*d)%MOD;
         tc=(c*a+d*c)%MOD;
         td=(c*b+d*d)%MOD;   
         a=ta;b=tb;c=tc;d=td;             
    }
    return (6*aa+2*cc)%MOD; 
}

int main(){
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    int cases;
    scanf("%d",&cases);
    int K=1;
    while(cases-->0){
        scanf("%d",&n);
        printf("Case #%d: %03d\n",K++,(MOD+work(n-1)-1)%MOD);        
    }
    return 0;
}
