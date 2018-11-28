#include <iostream>
using namespace std;
int main() {
  int c, n, k, b, i=0;
  cin >> c;
  while(c--) {
    i++;
    cin >> n >> k;
    b=1<<n;
    k%=b;
    cout<<"Case #"<<i<<": ";
    if(b-1==k) cout<<"ON"; else cout<<"OFF";
    cout<<endl;
  }
  return 0;
}
