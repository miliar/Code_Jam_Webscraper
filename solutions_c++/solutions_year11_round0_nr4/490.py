#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int T,N,P[1111];
bool used[1111];

void work(int x){
  int i,j,k,t=N;   
  for (i=1;i<=N;i++){   
     scanf("%d",&P[i]);
     used[i] = false;   
  }   

  for (i=1;i<=N;i++){
        if (P[i]==i) t--;
      }
  printf("Case #%d: %.6lf\n",x,(double)(t));
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
