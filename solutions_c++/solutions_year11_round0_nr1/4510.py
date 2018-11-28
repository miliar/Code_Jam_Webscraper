#include <iostream>
#include <vector>

using namespace std;

int main()
{
  int t,n;
  cin>>t;
  for (int i=1;i<=t;i++)
  {
    cin>>n;
    int o=1,b=1,oi=0,bi=0;
    for (int j=0;j<n;j++)
    {
      char z;int t;
      cin>>z>>t;
     // cout<<z<<t<<endl;
      if (z=='O')
      {
        int d=abs(t-o)+1;
        o=t;
        oi+=d;
        if (oi<=bi)
          oi=bi+1;
      }
      else
      {
        int d=abs(t-b)+1;
        b=t;
        bi+=d;
        if (bi<=oi)
          bi=oi+1;
      }
      //cout<<o<<' '<<oi<<' '<<b<<' '<<bi<<endl;
    }
    cout<<"Case #"<<i<<": ";
    if (oi>bi)
      cout<<oi<<endl;
    else
      cout<<bi<<endl;
  }
  return 0;
}