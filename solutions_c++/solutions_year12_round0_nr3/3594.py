#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> f(int i) {
  vector<int> v;
  while(i) { v.push_back(i%10); i/=10; }
  reverse(v.begin(), v.end());
  return v;
}

bool g(vector<int> v, vector<int> w) {
  if(v.size() != w.size()) return false;
  for(int i=0; i<v.size(); i++) {
    bool ok = true;
    for(int j=0; j<v.size()&&ok; j++) {
      if(v[j]!=w[(j+i)%v.size()]) ok=false;
    }
    if(ok) return true;
  }
  return false;
}

int main() {
  int T; cin >> T;
  for(int testcase=1; testcase<=T; testcase++) {
    int A, B; cin >> A >> B;
    int ans = 0;
    for(int i=A; i<=B; i++) {
      for(int j=i+1; j<=B; j++) {
        if(g(f(i),f(j))) ans++;
      }
    }
    cout << "Case #" << testcase << ": " << ans << endl;
  }
  return 0;
}
