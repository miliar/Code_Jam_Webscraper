#include<iostream>
using namespace std;
long a[31];
int main(){
  int t;
  cin>> t;
  int o=t;
  a[0] = 1;
  for (int i = 1; i <31;++i)
    a[i]=a[i-1]*2;
  while (t--){
    int n,k;
    cin >> n >> k;
    int pp = a[n];
    cout <<"Case #"<<o-t <<": ";
    if (k%pp==pp-1)
      cout <<"ON\n";
    else
      cout <<"OFF\n";
      
  }


}
