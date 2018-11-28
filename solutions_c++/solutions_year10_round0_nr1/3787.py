#include<iostream>
#include<cmath>

using namespace std;

int main()
{
  bool result;
  long long n,k;
  long long inter;
  int t,i;
  cin>>t;
  for(i=1;i<=t;i++)
  {
    cin>>n>>k;
    inter = (int)pow((double)2,(double)n);       	
    if((k+1)%inter == 0)
    {
      cout<<"Case #"<<i<<": ON\n"; 
    }
    else
    {
      cout<<"Case #"<<i<<": OFF\n";
    }
  }
  return 0;
}
