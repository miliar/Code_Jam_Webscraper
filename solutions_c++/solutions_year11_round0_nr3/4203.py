#include<iostream>
using namespace std;

int main()
{
 freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);   
 int t,n,arr[1000],x,sum,res[100],k;
 cin>>t;
 for(int p=0;p<t;p++)
 {cin>>n;
  for(int i=0;i<n;i++)
   cin>>arr[i];
  x=0;
  sum=0;
  for(int i=0;i<n;i++)
   x=x^arr[i];
  if(x!=0)
   res[p]=0;
  else
  {k=arr[0];
   for(int i=0;i<n;i++)
   {
    if(arr[i]<k)
      k=arr[i];
    sum=sum+arr[i];
   }
   sum=sum-k;
   res[p]=sum;
  }
  }
  for(int p=0;p<t;p++)
  {
          if(res[p]!=0)
               cout<<"Case #"<<(p+1)<<": "<<res[p]<<endl;
          else
               cout<<"Case #"<<(p+1)<<": NO"<<endl;
  }
  cin>>x;            
  return 0;
}
   
