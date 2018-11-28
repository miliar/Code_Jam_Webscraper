#include <cstdio>
#include <iostream>
using namespace std;
char w[4][5];
bool notcomplete;

void check(int j, int k, int &x, int &y){
  if(w[j][k] == '.'){notcomplete = true;}
  else if(w[j][k] == 'X') x++;
  else if(w[j][k] == 'O') y++;
  else {x++; y++;}
}

int main(int argc, char const *argv[])
{
  int count = 0;
  scanf("%d", &count);

  for (int counter = 1; counter <= count; ++counter)
  {
    cout<<"Case #"<<counter<<": ";
    notcomplete = false;
    for (int j = 0; j < 4; ++j)
    {
      scanf("%s", w[j]);
    }
    //Row
    int x = 0, y = 0, done =false;
    int xc = 0, yc = 0;
    for (int j = 0; j < 4; ++j)
    {
      x=y=xc=yc=0;
      for(int k = 0; k< 4; k++) {
        check(j,k,x,y);
        check(k,j,xc,yc);
      }
      if( x == 4 || xc == 4) {cout<<"X won\n"; done=true; break;}
      else if( y==4 || yc == 4) {cout<<"O won\n"; done=true; break;}
    }
    if(done) continue;

    x=y=xc=yc=0;
    for(int k = 0; k< 4; k++) {
        check(k,k,x,y);
        check(k,3-k,xc,yc);
    }
    if( x == 4 || xc == 4) {cout<<"X won\n"; done=true;}
    else if( y==4 || yc == 4) {cout<<"O won\n"; done=true;}
    if(done) continue;
    if(notcomplete) {cout<<"Game has not completed\n";}
    else cout<<"Draw\n";
  }
  return 0;
}