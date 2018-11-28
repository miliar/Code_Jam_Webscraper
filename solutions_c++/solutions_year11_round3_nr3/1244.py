#include<iostream>
using namespace std;
int main()
{
  int t,n,c,l,h,k,i,j,z,arr[10000];
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  cin>>t;
  for(z=1;z<=t;z++)
  {
  k=0;
  cin>>n;
  cin>>l;
  cin>>h;
  for(i=0;i<n;i++)
  {
    cin>>arr[i];                 
  }  
  cout<<"Case #"<<z<<": ";
  for(i=l;i<=h;i++)
  {
     c =0 ;
     for(j=0;j<n;j++)
     {
       if(!((arr[j]%i==0)  || (i%arr[j] == 0)))
         { 
          c=1 ;
          break;              
         }           
     }
     if(c==0)
        {
             k=1;
             cout<<i;   
             break;      
        }           
  }  
  if(k==0)
     cout<<"NO";   
  cout<<endl;   
  }  
  return 0;    
}
