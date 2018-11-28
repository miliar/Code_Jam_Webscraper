#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int iT=1; iT<=T; ++iT) {
    int n;
    cin >> n;
    vector<int> v(n);
    for (int i=0; i<n; ++i) {
      string s;
      cin >> s;
      int j=n;
      for (; j>0 && s[j-1]!='1'; --j);
      v[i]=j;
    }
    int ans=0;
    for (int i=0; i<n; ++i) {
      int clo=-1;
      for (int j=i; j<n && clo==-1; ++j) {
        if (v[j]<=i+1) clo=j;
      }
      for (int j=clo; j>i; --j) {
        swap(v[j],v[j-1]);
        ++ans;
      }
    }
    cout << "Case #" << iT << ": " << ans << endl;
  }
}
