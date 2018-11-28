#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int T;
string b[4];

int check(char c) {
  int a,d;
  a=d=0;
  for(int i=0; i<4; ++i) {
    int nr=0,nr2=0;
    for(int j=0; j<4; ++j) {
      nr+=(b[i][j]==c || b[i][j]=='T');
      nr2+=(b[j][i]==c || b[j][i]=='T');
    }
    if(nr==4 || nr2==4) return 1;
    a+=(b[i][i]==c || b[i][i]=='T');
    d+=(b[i][4-i-1]==c || b[i][4-i-1]=='T');
  }
  if(a==4 || d==4) return 1;
}

int main()
{
    ifstream f("input.txt");
    ofstream g("output.txt");
    f>>T;
    for(int t=1; t<=T; ++t) {
      g<<"Case #"<<t<<": ";
      int ok=1;
      for(int i=0; i<4; ++i) {
        f>>b[i];
        if(b[i].find(".")!=string::npos) ok=0;
      }
      if(check('X')) g<<"X won";
      else if(check('O')) g<<"O won";
      else if(ok) g<<"Draw";
      else g<<"Game has not completed";
      g<<"\n";
    }
    return 0;
}
