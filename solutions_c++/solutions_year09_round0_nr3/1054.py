#include <iostream>
#include <string>
#include <vector>

using namespace std;

const string wel="welcome to code jam";
const int MOD=10000;

int main() {
  int n;
  cin >> n;
  string s;
  getline(cin,s);
  for (int in=0; in<n; ++in) {
    getline(cin,s);
    vector<vector<int> > pos(wel.size());
    for (int i=0; i<wel.size(); ++i) {
      for (int j=0; j<s.size(); ++j) {
        if (s[j]==wel[i]) pos[i].push_back(j);
      }
    }
    vector<vector<int> > dp(s.size(),vector<int>(wel.size(),0));
    int ans=0;
    for (int i=0; i<dp.size(); ++i) {
      if (s[i]==wel[0]) dp[i][0]=1;
      for (int j=1; j<wel.size(); ++j) if (s[i]==wel[j]) {
        for (int k=0; k<pos[j-1].size() && pos[j-1][k]<i; ++k) {
          dp[i][j]+=dp[pos[j-1][k]][j-1];
          dp[i][j]%=MOD;
        }
      }
      ans+=dp[i][int(wel.size())-1];
      ans%=MOD;
    }
    cout << "Case #" << in+1 << ": ";
    if (ans<1000) cout << 0;
    if (ans<100) cout << 0;
    if (ans<10) cout << 0;
    cout << ans << endl;
  }
}
