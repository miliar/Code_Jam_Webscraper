#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

bool element(char tar, char a){
  return tar == a || a == 'T';
}

bool isAllSame(char tar,char a, char b, char c, char d){
  return element(tar,a) && element(tar,b) && element(tar,c) && element(tar,d);
}

bool rows(char tar,vector<string> & in){
  for(int i=0;i<4;i++){
    if (isAllSame(tar,in[i][0],in[i][1],in[i][2],in[i][3]))return true;
  }
  return false;
}

bool cols(char tar,vector<string> & in){
  for(int i=0;i<4;i++){
    if (isAllSame(tar, in[0][i], in[1][i], in[2][i], in[3][i]))return true;
  }
  return false;
}

bool diag1(char tar,vector<string> & in){
  return isAllSame(tar,in[0][0],in[1][1],in[2][2],in[3][3]);
}

bool diag2(char tar,vector<string>& in){
  return isAllSame(tar,in[0][3],in[1][2],in[2][1],in[3][0]);
}

bool isNoEmpty(vector<string>&in){
  for(int i=0;i<4;i++){
    if (find(in[i].begin(),in[i].end(),'.') != in[i].end())return false; 
  }
  return true;
}

bool isWin(char tar,vector<string> &in){
  return diag1(tar,in) || diag2(tar,in) || rows(tar,in) || cols(tar,in);
}

int main(){
  int te,tc = 1;
  cin>>te;
  while(te--){
    cout <<"Case #" << tc++ << ": ";
    vector<string> in(4);
    for(int i=0;i<4;i++){
      cin>>in[i];
    }
    if (isWin('X',in))     cout << "X won" << endl;
    else if (isWin('O',in))cout << "O won" << endl;
    else if (isNoEmpty(in))cout << "Draw" << endl;
    else                   cout << "Game has not completed" << endl;
    /*
      Case #2: Draw
      Case #3: Game has not completed
      Case #4: O won
      Case #5: O won
      Case #6: O won
    */
    
  }
  return 0;
}
