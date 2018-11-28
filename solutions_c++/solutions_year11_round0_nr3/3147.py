#include <iostream>
#include <map>
using namespace std;
int n;
long long a[1002];
#define OFFSET (long long)1e9
#define INF (long long)1e10
map<long long,long long> mp[1002];
long long encode(long long x, long long y){
  return x * OFFSET+y ;
}
void solve(int nown, int b,int c,long long d,long long e){
  long long tmp = encode(b,c);
  //cout << "nown = " << nown << " " <<  b << " " << c << " " << d << " " << e << endl;
  if(nown==n){
   // mp[nown][tmp] = max(mp[nown][tmp],max(d,e));
     mp[nown][tmp] = max(mp[nown][tmp],max(d,e));
    return; 
  }
  if(mp[nown].count(tmp)){
   // mp[nown][tmp]= max(mp[nown][tmp], max(d,e));
    return;
  }
  mp[nown][tmp] = max(d,e);
  solve(nown+1, b^a[nown],c,d+a[nown],e);
  solve(nown+1,b,c^a[nown],d,e+a[nown]);
  
}
int main(){
  int t,kase=1;
  long long x,y;
  cin >> t;
  while(t--){
    cin >> n;
    long long sum= 0;
    for(int i =0; i < n; i++){
      cin >> a[i];
      sum += a[i];
      mp[i].clear();
    }
   // sort(a,a+n, greater<long long>());
    mp[n].clear();
    solve(0,0,0,0,0);
    cout << "Case #" << kase++ <<": ";
    long long ans = -1;
    for(map<long long ,long long>::iterator p =mp[n].begin();p!=mp[n].end();p++){
      x=p->first/OFFSET;
      y=p->first%OFFSET;
      if((sum-p->second)!=0 && (p->second)!=0 && x==y){
        ans = max(ans,sum- p->second);
        ans = max(ans,p->second);
      }
    }
    if(ans==-1){
      cout << "NO";
    }
    else{
      cout << ans ;     
    }
    cout << endl;
  }
  return 0;    
}
