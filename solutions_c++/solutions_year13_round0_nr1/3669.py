/*
ID: nongeek1
PROG: my
LANG: C++
*/
#include<iostream>
#include<fstream>
using namespace std;

ifstream fin("my.in");
ofstream fout("my.out");

char a[4][4];

bool checkRow(int k, char c){
  for(int i=0; i<4; i++)
    if(a[k][i] != c && a[k][i] != 'T') return false;
  return true;
}
bool checkCol(int k, char c){
  for(int j=0; j<4; j++)
    if(a[j][k] != c && a[j][k] != 'T' ) return false;
  return true;
}
bool checkDiagonal1(char c){
  for(int i=0; i<4; i++)
    if(a[i][i] != c && a[i][i] != 'T') return false;
  return true;
}
bool checkDiagonal2(char c){
  for(int i=0; i<4; i++)
    if(a[i][3-i] != c && a[i][3-i] != 'T') return false;
  return true;
}
bool checkPlayer(char c){
  for(int i=0; i<4; i++)
    if(checkRow(i, c) || checkCol(i, c)) return true;
  if(checkDiagonal1(c)) return true;
  if(checkDiagonal2(c)) return true;
  return false;
}
bool checkOver(){
  for(int i=0; i<4; i++)
    for(int j=0; j<4; j++)
      if(a[i][j]=='.') return false;
  return true;
}
void solve(){
  
  for(int i=0; i<4; i++)
    for(int j=0; j<4; j++)
      fin>>a[i][j];
  if(checkPlayer('X')) fout << "X won" << endl;
  else if(checkPlayer('O')) fout << "O won" << endl;
  else if(checkOver())
    fout << "Draw" << endl;
  else
    fout << "Game has not completed" << endl;
}
int main(){
  int caseN;
  fin >> caseN;
  for(int index=1; index<=caseN; index++){
    fout << "Case #" << index <<": ";    
    solve();
  }
  return 0;
}
