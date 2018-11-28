#include<stdio.h>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<string>
#include<cmath>
#include<set>
#include<map>
#include<vector>
using namespace std;
void gao(int *x,int n){
     if(n==0)return;
     for(int i=2;i<=100;i++){
         if(n==1)break;
         while(n%i==0){
             n/=i; 
             x[i]++; 
         }                  
     }   
}
void sub(int *x,int *y){
    for(int i=2;i<=100;i++){
         int temp=min(x[i],y[i]); 
         x[i]-=temp;
         y[i]-=temp;                
     }     
}
int gcd(int a,int b){
    if(b==0)return a;
    return gcd(b,a%b);    
}
int main()

{
    freopen("A-large.in","r",stdin);
    freopen("1.txt","w",stdout);
    int T,C,pd,pg;
    __int64 N;int i,j;
    scanf("%d",&T);
    for(C=1;C<=T;C++){
        scanf("%I64d%d%d",&N,&pd,&pg);
        printf("Case #%d: ",C);
        if(pg==100){
            if(pd!=100){
                 puts("Broken");
                 continue;           
            }         
        }
        if(pg==0){
            if(pd!=0){
                 puts("Broken");
                 continue;           
            }         
        }
        /*int a[101],b[101];
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        gao(a,pd);
        gao(b,100);
        sub(a,b);
        __int64 res=1;
        for(i=2;i<=100;i++){
            if(a[i]){
                for(j=0;j<a[i];j++){
                    res*=i;                    
                }         
            }                    
        }*/
        __int64 xx;
        xx=gcd(100,pd);
        xx=100/xx;
        if(xx<=N){
            puts("Possible");
        }
        else puts("Broken");
        
                          
    }
}
