#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int T,N,P[1111];
char R[1111][3];

int abs(int x){
 if (x<0) return -x;
 return x;   
}

int max(int a,int b){
    if (a<b) return b;
    return a;
}

void work(int x){
  int i,j,k,oo=0,bb=0,lo=1,lb=1,t=0;   
  for (i=1;i<=N;i++){   
     scanf("%s",R[i]);
     scanf("%d",&P[i]);
     if (R[i][0]=='O'){
        t = max(oo+abs(P[i]-lo)+1,t+1);            
        oo = t;
        lo = P[i];            
     }
     else{
        t = max(bb+abs(P[i]-lb)+1,t+1);            
        bb = t;
        lb = P[i];   
     }  
  }   
  printf("Case #%d: %d\n",x,t);
}

int main(){
    int i,j,k;
    freopen("A.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
     for (k=1;k<=T;k++){
      scanf("%d",&N);
        work(k);    
     }
    return 0;   
}
