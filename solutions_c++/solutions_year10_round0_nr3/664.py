#include<cstdio>
#include<algorithm>
using namespace std;

typedef long long L;

typedef pair<int,L> P;

int main(){
  int T;
  scanf(" %d",&T);
  for(int i=0;i<T;++i){
    int R,K,N;
    int G[1000];
    scanf(" %d %d %d",&R,&K,&N);
    for(int j=0;j<N;++j){
      scanf(" %d",G+j);
    }
    printf("Case #%d: ",i+1);
    P cash[1000];
    fill_n(cash,1000,P(-1,0));
    cash[0]=P(0,0);
    int pos=0;
    L res=0;
    for(int j=1;;++j){
      if(j>R){
        goto end;
      }
      L buf=0;
      int begin=pos;
      for(int k=0;buf+G[pos]<=K;++k){
        buf+=G[pos++];
        pos%=N;
        if(pos==begin)break;
      }
      res+=buf;
      if(cash[pos].first>=0){
        res+=(res-cash[pos].second)*((R-j)/(j-cash[pos].first));
        R=(R-j)%(j-cash[pos].first);
        break;
      }
      cash[pos]=P(j,res);
    }
    for(int j=0;j<R;++j){
      int buf=0;
      for(int k=0;buf+G[pos]<=K;++k){
        buf+=G[pos++];
        pos%=N;
      }
      res+=buf;
    }
  end:;
    printf("%lld\n",res);
  }
  return 0;
}
