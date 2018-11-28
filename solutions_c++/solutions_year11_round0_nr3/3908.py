#include <iostream>
#include <vector>
using namespace std;

int main() {
  int T;
  cin>>T;
  for (int t = 1; t<= T; ++t) {
    int N;
    cin>>N;
    vector<int> x;
    int s = 0;
    for (int i = 0; i < N; ++i) {
      int xx; cin>>xx; x.push_back(xx); s+=xx;
    }
    int f = -1;
    for (int i = 0; i < (1<<N) - 1; ++i) {
      vector<int> p,q;
      for (int j=0; j<N; ++j) {
        if ((1<<j) & i) p.push_back(x[j]);  else q.push_back(x[j]); 
      }
      int pp,qq; pp=qq=0;
      for (int j=0; j<p.size();++j) pp ^= p[j];
      for (int j=0;j<q.size();++j) qq += q[j];
      if (pp == qq && f < s - qq) { f = s - qq; }
    }
    cout<<"Case #"<<t<<": ";
    if (f == -1) cout<<"NO"; else cout<<f;
    cout<<endl;
  }

  return 0;
}
