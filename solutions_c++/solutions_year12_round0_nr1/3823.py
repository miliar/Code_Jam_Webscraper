#include <iostream>
#include <string>
#include <map>

using namespace std;

string S;

char M[] = "yhesocvxduiglbkrztnwjpfmaq";

string solve() {
  string R;

  for (auto c : S) {
    if (c == ' ') {
      R.append( 1, c );
    } else {
      R.append( 1, M[c-'a'] );
    }
  }

  return R;
}

int main() {
  int T;
  cin >> T;
  getline(cin, S);
  for (int tc=1; tc<=T; ++tc) {
    getline(cin, S);
    cout << "Case #" << tc << ": " << solve() << endl;
  }
}
