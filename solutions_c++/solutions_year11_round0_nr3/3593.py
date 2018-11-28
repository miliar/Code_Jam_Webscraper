#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <string>
#include <algorithm>
#include <cmath>

#define FOR(i,n) for(i=0;i<n;i++)
#define MAXN 1111

using namespace std;

int T,t,N;

int main(int argc, char *argv[]){
  int i,a,b,sum,m;
  scanf("%d",&T);
  FOR(t,T){
    scanf("%d",&N);
    b=0; m=MAXN*MAXN,sum=0;
    FOR(i,N){
      scanf("%d",&a);
      b^=a;
      sum+=a;
      m=min(m,a);
    }
    if(b) printf("Case #%d: NO\n",t+1);
    else printf("Case #%d: %d\n",t+1,sum-m);
  }
  return 0;
}
