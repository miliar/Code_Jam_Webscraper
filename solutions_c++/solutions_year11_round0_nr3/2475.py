#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int tt;
    cin>>tt;
    for (int t=1;t<=tt;++t)
        {
             int n,m=INT_MAX,sum=0,flag=0;
             cin>>n;
             for (int i=1;i<=n;++i)
                 {
                      int k;
                      cin>>k;
                      if (k<m) m=k;
                      flag^=k;
                      sum+=k;
                  }
             cout<<"Case #"<<t<<": ";
             if (flag) cout<<"NO";else cout<<sum-m;
             cout<<endl;
         }
    return 0;
}
