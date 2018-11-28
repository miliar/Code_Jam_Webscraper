#include <iostream>

using namespace std;

int main(){
  int c;
  cin>>c;
  for(int i=1;i<=c;i++){
    int n,k,b,t,ans=0,p=0;
    int x[50],v[50];
    cin>>n>>k>>b>>t;
    for(int j=0;j<n;j++)
      cin>>x[j];
    for(int j=0;j<n;j++)
      cin>>v[j];
    for(int j=n-1;j>=0;j--)
      if((b-x[j]) <= t*(long long)v[j]){
        ans+=p;
        if(--k==0) break;
      }
      else
        p++;
    cout<<"Case #"<<i<<": ";
    if(k)
      cout<<"IMPOSSIBLE"<<endl;
    else
      cout<<ans<<endl;
  }
  return 0;
}

