#include <iostream>


int tab1[4][4];
int tab2[4][4];
char z;
int T;
bool draw,xwon,owon,empty;

using namespace std;

int main(void) {
  cin >> T;
  draw=false;
  xwon=false;
  owon=false;
  
  for (int i=0;i<T;i++) {
    draw=false;
    xwon=false;
    owon=false;
    empty=false;  
    for (int x=0;x<4;x++) {
      for (int y=0;y<4;y++) {
        cin >> z;
        if (z=='.') {
          empty=true;          
          tab1[x][y]=0;
          tab2[x][y]=0;
        }
        if (z=='X') {
          tab1[x][y]=1;
          tab2[x][y]=1;
        }
        if (z=='O') {
          tab1[x][y]=-1;
          tab2[x][y]=-1;
        }
        if (z=='T') {
          tab1[x][y]=1;
          tab2[x][y]=-1;
        }
      }
    }      
    
    int s;
    for (int x=0;x<4;x++) {
      s = tab1[x][0]+tab1[x][1]+tab1[x][2]+tab1[x][3];
      if (s==4) xwon=true;
      if (s==-4) owon=true;
      s = tab2[x][0]+tab1[x][1]+tab1[x][2]+tab1[x][3];
      if (s==4) xwon=true;
      if (s==-4) owon=true;
      
      s = tab1[0][0]+tab1[1][1]+tab1[2][2]+tab1[3][3];
      if (s==4) xwon=true;
      if (s==-4) owon=true;            
      s = tab2[0][0]+tab1[1][1]+tab1[2][2]+tab1[3][3];
      if (s==4) xwon=true;
      if (s==-4) owon=true;

      s = tab1[3][0]+tab1[2][1]+tab1[1][2]+tab1[0][3];
      if (s==4) xwon=true;
      if (s==-4) owon=true;            
      s = tab2[3][0]+tab1[2][1]+tab1[1][2]+tab1[0][3];
      if (s==4) xwon=true;
      if (s==-4) owon=true;
      
      s = tab2[0][x]+tab1[1][x]+tab1[2][x]+tab1[3][x];
      if (s==4) xwon=true;
      if (s==-4) owon=true;
      s = tab2[0][x]+tab1[1][x]+tab1[2][x]+tab1[3][x];
      if (s==4) xwon=true;
      if (s==-4) owon=true;                         
    }  
      
    if (xwon && owon) cout << "Case #" << (i+1) << ": Draw" << endl;
    else {
      if (!xwon && !owon && empty) {
        cout << "Case #" << (i+1) << ": Game has not completed" << endl;
        continue;
      }  
      if (!xwon && !owon && !empty) {
        cout << "Case #" << (i+1) << ": Draw" << endl;
        continue;
      }  
      if (xwon) {
        cout << "Case #" << (i+1) << ": X won" << endl;
      }
      if (owon) {
        cout << "Case #" << (i+1) << ": O won" << endl;
      }      
    }                    
  }        
}