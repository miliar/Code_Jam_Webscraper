#include<iostream>
#include<cassert>
using namespace std;

int main()
{
int t;
cin>>t;
int i = 1;
long long n , k;
while( i<= t )
{
  cin>>n>>k;
 
  long long a = (1<<n);
  long long b = a-1;
  
  k = ( ( k % ( a ) ) + (a) ) % (a);
  assert(k>=0);
  assert(a>=0);
  assert(b>=0);
  if( k < b )
    cout<<"Case #"<<i<<": OFF"<<endl;
  else
    cout<<"Case #"<<i<<": ON"<<endl;

i++;
}  
return 0;  
}