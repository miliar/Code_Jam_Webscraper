#include <iostream>

using namespace std;

int main()
{
int t;
cin >> t;
std::string f[4];
for(int i=1; i<=t; i++)
{
  for(int j=0; j<4; j++)cin >> f[j];
  bool owin=false;
  bool xwin=false;
  bool nf=false;
  for(int j=0; j<4; j++)for(int t=0;t<4;t++)if(f[t][j]=='.')nf=true;
  for(int j=0; j<4;j++){
    int no,nx,nt;
    no=nx=nt=0;
    for(int t=0; t<4; t++){
      switch(f[t][j]){
        case 'O':no++;break;
        case 'X':nx++;break;
        case 'T':nt++;break;
      }
    }
    if(no+nt==4)owin=true;
    if(nx+nt==4)xwin=true;
  }
  
  for(int j=0; j<4;j++){
    int no,nx,nt;
    no=nx=nt=0;
    for(int t=0; t<4; t++){
      switch(f[j][t]){
        case 'O':no++;break;
        case 'X':nx++;break;
        case 'T':nt++;break;
      }
    }
    if(no+nt==4)owin=true;
    if(nx+nt==4)xwin=true;
  }
  {
    int no,nx,nt;
    no=nx=nt=0;
    for(int t=0; t<4; t++){
      switch(f[t][t]){
        case 'O':no++;break;
        case 'X':nx++;break;
        case 'T':nt++;break;
      }
    }
    if(no+nt==4)owin=true;
    if(nx+nt==4)xwin=true;
  }
  
  {
    int no,nx,nt;
    no=nx=nt=0;
    for(int t=0; t<4; t++){
      switch(f[3-t][t]){
        case 'O':no++;break;
        case 'X':nx++;break;
        case 'T':nt++;break;
      }
    }
    if(no+nt==4)owin=true;
    if(nx+nt==4)xwin=true;
  }
  cout << "Case #" << i<<": ";
  if(owin)cout << "O won\n";
  else if(xwin)cout << "X won\n";
  else if(nf)cout << "Game has not completed\n";
  else cout << "Draw\n";
}
return 0;
}
