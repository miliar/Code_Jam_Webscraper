#include <stdio.h>
#include <fstream>
#include <iostream>

using namespace std;

int main(){

char a[4] = {'.'};
int b[4][4]={0};
int H0=0, H1=0, H2=0, H3=0, V0=0, V1=0, V2=0, V3=0, DL=0, DR=0, sum=0;

ifstream myFile;
myFile.open("input.txt");
int T=0;
myFile >> T;
int count=0;
int i=0;

while(count != T){

  H0=H1=H2=H3=V0=V1=V2=V3=DL=DR=sum=0;

  myFile >> a;
  for(i=0;i<4;i++) if (a[i] == 'X')       b[0][i] = 1000;
                   else if (a[i] == 'O')  b[0][i] = 1;
                   else if (a[i] == 'T')  b[0][i] = 0;
                   else                   b[0][i] = -1;

  myFile >> a;
  for(i=0;i<4;i++) if (a[i] == 'X')       b[1][i] = 1000;
                   else if (a[i] == 'O')  b[1][i] = 1;
                   else if (a[i] == 'T')  b[1][i] = 0;
                   else                   b[1][i] = -1;

  myFile >> a;
  for(i=0;i<4;i++) if (a[i] == 'X')       b[2][i] = 1000;
                   else if (a[i] == 'O')  b[2][i] = 1;
                   else if (a[i] == 'T')  b[2][i] = 0;
                   else                   b[2][i] = -1;
  myFile >> a;
  for(i=0;i<4;i++) if (a[i] == 'X')       b[3][i] = 1000;
                   else if (a[i] == 'O')  b[3][i] = 1;
                   else if (a[i] == 'T')  b[3][i] = 0;
                   else                   b[3][i] = -1;

  H0=b[0][0] + b[0][1] + b[0][2] + b[0][3];
  H1=b[1][0] + b[1][1] + b[1][2] + b[1][3];
  H2=b[2][0] + b[2][1] + b[2][2] + b[2][3];
  H3=b[3][0] + b[3][1] + b[3][2] + b[3][3];

  V0=b[0][0] + b[1][0] + b[2][0] + b[3][0];
  V1=b[0][1] + b[1][1] + b[2][1] + b[3][1];
  V2=b[0][2] + b[1][2] + b[2][2] + b[3][2];
  V3=b[0][3] + b[1][3] + b[2][3] + b[3][3];

  DL=b[0][0] + b[1][1] + b[2][2] + b[3][3];
  DR=b[0][3] + b[1][2] + b[2][1] + b[3][0];

  sum= H0 + H1 + H2 + H3;

  if ((H0 == 3000) || (H0 == 4000) || (H1 == 3000) || (H1 == 4000) || (H2 == 3000) || (H2 == 4000) || (H3 == 3000) || (H3 == 4000) || (DL == 3000) || (DL == 4000) || (DR == 3000) || (DR == 4000) ||      (V0 == 3000) || (V0 == 4000) || (V1 == 3000) || (V1 == 4000) || (V2 == 3000) || (V2 == 4000) || (V3 == 3000) || (V3 == 4000)){ printf("Case #%d: X won\n", count+1); }
  else if ((H0 == 3) || (H0 == 4) || (H1 == 3) || (H1 == 4) || (H2 == 3) || (H2 == 4) || (H3 == 3) || (H3 == 4) || (DL == 3) || (DL == 4) || (DR == 3) || (DR == 4) ||
           (V0 == 3) || (V0 == 4) || (V1 == 3) || (V1 == 4) || (V2 == 3) || (V2 == 4) || (V3 == 3) || (V3 == 4))                   { printf("Case #%d: O won\n", count+1); }
  else if ((sum == 8008) || (sum == 8007) || (sum == 7008)){ printf("Case #%d: Draw\n", count+1); }
  else { printf("Case #%d: Game has not completed\n", count+1); }

  count++;
}

return 0;
}
