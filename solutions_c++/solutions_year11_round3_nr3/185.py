#include <cstdio>
#include <algorithm>
#include <cstring>
#include <map>
#include <cmath>
#include <vector>
#include <set>
#include <cstdlib>
using namespace std;
int Q,N,ok;
long long L,H,best;
long long fre[10240];
int main(){
  scanf("%d",&Q);
  for(int q=1;q<=Q;q++){
    scanf("%d %lld %lld",&N,&L,&H);
    for(int i=0;i<N;i++)
      scanf("%lld",&fre[i]);
    best=-1;
    for(long long i=L;i<=H;i++){
      ok=1;
      for(int j=0;j<N;j++){
        if(((fre[j]%i)!=0) && ((i%fre[j])!=0))
          ok=0;
      }
      if (ok && best<0)
        best=i;
    }
    if (best>0)
      printf("Case #%d: %lld\n",q,best);
    else
      printf("Case #%d: NO\n",q);
    
  }
}
