#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main() {
  int L,D,N;
  cin >> L >> D >> N;
  vector<string> w(D);
  for (int i=0; i<D; ++i) {
    cin >> w[i];
  }
  for (int in=0; in<N; ++in) {
    string s;
    cin >> s;
    stringstream ss;
    bool block=0;
    for (int i=0; i<s.size(); ++i) {
      if (s[i]=='(') block=1;
      else if (s[i]==')') {
        block=0;
        ss << endl;
      }
      else {
        ss << s[i];
        if (!block) ss << endl;
      }
    }
    vector<bool> can(D,1);
    for (int i=0; i<L; ++i) {
      vector<bool> let(256,0);
      string t;
      ss >> t;
      for (int j=0; j<t.size(); ++j) {
        let[t[j]]=1;
      }
      for (int j=0; j<D; ++j) {
        if (!let[w[j][i]]) can[j]=0;
      }
    }
    int ans=0;
    for (int i=0; i<D; ++i) {
      if (can[i]) ++ans;
    }
    cout << "Case #" << in+1 << ": " << ans << endl;
  }
}
