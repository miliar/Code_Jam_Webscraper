#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>

#include<vector>
#include<list>
#include<set>
#include<map>
#include<queue>
#include<string>
#include<algorithm>

#include<iostream>

using namespace std;

vector<string> readMap(int Y, int X)
{
  if(Y<=0)
    return vector<string>(1,"...................................................................");
  else{
    string str;
    cin>>str;
    vector<string> r=readMap(Y-1,X);
    r.push_back("."+str+".");
    return r;
  }
}

bool fill(vector<string>&m,const int y,const int x,const int Y,const int X)
{
  if(x>=X)
    return fill(m,y+1,0,Y,X);
  else if(y>=Y)
    return true;
  else if(m[y][x]=='#'){
    if(m[y+1][x+1]=='#'
     &&m[y+1][x  ]=='#'
     &&m[y  ][x+1]=='#'){
       m[y  ][x  ]='\\';
       m[y  ][x+1]='/';
       m[y+1][x  ]='/';
       m[y+1][x+1]='\\';
       return fill(m,y,x+2,Y,X);
    }
    else
      return false;
  }
  else
    return fill(m,y,x+1,Y,X);
}

void printMap(const vector<string>&m,const int y,const int Y,const int X)
{
  if(y<1)
    return;
  else{
    printf("%s\n",m[y].substr(1,X).c_str());
    printMap(m,y-1,Y,X);
  }
}

int doCase(const int C, const int T)
{
  if(C>T)
    return 0;
  else{
    int X, Y;
    cin>>Y>>X;
    vector<string> m=readMap(Y,X);
    m.push_back("...................................................................");
    printf("Case #%d:\n",C);
    if(fill(m,0,0,Y+2,X+2)){
      printMap(m,Y,Y+1,X);
    }
    else{
      printf("Impossible\n");
    }
    return doCase(C+1,T);
  }
}

int main()
{
 int T;
 cin>>T;
 return doCase(1,T);
}
