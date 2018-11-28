#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
#include "iostream"
#define DRAW 0
#define INCOMPLETE 1
#define XWIN 2
#define YWIN 3
using namespace std;
typedef long long i64;

int main() {
  int T; scanf("%d", &T);
  vector<string> match(4);
  match[0]="Draw";
  match[1]="Game has not completed";
  match[2]="X won";
  match[3]="O won";
  for (int Ti = 1; Ti <= T; ++Ti) {
    vector<string> inp;
    for (int i = 0;  i < 4 ; i++)
    {
      string line;
      cin>>line;
      inp.push_back(line);
    }
    bool complete= true;
    int x=-1,y=-1;
    for(int i=0;i<4;i++)
    {
       for(int j=0;j<4;j++)
       {
         if(inp[i][j]=='.')
           complete = false;
         if(inp[i][j]=='T')
         {
           x=i;
           y=j;
         }
       }
    }
    int state=-1;
    for(int i=0;i<4;i++)
    {
      int nx=0,no=0;
      for(int j=0;j<4;j++)
      {
        if(inp[i][j]=='X' || inp[i][j]=='T')nx++;
        if(inp[i][j]=='O' || inp[i][j]=='T')no++;
      }
      if(nx==4)
      {
        state=XWIN;
        goto END;
      }
      else if (no==4)
      {
        state=YWIN;
        goto END;
      }
    }
    for(int i=0;i<4;i++)
    {
      int nx=0,no=0;
      for(int j=0;j<4;j++)
      {
        if(inp[j][i]=='X' || inp[j][i]=='T')nx++;
        if(inp[j][i]=='O' || inp[j][i]=='T')no++;
      }
      if(nx==4)
      {
        state=XWIN;
        goto END;
      }
      else if (no==4)
      {
        state=YWIN;
        goto END;
      }
    }
    {
      int nx=0,no=0;
      for(int i=0;i<4;i++)
      {
        if(inp[i][i]=='X' || inp[i][i]=='T')nx++;
        if(inp[i][i]=='O' || inp[i][i]=='T')no++;
      }if(nx==4)
      {
        state=XWIN;
        goto END;
      }
      else if (no==4)
      {
        state=YWIN;
        goto END;
      }
    }
    {
      int nx=0,no=0;
      for(int i=0;i<4;i++)
      {
        if(inp[i][3-i]=='X' || inp[i][3-i]=='T')nx++;
        if(inp[i][3-i]=='O' || inp[i][3-i]=='T')no++;
      }if(nx==4)
      {
        state=XWIN;
        goto END;
      }
      else if (no==4)
      {
        state=YWIN;
        goto END;
      }
    }
    if(complete)
    {
      state=DRAW;
    }
    else
      state=INCOMPLETE;
END:
    printf("Case #%d: ", Ti);
    cout<<match[state]<<endl;
  }
  
  return 0;
}
