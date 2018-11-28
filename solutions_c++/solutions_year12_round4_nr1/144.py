#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
#include <set>
#define MAXN 10005 
using namespace std;

int testcase,N,L[MAXN],D[MAXN],X,P[MAXN],t1,lo,hi,mid,T[MAXN];
struct cmp{
  bool operator()(int a,int b){
    if(P[a] != P[b]) return P[a] > P[b];
    return a < b;
  }
};
set <int,cmp> S;

int query(int x){
  if(!x) return 0;
  int sum = 0;
  for(;x>0;x-=(x&-x)) sum += T[x];
  return sum;
}
void update(int x){
  for(;x<=N;x+=(x&-x)) ++T[x];
}

int main(){
  freopen("A-large.in","r",stdin);
  freopen("A.out","w",stdout);
  scanf("%d",&testcase);
  for(int TC=1;TC<=testcase;++TC){
    scanf("%d",&N);
    for(int i=1;i<=N;++i) scanf("%d%d",&D[i],&L[i]);
    scanf("%d",&D[N+1]);
    P[N+1] = D[N+1];
    S.clear();
    S.insert(N+1);
    memset(T,0,sizeof(T));
    P[1] = -1;
    printf("Case #%d: ",TC);
    ++N;
  //  printf("currently %d %d\n",*S.begin(),P[*S.begin()]);
    for(int i=N-1;i>0;--i){
     // printf("at %d with D[%d] = %d\n",i,i,D[i]);
      while(!S.empty() && P[*S.begin()] >= D[i]){
       // printf("remove %d\n",*S.begin());
        update(*S.begin());
        S.erase(*S.begin());
      }
      lo = i+1, hi = lower_bound(D+1,D+N,D[i]+L[i])-D;
      if(D[hi] > D[i]+L[i]) --hi;
    //  printf("%d can reach %d\n",i,hi);
      while(hi > lo){
        mid = (hi+lo)/2;
        if(query(mid) - query(i) > 0) hi = mid;
        else lo = mid+1;
      }
      if(lo <= hi && query(hi) - query(hi-1) > 0){
        P[i] = D[i] - (D[hi]-D[i]);
        S.insert(i);
    //    printf("P[%d] = %d\n",i,P[i]);
      }
    }
    if(P[1] >= 0) printf("YES\n");
    else printf("NO\n");
  }
 // system("pause");
}
