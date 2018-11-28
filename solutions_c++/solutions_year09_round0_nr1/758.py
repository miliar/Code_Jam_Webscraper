#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

string A[5000];
bool OK[15][26];

int main() {
  int L, D, N;
  cin >> L >> D >> N;
  for(int i = 0; i < D; i++) cin >> A[i];
  for(int t = 1; t <= N; t++) {
    string pat; cin >> pat;
    int ind = 0;
    bool in = false;
    memset(OK, 0, sizeof(OK));
    for(int j = 0; j < pat.size(); j++) {
      int v = -1;
      if(pat[j] == '(') {
        in = true;
      } else if (pat[j] == ')') {
        in = false;
        ind++;
      } else {
        v = pat[j] - 'a';
      }
      if(v != -1) {
        OK[ind][v] = true;
        if(!in) ind++;
      }
    }
    int res = 0;
    for(int i = 0; i < D; i++) {
      bool ok = true;
      for(int j = 0; j < L && ok; j++) ok = OK[j][A[i][j] - 'a'];
      res += ok;
    }
    cout << "Case #" << t << ": " << res << endl;
  }
}
