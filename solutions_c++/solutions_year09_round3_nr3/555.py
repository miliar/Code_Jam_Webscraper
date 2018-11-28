#include <iostream>
#include <vector>
#include <algorithm>
#define REP(i,n) for(i=0;i<n;++i)
#define FOR(i,a,b) for(i=0;i<=b;++i)
using namespace std;

int tt,t,p,q,i;
int x;
vector<int> v;
int a[200],dd[10];
int sum, best,c;

int go(){
  int j,k,am;
  REP(j,q){
    if (dd[j]==0){
      dd[j]=1;
      am=0;
      k=v[j]-1;
      while (k>=1 && a[k]!=0) { ++am; --k; }
      k=v[j]+1;
      while (k<=p && a[k]!=0) { ++am; ++k; }
      a[v[j]]=0;
      sum+=am;
      ++c;
      if (c==q) {
        if (best>sum) best=sum;
      }
      else {
        go(); 
      }
      --c;
      sum-=am;
      a[v[j]]=1;
      dd[j]=0;
    }
  }
}

int main(){
  freopen("1cc.in","r",stdin);
  freopen("1cc.out","w",stdout);
  cin >> t;
  REP(tt,t){
    cin >> p >> q;
    v.clear();
    REP(i,q) { cin >> x; v.push_back(x); }
    sum=0; best=(1<<31)-1; c=0;
    FOR(i,1,p) a[i]=1;
    memset(dd,0,sizeof(dd));
    go();
    cout << "Case #" << tt+1 << ": " << best << endl;
  }
}
