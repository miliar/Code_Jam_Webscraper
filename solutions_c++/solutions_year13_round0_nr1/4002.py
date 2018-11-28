#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  int Q;
  cin >> Q;
  for(int q=0;q<Q;q++) {
    cout << "Case #" << q+1 << ": ";
    int a[4][4];
    int k=0;
    for(int i=0;i<4;i++){
      string s;
      cin >> s;
      for(int j=0;j<4;j++) {
        switch (s[j]) {
          case '.': a[i][j] = 0;
                    k++;
                    break;
          case 'T': a[i][j] = 3;
                    break;
          case 'X': a[i][j] = 1;
                    break;
          case 'O': a[i][j] = 2;
                    break;
        }
      }
    }
    int win = 0;
    for (int i=0;i<4;i++){
      int f = 3;
      for(int j=0;j<4;j++){
        f &= a[i][j];
      }
      win |= f;
    }
    for (int i=0;i<4;i++){
      int f = 3;
      for(int j=0;j<4;j++){
        f &= a[j][i];
      }
      win |= f;
    }
    int f = 3;
    for(int i=0;i<4;i++){
      f &= a[i][i];
    }
    win |= f;
    f = 3;
    for(int i=0;i<4;i++){
      f &= a[3-i][i];
    }
    win |= f;
    if (win == 1){
      cout << "X won\n";
    }else
    if (win == 2){
      cout << "O won\n";
    }else
    if (k!=0) {
      cout << "Game has not completed\n";
    }else{
      cout << "Draw\n";
    }
  }
  return 0;
}