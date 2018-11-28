#include <iostream>
#include <vector>
#include <cstring>
#include <iomanip>

using namespace std;

string s = "welcome to code jam";
int DP[30];

int main() {
  int T; cin >> T;
  for(int t = 0; t <= T; t++) {
    string A; getline(cin, A); if(!t) continue;
    memset(DP, 0, sizeof(DP));
    DP[0] = 1;
    for(int i = 0; i < A.size(); i++) {
      for(int j = s.size() - 1; j >= 0; j--) {
        if(A[i] == s[j]) {
          DP[j + 1] += DP[j];
          DP[j + 1] %= 10000;
        }
      }
    }
    cout << "Case #" << t << ": " << setw(4) << setfill('0') << DP[s.size()] << endl;;
  }
}
