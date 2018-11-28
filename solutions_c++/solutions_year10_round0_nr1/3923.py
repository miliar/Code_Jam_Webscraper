#include <iostream>
using namespace std;


int main()
{
  int t, n, k;
  int i;
  cin>>t;
  for(i = 1; i <= t; i ++){
    cin>>n>>k;
    if ((k+1) & ((1<<n) - 1)) cout<<"Case #"<<i<<": OFF"<<endl;
    else cout<<"Case #"<<i<<": ON"<<endl;
  }
  
  return 0;
}
