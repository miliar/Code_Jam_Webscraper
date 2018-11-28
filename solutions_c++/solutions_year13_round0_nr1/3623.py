#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<string>
#include<iostream>
#include<stack>
#include<queue>
#include<map>
#include<set>
using namespace std;
int T;
char fie[5][5];
char solve(int x,int y,int dx,int dy){
  char c='T';
  bool f=true;
  //  printf("%d %d %d %d\n",x,y,dx,dy);
  for(;x<4 && y<4;x+=dx,y+=dy){
    if(c=='T') c=fie[x][y];
    else if(c==fie[x][y]) c=fie[x][y];
    else if(fie[x][y]=='T') {}
    else { f=false; break; }
  }
  //  printf("%c %d\n",c,f);
  if(f) return c;
  else return '.';
}
bool check(){
  bool f=true;
  for(int x=0;x<4;x++)
    for(int y=0;y<4;y++)
      if(fie[x][y]=='.'){ f=false; break; }
  return f;
}
int main(){
  cin >> T;
  for(int loop=0;loop<T;loop++){
    for(int y=0;y<4;y++)
      for(int x=0;x<4;x++)
	cin >> fie[x][y];

    int won[2]={};
    for(int x=0;x<4;x++){
      char ret = solve(x,0,0,1);
      if(ret == 'X') won[1]=1;
      else if(ret == 'O') won[0]=1;
    }
    for(int y=0;y<4;y++){
      char ret = solve(0,y,1,0);
      if(ret == 'X') won[1]=1;
      else if(ret == 'O') won[0]=1;
    }
    char ret = solve(0,0,1,1);
    if(ret == 'X') won[1]=1;
    else if(ret == 'O') won[0]=1;
    ret = solve(3,0,-1,1);
    if(ret == 'X') won[1]=1;
    else if(ret == 'O') won[0]=1;

    if(won[0] && won[1])
      printf("Case #%d: Draw\n",loop+1);
    else if(won[0])
      printf("Case #%d: O won\n",loop+1);
    else if(won[1])
      printf("Case #%d: X won\n",loop+1);
    else if(check())
      printf("Case #%d: Draw\n",loop+1);
    else
      printf("Case #%d: Game has not completed\n",loop+1);
    
  }
}
