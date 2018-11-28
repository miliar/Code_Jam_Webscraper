#include <iostream>

using namespace std;

char data[4][4];

bool judge(char c){
  int cnt;
  for(int i=0;i<4;i++){
    cnt = 0;
    for(int j=0;j<4;j++) if(data[i][j] == c || data[i][j] == 'T') cnt++;
    if(cnt == 4) return true;
  }
  for(int j=0;j<4;j++){
    cnt = 0;
    for(int i=0;i<4;i++) if(data[i][j] == c || data[i][j] == 'T') cnt++;
    if(cnt == 4) return true;
  }
  cnt = 0;
  for(int i=0;i<4;i++) if(data[i][i] == c || data[i][i] == 'T') cnt++;
  if(cnt == 4) return true;
  cnt = 0;
  for(int i=0;i<4;i++) if(data[i][3-i] == c || data[i][3-i] == 'T') cnt++;
  if(cnt == 4) return true;
  return false;
}

bool isFilled(){
  for(int i=0;i<4;i++) for(int j=0;j<4;j++) if(data[i][j] == '.') return false;
  return true;
}

main(){
  int T;
  cin >> T;
  for(int t=1;t<=T;t++){
    for(int i=0;i<4;i++) for(int j=0;j<4;j++) cin >> data[i][j];
    bool x = judge('X');
    bool o = judge('O');
    string ans;
    if(x && o) ans = "Draw";
    else if(x) ans = "X won";
    else if(o) ans = "O won";
    else if(isFilled()) ans = "Draw";
    else ans = "Game has not completed";
    cout << "Case #" << t << ": " << ans << endl;
  }
}
