#include<iostream>
using namespace std;
int main()
{
  int t,n,k,cas=1,i;
  long long p,d;
  cin>>t;
  while(t--)
  {
    cin>>n>>k;
    p=1<<n;
    d=k%p;
    if(d==p-1)
    cout<<"Case #"<<cas++<<": ON"<<endl;
    else
    cout<<"Case #"<<cas++<<": OFF"<<endl;
  }
  return 0;
}
  
     
