#include <cstdio>
#include <algorithm>

using namespace std;
const int M = 1000005;
typedef long long LL;

int mx[M];

int main() {
  mx[1]=0; mx[2]=1;
  for(int i=3;i<M;++i) {
    int prev=mx[i-1];
    int cur=prev;
    while(true) {
      int next=cur+1;
      int diff=i-next;
      if(mx[next]<diff){
        cur=next;
      } else break;
    }
    mx[i]=cur;
  }
  int d;
  scanf("%d",&d);
  for(int tc=1;tc<=d;++tc) {
    int A1,A2,B1,B2;
    scanf("%d %d %d %d",&A1,&A2,&B1,&B2);
    LL ret=0;
    for(int i=A1;i<=A2;++i)
      if(B1<=mx[i])
        ret+=min(B2,mx[i])-B1+1;
    for(int i=B1;i<=B2;++i)
      if(A1<=mx[i])
        ret+=min(A2,mx[i])-A1+1;
    printf("Case #%d: %lld\n",tc,ret);
  }
  return 0;
}
