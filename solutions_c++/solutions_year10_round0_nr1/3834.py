#include<iostream>
#include<cmath>

using namespace std;


int main()
{
  int t;
  cin>>t;
  for(int i =0;i<t;i++)
  {
    cout<<"Case #"<<i+1<<": ";
    int n,k;
    cin>>n>>k;
    int x = pow(2,n);
    if(k%x == x-1)
      cout<<"ON"<<endl;
    else
      cout<<"OFF"<<endl;
  }
  return 0;
}
