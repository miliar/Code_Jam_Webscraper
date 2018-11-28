#include <iostream>
#include <set>
#include <map>
#include <string>
#include <vector>

using namespace std;

bool ifX(char c) {
  return c=='X' || c=='T';
}

bool ifO(char c) {
  return c=='O' || c=='T';
}

bool Xall(char c1, char c2, char c3, char c4) {
  return ifX(c1)+ifX(c2)+ifX(c3)+ifX(c4)==4;
}

bool Oall(char c1, char c2, char c3, char c4) {
  return ifO(c1)+ifO(c2)+ifO(c3)+ifO(c4)==4;
}

string b[4];

int won() {
  int full=true;
  for(int i=0; i<4; i++)
    for(int j=0; j<4; j++)
      if(b[i][j]=='.')
        full=false;
  
  //diag
  if(Xall(b[0][0], b[1][1], b[2][2], b[3][3]) ||
     Xall(b[0][3], b[1][2], b[2][1], b[3][0]))
    return 0;
  if(Oall(b[0][0], b[1][1], b[2][2], b[3][3]) ||
     Oall(b[0][3], b[1][2], b[2][1], b[3][0]))
    return 1;

  //row-col
  for(int i=0; i<4; i++) {
    if(Xall(b[i][0], b[i][1], b[i][2], b[i][3]) ||
       Xall(b[0][i], b[1][i], b[2][i], b[3][i]))
      return 0;
    if(Oall(b[i][0], b[i][1], b[i][2], b[i][3]) ||
       Oall(b[0][i], b[1][i], b[2][i], b[3][i]))
      return 1;
  }

  if(full) {
    return 2;
  } else {
    return 3;
  }
}


int main() {
  int tc;
  cin>>tc;
  for(int t=1; t<=tc; t++) {
    cout<< "Case #"<<t<<": ";
    for(int i=0; i<4; i++) {
      cin >> b[i];
    }
    switch (won()){
    case 0: cout<<"X won"<<endl; break;
    case 1: cout<<"O won"<<endl; break;
    case 2: cout<<"Draw"<<endl; break;
    case 3: cout<<"Game has not completed"<<endl; break;
    }
  }


  return 0;
}
