#include "stdio.h"
#include "string.h"
using namespace std;
char A[4][4];
bool checkRow(int i, char c) {
  int count = 0;
  bool isT = false;
  for(int k=0; k<4; k++) {
    if (A[i][k] == 'T') isT= true;
    if(A[i][k] == c) count++;
  }
  if (count == 4 || (isT && count==3)) return true;
  return false;
}

bool checkCol(int i, char c) {
  int count = 0;
  bool isT = false;
  for(int k=0; k<4; k++) {
    if (A[k][i] == 'T') isT= true;
    if(A[k][i] == c) count++;
  }
  if (count == 4 || (isT && count==3)) return true;
  return false;
}

bool checkD1(char c) {
  int count = 0;
  bool isT = false;
  for(int k=0; k<4; k++) {
    if (A[k][k] == 'T') isT= true;
    if(A[k][k] == c) count++;
  }
  if (count == 4 || (isT && count==3)) return true;
  return false;
}

bool checkD2(char c) {
  int count = 0;
  bool isT = false;
  for(int k=0; k<4; k++) {
    if (A[k][3-k] == 'T') isT= true;
    if(A[k][3-k] == c) count++;
  }
  if (count == 4 || (isT && count==3)) return true;
  return false;
}


int main() {
  int t;
  scanf("%d", &t);
  for(int x=1; x<=t; x++) {
    for(int i=0; i<4; i++) {
      char s[4];
      scanf("%s", s);
      strcpy(A[i], s);
    }
    //for (int i=0; i<4; i++) { for(int j=0; j<4;j++) {printf("%c", A[i][j]);} printf("\n");}
    bool xwon=false, owon=false, iscomplete=true;
    if(checkD1('X') || checkD2('X')) xwon = true;
    if(checkD1('O') || checkD2('O')) owon = true;
    for (int y=0; y<4; y++) {
      if(checkRow(y, 'X') || checkCol(y, 'X')) xwon = true;
      if(checkRow(y, 'O') || checkCol(y, 'O')) owon = true;
    }
    for (int y=0; y<4; y++) {
      for(int z=0; z<4; z++) {
	if(A[y][z]=='.') iscomplete = false;
      }
    }
    
    if(xwon) { printf("Case #%d: X won\n", x); continue;}
    else if(owon) { printf("Case #%d: O won\n", x); continue;}
    else if(iscomplete) { printf("Case #%d: Draw\n", x); continue;}
    else printf("Case #%d: Game has not completed\n", x);
  }
}