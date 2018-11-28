#include<iostream>
#include<cmath>
using namespace std;
int main()
{
unsigned long int n,k,t, c,l,m=1;
cin>>t;
while(m<=t)
{
  cin>>n>>k;
  c=1;
  c=c<<n;
  l=k&(c-1);
  if(l+1==c)
  cout<<"Case #"<<m<<": ON\n";
      else
      cout<<"Case #"<<m<<": OFF\n";
  m++;
}
return 0;
}
