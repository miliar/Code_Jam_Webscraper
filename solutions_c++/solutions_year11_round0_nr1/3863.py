#include<iostream>
#include<cmath>
using namespace std;

int main()
{
  int n; 
  cin>>n;
  for(int i=0;i<n;i++)
  {
    int nt;
    cin>>nt;
    char c; int s;
    int cO,cB;
    cO=cB=1;
    int p,q;
    p=q=0;
    while(nt--)
    {
       cin>>c>>s;
       if(c=='O')
       {
         p = max( p +(int) abs((float)s-cO),q)+1;
          cO=s; 
         continue;
       }
         q = max( q +(int) abs((float)s-cB),p)+1;
          cB=s; 
    }
    cout<<"Case #"<<i+1<<": "<<max(p,q)<<endl;
  }
}