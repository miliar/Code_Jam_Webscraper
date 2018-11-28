#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

// [0,30]
int f(int x) {
  return (int)floor((x-1)/3.0)+1;
}

// [2,28]
int g(int x) {
  return (int)floor((x-2)/3.0)+2;
}

int main() {
  int T; cin >> T;
  
  for(int testcase=1; testcase<=T; testcase++) {
    int N, S, p; cin >> N >> S >> p;
    vector<int> t(N);
    for(int i=0; i<N; i++) cin >> t[i];
    sort(t.begin(), t.end());
    
    int ans = 0;
    for(int i=0; i<N; i++) {
      if(t[i] >= 29) { ans+=f(t[i])>=p; continue; }
      if(t[i] <= 1) { ans+=f(t[i])>=p; continue; }
      if(g(t[i])>=p&&S) { ans++; S--; continue; }
      if(f(t[i])>=p) { ans++; continue; }
    }
    
    cout << "Case #" << testcase << ": " << ans << endl;
  }
  
  return 0;
}
