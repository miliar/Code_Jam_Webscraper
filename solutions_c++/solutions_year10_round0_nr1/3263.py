#include <cstdio>
using namespace std;
int main(){
  int T;
  scanf("%d",&T);
  for(int Case = 1; Case<=T; Case++){
    int N,K;
    scanf("%d%d",&N,&K);
    if((K+1)%(1<<N)==0)
      printf("Case #%d: ON\n", Case);
    else 
      printf("Case #%d: OFF\n", Case);          
  }
}
