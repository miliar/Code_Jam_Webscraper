#include<iostream>
#include<math.h>
using namespace std;

int main()
{
  int t,i;
  cin>>t;
  
  for(i=0;i<t;i++)
  {
    int n,k,j,l;
    cin>>n>>k;
    
    
    int num=pow(2,n);
    
    cout<<"Case #"<<i+1<<": ";
    
    if((k+1)%num==0&&k!=0)
      cout<<"ON";
    else
      cout<<"OFF";
    
    cout<<"\n";
    
    
  }
  
  return 0;
}