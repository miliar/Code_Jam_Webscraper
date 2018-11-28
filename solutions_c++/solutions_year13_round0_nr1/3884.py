#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<utility>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<cmath>

using namespace std;

bool ocheck(string s){
  string op1="OOOO";
  string op2="TOOO";
  string op3="OTOO";
  string op4="OOTO";
  string op5="OOOT";
  return s==op1||s==op2||s==op3||s==op4||s==op5;
}
bool xcheck(string s){
  string xp1="XXXX";
  string xp2="TXXX";
  string xp3="XTXX";
  string xp4="XXTX";
  string xp5="XXXT";
  return s==xp1||s==xp2||s==xp3||s==xp4||s==xp5;
}
int main(){
  int T;
  string s,ans;
  vector<string> board;
  cin>>T;
  for(int c=1;c<=T;printf("Case #%d: %s\n",c++,ans.c_str())){
    board.clear();
    int flag=1;
    for(int i=0;i<4;i++){
      string in;
      cin>>in;
      if(flag&&strstr(in.c_str(),".")!=NULL)flag=0;
      board.push_back(in);
    }
    ans=flag?"Draw":"Game has not completed";
    flag=1;
    for(int i=0;i<4;i++){
      s=board[i];
      if(ocheck(s)){
        ans="O won";
        flag=0;
        break;
      }
      if(xcheck(s)){
        ans="X won";
        flag=0;
        break;
      }
    }
    if(!flag)continue;
    for(int j=0;j<4;j++){
      s="";
      for(int i=0;i<4;i++)s+=board[i][j];
      if(ocheck(s)){
        ans="O won";
        flag=0;
        break;
      }
      if(xcheck(s)){
        ans="X won";
        flag=0;
        break;
      }
    }
    if(!flag)continue;
    s="";
    for(int i=0;i<4;i++)s+=board[i][i];
    if(ocheck(s)){
      ans="O won";
      continue;
    }
    if(xcheck(s)){
      ans="X won";
      continue;
    }
    s="";
    for(int i=0,j=3;i<4&&j>=0;i++,j--)s+=board[i][j];
    if(ocheck(s)){
      ans="O won";
      continue;
    }
    if(xcheck(s)){
      ans="X won";
      continue;
    }
  }
  return 0;
}