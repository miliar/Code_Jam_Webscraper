#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <vector>

#define mp make_pair
#define pb push_back

#define REP(i,n) for(int i=0; i < (n); ++i)

using namespace std;


void solve()
{
  string a[5];

  REP(i,5) getline(cin, a[i]);

  int status = -1;

  for(int i = 0; i < 4; ++i) {
    bool checkO = true;
    bool checkX = true;

    for(int j = 0; j < 4; ++j) {
      if(a[i][j] == 'T') continue;
      if(a[i][j] != 'O') checkO = false;
      if(a[i][j] != 'X') checkX = false;
    }
    if(checkX) status = 0;
    else if(checkO) status = 1;

    if(status != -1) break;

    checkO = true;
    checkX = true;

    for(int j = 0; j < 4; ++j) {
      if(a[j][i] == 'T') continue;
      if(a[j][i] != 'O') checkO = false;
      if(a[j][i] != 'X') checkX = false;
    }
    if(checkX) status = 0;
    else if(checkO) status = 1;

    if(status != -1) break;

    checkO = true;
    checkX = true;

    for(int j = 0; j < 4; ++j) {
      if(a[j][j] == 'T') continue;
      if(a[j][j] != 'O') checkO = false;
      if(a[j][j] != 'X') checkX = false;
    }
    if(checkX) status = 0;
    else if(checkO) status = 1;

    if(status != -1) break;

    checkO = true;
    checkX = true;

    for(int j = 0; j < 4; ++j) {
      if(a[j][3-j] == 'T') continue;
      if(a[j][3-j] != 'O') checkO = false;
      if(a[j][3-j] != 'X') checkX = false;
    }
    if(checkX) status = 0;
    else if(checkO) status = 1;

    if(status != -1) break;
  }

  if(status == 0) cout << "X won" << endl;
  else if(status == 1) cout << "O won" << endl;
  else {
    for(int i = 0; i < 4; ++i) {
      for(int j = 0; j  < 4; ++j) {
        if(a[i][j] == '.') {
          cout << "Game has not completed" << endl;
          return;
        }
      }
    }
    cout << "Draw" << endl;
  }
}

int main(int argc, char *argv[])
{
  int t;
  cin >> t;
  string ee;
  getline(cin,ee);

  for(int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    solve();
  }

  return 0;
}

