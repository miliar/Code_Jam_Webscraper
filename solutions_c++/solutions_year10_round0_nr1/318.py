#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

typedef unsigned long long  uint;

int foo()
{
  int n , k;
  cin >> n >> k;
  return  ( (k+1) % ( 1<< n) == 0);
}

int main()
{
int t; cin >> t;
for (int i = 0;i<t;i++)
cout << "Case #" << i +1 << ": " << ( foo()?"ON":"OFF" ) <<endl;
}