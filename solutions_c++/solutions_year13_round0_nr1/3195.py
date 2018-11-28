//GCJ
/*
ID: Geek7
LANG: C++
TASK:
STATE:
MEMO:
*/
#include<iostream>
#include<cmath>
#include<map>
#include<cstring>
#include<cstdio>
#include<cstdarg>
#include<cstdio>
#include<cassert>
#include<vector>
#include<string>
#include<algorithm>
#include<list>
#include<set>
#include<queue>
#include<stack>
#include<sstream>
#include<numeric>
#include<functional>
#include<utility>
#include<bitset>
#define LL long long
#define maxab(a,b) (a)>(b)?(a):(b)
#define LL long long
using namespace std;
char maze[4][5];
int main(){
  int T,i,j,cases=1;
  char win;
  freopen("input.in","r",stdin);
  freopen("output.out","w",stdout);
  scanf("%d",&T);
  while(T--){
    win=0;
    for(i=0;i<4;++i) scanf("%s",maze[i]);
    //..............................................
    for(i=0;i<4;++i){
      for(j=0;j<4;++j){
        if(maze[i][j]!='X' && maze[i][j]!='T') break;
      }
      if(j==4){
        win=1;//x win
        break;
      }
    }
    if(win==1){
      printf("Case #%d: X won\n",cases++);
      continue;
    }
    //..............................................
    for(i=0;i<4;++i){
      for(j=0;j<4;++j){
        if(maze[j][i]!='X' && maze[j][i]!='T') break;
      }
      if(j==4){
        win=1;//x win
        break;
      }
    }
    if(win==1){
      printf("Case #%d: X won\n",cases++);
      continue;
    }
    //.................................................
    for(i=0;i<4;++i) if(maze[i][i]!='X' && maze[i][i]!='T') break;
    if(i==4) win=1;
    if(win==1){
      printf("Case #%d: X won\n",cases++);
      continue;
    }
    //.................................................
    for(i=0;i<4;++i) if(maze[i][3-i]!='X' && maze[i][3-i]!='T') break;
    if(i==4) win=1;
    if(win==1){
      printf("Case #%d: X won\n",cases++);
      continue;
    }

    //........................................................
    for(i=0;i<4;++i){
      for(j=0;j<4;++j){
        if(maze[i][j]!='O' && maze[i][j]!='T') break;
      }
      if(j==4){
        win=2;//x win
        break;
      }
    }
    if(win==2){
      printf("Case #%d: O won\n",cases++);
      continue;
    }
    //..............................................
    for(i=0;i<4;++i){
      for(j=0;j<4;++j){
        if(maze[j][i]!='O' && maze[j][i]!='T') break;
      }
      if(j==4){
        win=2;//x win
        break;
      }
    }
    if(win==2){
      printf("Case #%d: O won\n",cases++);
      continue;
    }
    //.................................................
    for(i=0;i<4;++i) if(maze[i][i]!='O' && maze[i][i]!='T') break;
    if(i==4) win=2;
    if(win==2){
      printf("Case #%d: O won\n",cases++);
      continue;
    }
    //.....................................................
    for(i=0;i<4;++i) if(maze[i][3-i]!='O' && maze[i][3-i]!='T') break;
    if(i==4) win=2;
    if(win==2){
      printf("Case #%d: O won\n",cases++);
      continue;
    }
    //.....................................................
    bool flag=0;
    for(i=0;i<4;++i){
     for(j=0;j<4;++j)
       if(maze[i][j]=='.'){
         flag=1;
         break;
       }
     if(flag) break;
    }
    if(flag) printf("Case #%d: Game has not completed\n",cases++);
    else printf("Case #%d: Draw\n",cases++);
  }
  return 0;
}
