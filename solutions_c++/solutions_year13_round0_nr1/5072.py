#include<iostream>
#include<fstream>
using namespace std;

  ifstream f("input.txt");
  ofstream of("output.txt");

  long T[4][4];

  void Init(){

  char c;

  for(long i=0;i<4;++i)
  for(long j=0;j<4;++j)
  {
   f>>c;
   if(c=='T')T[i][j]=100;
   if(c=='.')T[i][j]=0;
   if(c=='O')T[i][j]=11;
   if(c=='X')T[i][j]=2;
  }
  }

  string Det(){

  long a;
  a=T[0][0]+T[0][1]+T[0][2]+T[0][3];if(a==133 || a==44)return "O won";if(a==106 || a==8)return "X won";
  a=T[1][0]+T[1][1]+T[1][2]+T[1][3];if(a==133 || a==44)return "O won";if(a==106 || a==8)return "X won";
  a=T[2][0]+T[2][1]+T[2][2]+T[2][3];if(a==133 || a==44)return "O won";if(a==106 || a==8)return "X won";
  a=T[3][0]+T[3][1]+T[3][2]+T[3][3];if(a==133 || a==44)return "O won";if(a==106 || a==8)return "X won";

  a=T[0][0]+T[1][0]+T[2][0]+T[3][0];if(a==133 || a==44)return "O won";if(a==106 || a==8)return "X won";
  a=T[0][1]+T[1][1]+T[2][1]+T[3][1];if(a==133 || a==44)return "O won";if(a==106 || a==8)return "X won";
  a=T[0][2]+T[1][2]+T[2][2]+T[3][2];if(a==133 || a==44)return "O won";if(a==106 || a==8)return "X won";
  a=T[0][3]+T[1][3]+T[2][3]+T[3][3];if(a==133 || a==44)return "O won";if(a==106 || a==8)return "X won";

  a=T[0][0]+T[1][1]+T[2][2]+T[3][3];if(a==133 || a==44)return "O won";if(a==106 || a==8)return "X won";
  a=T[3][0]+T[2][1]+T[1][2]+T[0][3];if(a==133 || a==44)return "O won";if(a==106 || a==8)return "X won";

 long s=0;

 for(long i=0;i<4;++i)
 for(long j=0;j<4;++j)
 if (T[i][j]==0)s++;

 if(s>0)return "Game has not completed";
 return "Draw";
  }

int main(){

  long T;

  f>>T;

  for(long i=1;i<=T;++i){
  Init();
  of<<"Case #"<<i<<": "<<Det()<<"\n";
  }


return 0;
}
