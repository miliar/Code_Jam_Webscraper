#include<iostream>
#include<cstdlib>
#include<algorithm>
using namespace std;

main(){
  int te;
  cin>>te;
  for(int tc=1;tc<=te;tc++){
    int n;
    int lp[2]={1,1},t[2]={0},cur=0;
    cin>>n;
    for(int i=0;i<n;i++){
      char a;int v,ind;cin>>a>>v;
      if (a == 'O')ind=0;
      else ind=1;
      cur=max(cur+1,t[ind]+abs(lp[ind]-v)+1);
      t[ind]=cur;
      lp[ind]=v;
    }
    cout <<"Case #" << tc << ": " << cur << endl;
  }
  return false;
}
