#include <fstream>
#include <string>
#include <iostream>
#include <cassert>
using namespace std;

string board[4];

ifstream in;
ofstream out;

void write() {
  int i,j;
  for (int i=0;i<4;++i) {
    cout<<"> ";
    for (int j=0;j<4;++j)
      cout<<board[i][j];
    cout<<endl;
  }
}

bool win(char c) {
  int i,j;
  for (i=0;i<4;++i) {
    for (j=0;j<4;++j) {
      if (!(board[i][j]==c || board[i][j]=='T'))
	break;
    }
    if (j==4) return true;
  }
  for (i=0;i<4;++i) {
    for (j=0;j<4;++j) {
      if (!(board[j][i]==c || board[j][i]=='T'))
	break;
    }
    if (j==4) return true;
  }
  for (i=0;i<4;i++)
    if (!(board[i][i]==c || board[i][i]=='T')) break;
  if (i==4) return true;
  for (i=0;i<4;i++)
    if (!(board[i][3-i]==c || board[i][3-i]=='T')) break;
  if (i==4) return true;
  return false;
}

bool draw() {
  int i,j;
  for (i=0;i<4;++i)
    for (j=0;j<4;++j)
      if (board[i][j]=='.') return false;
  return true;
}

void solve() {
  int i;
  for (i=0;i<2;++i) {
    char c = "OX"[i];
    if (win(c)) {
      out<<c<<" won"<<endl;
      return;
    }
  }
  if (draw()) {
    out<<"Draw"<<endl;
    return;
  }
  if (i==2)
    out<<"Game has not completed"<<endl;
}

int main(int argc, char *argv[]) {
  assert(argc==3 || argc==4);
  string name=string(argv[1])+"-"+argv[2];
  if (argc==4)
    name += string("-")+argv[3];
  in.open((name+".in").c_str());
  assert(in);
  out.open((name+".out").c_str());
  assert(out);

  int T;
  in >> T;
  for (int t=1;t<=T;++t) {
    cout<<t<<endl;
    getline(in,board[0]);
    for (int i=0;i<4;++i)
      getline(in,board[i]);
    write();
    out<<"Case #"<<t<<": ";
    solve();
  }
  return 0;
}
