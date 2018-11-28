#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

long long gcd( long long a , long long b )
{
  if( !b )
      return a;
  
  return gcd( b , ( ( a % b ) + b ) % b ) ; 
  
}

int main()
{
int t;
cin>>t;
int test = 1;
while(t--)
{
int n;
cin>>n;
vector<long long> a;
vector<long long> b;
a.resize(n);
for(int i = 0 ; i < n ; i++) 
   cin>>a[i];
  
for(int i = 0 ; i < n - 1 ; i++)
    for(int j = i+1 ; j < n ; j++)
	b.push_back( abs( a[i] - a[j] ) );
  
long long gc = 0;

for(int i = 0 ; i < b.size() ; i++)
  gc = gcd( max(gc , b[i]) , min( gc,b[i] ) );


long long y;

y = ( (a[0] % gc ) + gc ) % gc;

if( y > 0 )
  y = ( gc - y );

cout<<"Case #"<<test<<": "<<y<<endl;
  
test++;  
}  
  
  
return 0;  
}