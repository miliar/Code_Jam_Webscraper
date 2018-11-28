#include<iostream>
using namespace std;
int main()
{
    long long a,test,i,n,k,j,f,cnt=1;
    cin>>test;
    for(i=0;i<test;i++)
    {
      f=0;
      cin>>n>>k;
      for(j=0;j<n;j++)
        if(!(k&(1<<j)))
          {
            f=1;
            break;
          }
      if(f==1) cout<<"Case #"<<cnt++<<": OFF\n";
      else cout<<"Case #"<<cnt++<<": ON\n";
    }
    return 0;
}
