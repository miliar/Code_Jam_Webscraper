#include<iostream>
#include<vector>
#include<stdio.h>
#include<cmath>
#include<cstdlib>
using namespace std;


int main()
{
int t,w=0;
  cin>>t;
  while(t--)
  {
  w++;
   int i,j;
   long long n,m,x,y,z;
   cin>>n>>m>>x>>y>>z;
   long long  a[n+1],b[n+1],c[n+1],ans=0;
   for(i=0;i<m;i++)
     cin>>a[i];
  for(i=0;i<n;i++)
  {
    b[i]=a[i%m];
    a[i%m]=(x*a[i%m] +y*(i + 1))%z;
  }
  for(i=0;i<n;i++)
  {
    c[i]=1;
  }
  for(i=0;i<n;i++)
  {
    for(j=0;j<i;j++)
    {
      if(b[i]>b[j])
      {
        c[i]=(c[i]+c[j])%1000000007;
      }
    }
 }
 
 for(i=0;i<n;i++)
  ans=(ans+c[i])%1000000007;
  
    
  
  printf("Case #%d: %lld\n",w,ans);
  }
}
