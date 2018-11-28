#include <iostream>
#include <string>
#include <vector>

using namespace std;

enum Result {
  XWON,
  OWON,
  DRAW,
  NOTCOMPLETE
};

bool hasLine(char who, char a, char b, char c, char d) {
  return
      ((a == who) || (a == 'T')) &&
      ((b == who) || (b == 'T')) &&
      ((c == who) || (c == 'T')) &&
      ((d == who) || (d == 'T'));
}
Result solve() {
  vector<string> lines;
  for(int i=0;i<5;++i) {
    string s;
    getline(cin, s);
    lines.push_back(s);
  }
  bool xwon = false;
  bool owon = false;
  bool hasdot = false;

  // Check for dots
  for(int i=0;i<4;++i) {
    for(int j=0;j<4;++j) {
      if(lines[i][j]=='.') {
        hasdot = true;
      }
    }
  }
  // Check lines
  for(int i=0;i<4;++i) {
    if(hasLine('X', lines[i][0], lines[i][1], lines[i][2], lines[i][3])){
      xwon = true;
    }
    if(hasLine('O', lines[i][0], lines[i][1], lines[i][2], lines[i][3])){
      owon = true;
    }
  }
  // Check rows
  for(int i=0;i<4;++i) {
    if(hasLine('X', lines[0][i], lines[1][i], lines[2][i], lines[3][i])){
      xwon = true;
    }
    if(hasLine('O', lines[0][i], lines[1][i], lines[2][i], lines[3][i])){
      owon = true;
    }
  }
  // Check diagonals
  if(hasLine('X', lines[0][0], lines[1][1], lines[2][2], lines[3][3])){
    xwon = true;
  }
  if(hasLine('O', lines[0][0], lines[1][1], lines[2][2], lines[3][3])){
    owon = true;
  }
  if(hasLine('X', lines[0][3], lines[1][2], lines[2][1], lines[3][0])){
    xwon = true;
  }
  if(hasLine('O', lines[0][3], lines[1][2], lines[2][1], lines[3][0])){
    owon = true;
  }

  if(xwon && owon) {
    cerr<<"!!! Both won"<<endl;
    return DRAW;
  }
  if(xwon && !owon) {
    return XWON;
  } else if(owon && !xwon) {
    return OWON;
  } else if(!xwon && !owon && hasdot) {
    return NOTCOMPLETE;
  } else if(!xwon && !owon && !hasdot) {
    return DRAW;
  }
  return DRAW;
}

int main(int argc, char** argv) {
  int N;
  cin>>N;
  string ignore;
  getline(cin, ignore);
  for(int n=0;n<N;++n) {
    cout<<"Case #"<<n+1<<": ";
    switch(solve()) {
      case OWON:
        cout<<"O won"<<endl;
        break;
      case XWON:
        cout<<"X won"<<endl;
        break;
      case DRAW:
        cout<<"Draw"<<endl;
        break;
      case NOTCOMPLETE:
        cout<<"Game has not completed"<<endl;
        break;
    }
  }
  return 0;
}
