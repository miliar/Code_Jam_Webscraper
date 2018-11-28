#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <deque>
#include <queue>
#include <set>
using namespace std;
typedef long double real;

struct vine_t{
  int x;
  int length;

  bool operator<(vine_t const& other) const{
    return x<other.x;
  }
};

bool solve(){
  int n; cin>>n;

  static vine_t vine[10008];
  static real best[10008];

  for (int i=0; i<n; i++) cin>>vine[i].x>>vine[i].length;
  for (int i=1; i<=n+2; i++) best[i]=-100;
  best[0]=abs(vine[0].x);

  int want; cin>>want;

  queue<int> valid;
  valid.push(0);
  for (int i=1; i<n; i++){
    while (not valid.empty()){
      auto f=valid.front();

      real dx=abs(vine[i].x-vine[f].x);
      real dy=min((real)vine[i].length,dx);
      if (dx>best[f]) {valid.pop(); continue;}

      if (dy>=0){
        best[i]=max(best[i],dy);
        valid.push(i);
      }
      break;
    }
  }
/*
  for (int i=0; i<n; i++)
    for (int j=0; j<n; j++) if (best[i]>=0.0L)
      for (int k=0; k<n; k++){
        real dx=abs(vine[k].x-vine[j].x);
        if (dx>best[j]) continue;
        real dy=min((real)vine[k].length,dx);
        if (dy>=0){
          best[k]=max(best[k],dy);
        }
      }
*/
  for (int i=n; i--;)
    if (abs(vine[i].x-want)<=best[i]+1e-10L)
      return true;

  return false;

}

int main(){
  freopen("A-large.in","r",stdin);
  freopen("A.out","w",stdout);

  ios::sync_with_stdio(false);
  int tests; cin>>tests; for (int i=1; i<=tests; i++) cout<<"Case #"<<i<<": "<<(solve()?"YES":"NO")<<endl;
}
