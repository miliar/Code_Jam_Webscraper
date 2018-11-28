#include <iostream>
#include <cmath>
using namespace std;

int N, K;

bool snapper(){
  int t = (int)pow(2, N) - 1;
  if ( (t & K) == t )
    return true;
  return false;
}

int main(){
  int n; cin>>n;
  for ( int i = 0; i < n; ++i ){
    cin>>N>>K;
    cout<<"Case #"<<i+1<<": ";
    if (snapper())
      cout<<"ON"<<endl;
    else
      cout<<"OFF"<<endl;
  }
}
