#include<stdio.h>
#include<string>
#include<vector>
#include<utility>
#include<algorithm>
#include<sstream>
#include<string>
#include<iostream>
using namespace std;

int primos[1000005];
vector < int > q; 

int gcd(int a, int b){
    int k;
    k=a%b; if(!k)return b;
    return gcd(b, k);
}


long long N;

int func(int p){
    int i;
    long long r=1;
    for(i=1; ; i++){
        r = r*p;
        if(r>N)
            return i-1;
    }   
    return 0;
    
}

int minimo(long long a, int b){
    if(a<b) return (int) a;
    else return b;
}

int main(){
    int i, k;
    for(i=0; i<=1000001; i++)
        primos[i]=1;
    for(i=2; i<=1001; i++)
        for(k=2; k*i<=1000001; k++)
            primos[i*k]=0;
    primos[0]=0;
    primos[1]=0;
    int totpr=0;
   // for(i=0; i<=1000001; i++)
     //   if(primos[i]==1){
       //     q.push_back(i);
         //    totpr++;
        //}    
    int T;
    int g;
    scanf("%d ", &T);
    for(g=1; g<=T; g++){
        scanf("%lld ", &N);
        totpr=0;
        q.clear();
        int nnn = minimo(N, 1000000);
        for(i=0; i<=nnn; i++)
            if(primos[i]==1){
                q.push_back(i);
                totpr++;
        }  
        int jj = q.size();
        int mer=0;
        for(i=0; i<jj; i++){
            mer+=func(q[i]);
        }
        mer++;
        if(N==1) mer=jj;
        printf("Case #%d: %d\n", g, mer-jj);
                
    }
}
