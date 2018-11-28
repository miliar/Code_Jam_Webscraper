#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
inline int len(int a) {
  int n(0);
  while(a) {
    ++n;
    a/=10;
  }
  return n;
}
inline int ten_n(int n) {
  int c(1);
  for(int i(0);i!=n;++i) {
    c*=10;
  }
  return c;
}
inline int move(int a,int p) {
  int n(len(a)-p),c(a%ten_n(p));
  return a/ten_n(p)+c*ten_n(n);
}
main() {
  int n;
  cin>>n;
  for(int i(0);i!=n;++i) {
    int a,b,result(0);
    cin>>a>>b;
    int lent(len(a));
    for(int k(a);k!=b;++k) {
      int p(k);
      vector<int> CLOSE;
      for(int q(1);q!=lent;++q) {
        p = move(k,q);
        if(p<=b && p>k && !count(CLOSE.begin(),CLOSE.end(),p)) {
          CLOSE.push_back(p);
          ++result;
        }
      }
      CLOSE.clear();
    }
    cout<<"Case #"<<i+1<<": ";
    cout<<result<<endl;
  }
  return 0;
}
