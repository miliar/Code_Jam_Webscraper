#include <iostream>
#include <algorithm>
using namespace std;
int main(){
  int t;
  cin >> t;
  for (int i=1; i<=t;++i){
    int n, sum, xsum,minp;
    sum = xsum = 0;
    minp = 1000001;
    cin >> n;
    for (int j = 0; j<n;++j){
      int k;
      cin >> k;
      sum+=k;
      xsum^=k;
      minp=min(k,minp);
    }
    cout<<"Case #"<<i<< ": ";
    if (xsum!=0){
      cout << "NO\n";
    }else
      cout << sum-minp << "\n";
  }
}

