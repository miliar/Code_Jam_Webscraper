//#include <iostream>
#include <fstream>
#include <string>
using namespace std;

ifstream cin ("A-large.in");
ofstream cout ("A-large.out");
char A[4][4];

string run() {
  for (int i=0; i<4; i++) {
    for (int j=0; j<4; j++) {
      char c = ' ';
      while (c!='X' && c!='O' && c!='T' && c!='.') cin >> c;
      A[i][j] = c;
    }
  }
  bool x=0, o=0, inc=0;
  
  for (int i=0; i<4; i++) {
    int xx=0, oo=0;
    for (int j=0; j<4; j++) {
      if (A[i][j]=='X') xx++;
      if (A[i][j]=='O') oo++;
      if (A[i][j]=='T') {xx++; oo++;}
      if (A[i][j]=='.') inc=1;
    }
    if (xx==4) x=1;
    if (oo==4) o=1;
    xx=0; oo=0;
    for (int j=0; j<4; j++) {
      if (A[j][i]=='X') xx++;
      if (A[j][i]=='O') oo++;
      if (A[j][i]=='T') {xx++; oo++;}
      if (A[j][i]=='.') inc=1;
    }
    if (xx==4) x=1;
    if (oo==4) o=1;
  }
  int xx=0, oo=0;
  for (int j=0; j<4; j++) {
    if (A[j][j]=='X') xx++;
    if (A[j][j]=='O') oo++;
    if (A[j][j]=='T') {xx++; oo++;}
    if (A[j][j]=='.') inc=1;
  }
  if (xx==4) x=1;
  if (oo==4) o=1;
  xx=0; oo=0;
  for (int j=0; j<4; j++) {
    if (A[j][3-j]=='X') xx++;
    if (A[j][3-j]=='O') oo++;
    if (A[j][3-j]=='T') {xx++; oo++;}
    if (A[j][3-j]=='.') inc=1;
  }
  if (xx==4) x=1;
  if (oo==4) o=1;
  if (x && !o) return "X won";
  if (o && !x) return "O won";
  if (x && o) return "Draw";
  if (inc) return "Game has not completed";
  return "Draw";
}

int main () {
  int T; cin >> T;
  for (int i=1; i<=T; i++) {
    cout << "Case #" << i << ": " << run() << endl;
  }
  return 0;
}
