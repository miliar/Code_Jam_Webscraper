#include<iostream>
using namespace std;
  
int main()
{
 int t,a[1000],n,s,p,i,j,x,y,z;
 
 cin>>t;
 for(i=1;i<=t;i++)
 {
  cin>>n>>s>>p;
  x=n;
  y=p;
  z=p;
  for(j=0;j<n;j++)
  {
    cin>>a[j];
  }
  if(3*p-4<=0)
  {
    y=-1;
  }
  if(3*p-4<=0)
 {
   z=-1;
 }
 
 for(j=0;j<n;j++)
 {
  if(a[j]<(p*3))
  {
   if(a[j]!=(3*p-2) && a[j]!=(3*p-1))
   {
    if(s==0)
    {
     x--;
    }
    else if(s!=0)
    {
     if(a[j]!=(3*y-4) && a[j]!=(3*z-3))
     {
      x--;
     }
     else
     {
      s--;
     }
    }
   }
  }
 } 
 cout<<"Case #"<<i<<": "<<x<<"\n";
 }
}