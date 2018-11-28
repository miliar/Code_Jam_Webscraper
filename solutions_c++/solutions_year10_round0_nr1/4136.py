#include <iostream>
using namespace std;
int main()
{
  long long t,n,k,x=1,i,j;
  cin>>t;
  for(i=1;i<=t;i++)
  {
    cin>>n>>k;
    if(k==0) cout<<"Case #"<<i<<": OFF"<<endl;
    else
    {
    x=1;
    for(j=1;j<=n;j++)
    {
      x*=2;
    }
    if(k%x==x-1) cout<<"Case #"<<i<<": ON"<<endl;
    else cout<<"Case #"<<i<<": OFF"<<endl;
    }
  }
  return 0;
}