#include<cstdio>
using namespace std;

int T,N,K;

int main(){
  int t;
  for(scanf("%d",&T),t=1;t<=T;t++){
    bool ans=true;
    scanf("%d %d",&N,&K);

    for(int i=0,j=1;i<N;i++,j<<=1)
      if((K&j)==0)ans=false;

    printf("Case #%d: %s\n",t,ans?"ON":"OFF");
  }
  return 0;
}
