#include <cstring>
#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>

using namespace std;

void solve(){
  int n; int xr = 0;
  cin>>n; vector<int>v;
  for(int i=0;i<n;++i){
   int x; cin>>x; v.push_back(x); xr ^= x;
  }
  if(xr!=0) cout<<"NO"<<endl;
  else {
    sort(v.begin(),v.end());
    int sm = 0;
    for(int i=1;i<v.size();++i) sm += v[i];
    cout<<sm<<endl; 
  }
}

int main(){
  int tcase; cin>>tcase;
  for(int tc=1;tc<=tcase;++tc){
    cout<<"Case #"<<tc<<": "; solve();
  }
  return 0;
}
