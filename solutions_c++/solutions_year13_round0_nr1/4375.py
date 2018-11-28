#include <iostream>
#include <algorithm>
using namespace std;

int main(){
  int T;
  cin >> T;
  for(int t=1;t<=T;t++){
    int v[4][4];
    int ans = 0;
    bool isComplete = true;
    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++){
        char c;
        cin >> c;
        if(c == 'X') v[i][j] = 1;
        else if(c == 'O') v[i][j] = 2;
        else if(c == 'T') v[i][j] = 3;
        else {
          v[i][j] = 0;
          isComplete = false;
        }
      }
    }

    for(int i=0;i<4;i++){
      if(v[i][0] == 0) continue;
      int cnt = v[i][0];
      bool f = false;
      for(int j=1;j<4;j++){
        if(cnt == 3) cnt = v[i][j];
        else if(v[i][j] != 3 && v[i][j] != cnt){
          f = true;
          break;
        }
      }
      if(!f){
        if(ans == 0) ans = cnt;
        else if(ans == 1 && cnt == 2 || ans == 2 && cnt == 1) ans = 3;
      }
    }
    
    for(int i=0;i<4;i++){
      if(v[0][i] == 0) continue;
      int cnt = v[0][i];
      bool f = false;
      for(int j=1;j<4;j++){
        if(cnt == 3) cnt = v[j][i];
        else if(v[j][i] != 3 && v[j][i] != cnt){
          f = true;
          break;
        }
      }
      if(!f){
        if(ans == 0) ans = cnt;
        else if(ans == 1 && cnt == 2 || ans == 2 && cnt == 1) ans = 3;
      }
    }
    
    if(v[0][0] != 0){
      int cnt = v[0][0];
      bool f = false;
      for(int i=1;i<4;i++){
        if(cnt == 3) cnt = v[i][i];
        else if(v[i][i] != 3 && v[i][i] != cnt){
          f = true;
          break;
        }
      }
      if(!f){
        if(ans == 0) ans = cnt;
        else if(ans == 1 && cnt == 2 || ans == 2 && cnt == 1) ans = 3;
      }
    }
    
    if(v[0][3] != 0){
      int cnt = v[0][3];
      bool f = false;
      for(int i=1;i<4;i++){
        if(cnt == 3) cnt = v[i][3-i];
        else if(v[i][3-i] != 3 && v[i][3-i] != cnt){
          f = true;
          break;
        }
      }
      if(!f){
        if(ans == 0) ans = cnt;
        else if(ans == 1 && cnt == 2 || ans == 2 && cnt == 1) ans = 3;
      }
    }
    
    cout << "Case #" << t << ": ";
    if(ans == 1) cout << "X won" << endl;
    else if(ans == 2) cout << "O won" << endl;
    else if(ans == 3 || isComplete) cout << "Draw" << endl;
    else cout << "Game has not completed" << endl;

  }
}
