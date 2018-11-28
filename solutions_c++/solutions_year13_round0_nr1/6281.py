#include <string>
#include <iostream>
using namespace std;

string mp[4];

bool end() {
  for (int i=0; i<4; ++i) {
    for (int j=0; j<4; ++j)
      if (mp[i][j] == '.') return false;
  }
  return true;
}

bool win(char x) {
  // v
  for (int i=0; i<4; ++i) {
    bool okv = true, okh = true;
    for (int j=0; j<4; ++j) {
      okv = okv && (mp[j][i] == x || mp[j][i] == 'T');
      okh = okh && (mp[i][j] == x || mp[i][j] == 'T');
    }
    if (okv || okh) return true;
  }

  bool o1 = true, o2 = true;
  for(int i=0; i<4; ++i) {
    o1 = o1 && (mp[i][i] == x || mp[i][i] == 'T');
    o2 = o2 && (mp[i][3-i] == x || mp[i][3-i] == 'T');
  }
  if (o1 || o2) return true;
  return false;
}

int main() {
  int T;
  cin>>T;
  for (int tc=1; tc<=T; ++tc) {
    for (int i=0; i<4; ++i) cin>>mp[i];
    bool winx = false, wino = false;
    bool endgame = end();
    winx = win('X'); wino = win('O');

    cout<<"Case #"<<tc<<": ";
    if (winx) cout<<"X won"<<endl;
    else if (wino) cout<<"O won"<<endl;
    else if (endgame) cout<<"Draw"<<endl;
    else cout<<"Game has not completed"<<endl;
  }
}
