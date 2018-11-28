#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<limits>

using namespace std;

int nu;

int check(char a[]) {
  int nx = 0, no = 0;
  bool t = false;
  for (int i=0; i < 4; i++) {
    nu++;
    if (a[i] == 'X') nx++;
    else if (a[i] == 'O') no++;
    else if (a[i] == 'T') t = true;
    else nu--;
  }
  if ((nx == 4) || ((nx == 3) && t))
    return 1;
  if ((no == 4) || ((no == 3) && t))
    return 2;
  return 0;
}

int main() {
  int T;
  cin >> T;
  cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n'); 
  string s;
  char c[4][4], b[4], d;
  for (int i = 0; i < T; i++) {
    int r = 0, nut;
    nu = 0; 
    for (int j = 0; j < 4; j++) {
      getline(cin, s);
      c[j][0] = s[0];
      c[j][1] = s[1];
      c[j][2] = s[2];
      c[j][3] = s[3];
      
      b[0] = c[j][0];
      b[1] = c[j][1];
      b[2] = c[j][2];
      b[3] = c[j][3];
      if (!r)
        r = check(b);
    }
    
    getline(cin, s);
    
    nut = nu;
    
    for (int j = 0; (j < 4) && (!r); j++) {
      b[0] = c[0][j];
      b[1] = c[1][j];
      b[2] = c[2][j];
      b[3] = c[3][j];
      r = check(b);
    }
    
    if (!r) {
      b[0] = c[0][0];
      b[1] = c[1][1];
      b[2] = c[2][2];
      b[3] = c[3][3];
      r = check(b);
    }
    
    if (!r) {
      b[0] = c[0][3];
      b[1] = c[1][2];
      b[2] = c[2][1];
      b[3] = c[3][0];
      r = check(b);
    }
    
    if (!r) {
      if (nut < 16) 
        cout << "Case #" << i + 1 << ": Game has not completed" << endl;
      else
        cout << "Case #" << i + 1 << ": Draw" << endl;
    }
    else {
      if (r == 1) 
        cout << "Case #" << i + 1 << ": X won" << endl;
      else
        cout << "Case #" << i + 1 << ": O won" << endl;
    }
  }
  return 0;
}
