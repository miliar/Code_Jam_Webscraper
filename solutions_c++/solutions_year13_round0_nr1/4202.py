#include <iostream>
#include <cstdio>
#include <fstream>
#include <cstdlib>
using namespace std;

char win;
int t1,t2;

int check_diag(string table[]) {
  if(t1 != -1)
    table[t1][t2] = 'O';
    
  if(table[0][0]==table[1][1] && table[1][1]==table[2][2] && table[2][2]==table[3][3] && table[0][0]!='.') { win=table[0][0]; return 1; }
  if(table[0][3]==table[1][2] && table[1][2]==table[2][1] && table[2][1]==table[3][0] && table[0][3]!='.') { win=table[0][3]; return 1; }
  
  if(t1 != -1)
    table[t1][t2] = 'X';
    
  if(table[0][0]==table[1][1] && table[1][1]==table[2][2] && table[2][2]==table[3][3] && table[0][0]!='.') { win=table[0][0]; return 1; }
  if(table[0][3]==table[1][2] && table[1][2]==table[2][1] && table[2][1]==table[3][0] && table[0][3]!='.') { win=table[0][3]; return 1; }
  
  return 0;
}

int check_orto(string table[]) {
  if(t1 != -1)
    table[t1][t2] = 'O';
  
  for(int i=0; i<4; i++) {
    if(table[i][0]==table[i][1] && table[i][1]==table[i][2] && table[i][2]==table[i][3] && table[i][0]!='.') { win=table[i][0]; return 1;}
    if(table[0][i]==table[1][i] && table[1][i]==table[2][i] && table[2][i]==table[3][i] && table[0][i]!='.') { win=table[0][i]; return 1;}
  }
  
  if(t1 != -1)
    table[t1][t2] = 'X';
  
  for(int i=0; i<4; i++) {
    if(table[i][0]==table[i][1] && table[i][1]==table[i][2] && table[i][2]==table[i][3] && table[i][0]!='.') { win=table[i][0]; return 1;}
    if(table[0][i]==table[1][i] && table[1][i]==table[2][i] && table[2][i]==table[3][i] && table[0][i]!='.') { win=table[0][i]; return 1;}
  }
  
  return 0;
}
int draw(string table[]) {
  for(int i=0; i<4; i++)
    for(int j=0; j<4; j++)
      if(table[i][j]=='.')
        return 0;
  return 1;
}

void checkT(string table[]) {
  for(int i=0; i<4; i++)
    for(int j=0; j<4; j++)
      if(table[i][j]=='T') {
        t1 = i; 
        t2 = j;
        return;
      }
}

int main() {
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
  int C;
  cin >> C;
  string table[4];
  for(int i=0; i<C; i++) {
    t1 = t2 = -1;
    for(int j=0; j<4; j++)
      cin >> table[j];
    checkT(table);
    cout << "Case #" << i+1 << ": ";
    if(check_diag(table) ) cout << win << " won" << endl;
    else if(check_orto(table) ) cout << win << " won" << endl;
    else if(draw(table) ) cout << "Draw" << endl;
    else cout << "Game has not completed" << endl;
  }
  
  return 0;
}

