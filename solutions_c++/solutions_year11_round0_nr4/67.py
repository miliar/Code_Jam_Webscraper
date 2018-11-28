#include <iostream>

using namespace std;

int main()
{
  int t;
  cin>>t;
  int nums[2010];
  int n;
  for(int i=1; i<=t; i++)
  {
    cin>>n;
    for(int j=1; j<=n; j++)
      cin>>nums[j];
    
    int lugar=0;
    
    for(int j=1; j<=n; j++)
      if(nums[j]==j) lugar++;
      
     cout<<"Case #"<<i<<": "<<n-lugar<<".000000"<<endl;
     
    
  }
  
  
  return 0;
}