#include<iostream>
using namespace std;

int main()
{
  int ci,cn,n,k;
  cin>>cn;
  for(ci=1;ci<=cn;++ci)
  {
    cin>>n>>k;
    cout<<"Case #"<<ci<<": ";
    if((k&((1<<n)-1))==(1<<n)-1) cout<<"ON"<<endl;
    else cout<<"OFF"<<endl;
  }
}

