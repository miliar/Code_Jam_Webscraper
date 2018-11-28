#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int main (){
  int t,u,n,s,p,i,a[200];
  cin>>t;
  for (u=0;u<t;u++){
    cin>>n>>s>>p;
    for (i=0;i<n;i++) cin>>a[i];
    sort(a,a+n,greater<int>());
    for (i=0;i<n;i++){
      if (a[i]>=3*p-2) continue; 
      if (a[i]<2||a[i]<3*p-4||s==0) break;
      s--;
    }
    cout<<"Case #"<<(u+1)<<": "<<i<<endl;
  }
  return 0;
}
