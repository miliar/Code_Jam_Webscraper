#include<stdio.h>
#include<vector>
using namespace std;

#define PB push_back
#define LL(X) ((ll)(X))
#define SZ(X) ((int)X.size())
#define CLR(X) memset(X,0,sizeof(X))
typedef long long ll;
typedef vector<ll> VL;

int main(){
  int T, R, k, N;
  int g[1000];
  scanf("%d",&T);
  for(int i=1; i<=T; i++){
    ll ret=0;
    scanf("%d %d %d",&R, &k, &N);
    int last=N-1, rot=0;
    for(int j=0; j<N; j++) scanf("%d",&g[j]);
    {
      ll x=0;
      for(int j=0; j<N; j++) if(g[j]>k) {    printf("Case #%d: %lld\n", i, x); continue;} else {
        x+=g[j];
      }
      if(x<=k){printf("Case #%d: %lld\n", i, R*x); continue;}
    }
    do{
      ll s=0;
      rot=(last+1)%N;
      while(1){
        last++; last%=N;
        if(s+LL(g[last])<=LL(k)) s+=LL(g[last]); else {last=(last+N-1)%N;break;}
      }
      ret+=s;
      R--;
    } while(R);

    printf("Case #%d: %lld\n", i, ret);
  }
  return 0;
}
