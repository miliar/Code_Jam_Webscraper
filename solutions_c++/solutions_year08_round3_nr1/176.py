#include<iostream>
#include<vector>
#include<stdio.h>
#include<cmath>
#include<cstdlib>
using namespace std;
bool fun(long long a,long long b)
{
return a>b;
}
int main()
{
int t,m=0;
  cin>>t;
  while(t--)
  {
  m++;
   int i,j,l;
   int p,k,n;
    cin>>p>>k>>l;
    long long f[l+1],ans=0,temp=1;
    for(i=0;i<l;i++)
     cin>>f[i];
    
    sort(f,f+l,fun);
    i=0;temp=1;
    while(i<l)
    {
      j=0;
      while(j<k)
      {
    //  cout<<f[i]<<endl;
        ans+=f[i]*temp;
        j++;
        i++;
        if(i==l)
         break;
       // cout<<ans<<" ";
      }
      temp++;
   }
    
    
  

  
  
  printf("Case #%d: %lld\n",m,ans);
  }
  
}
