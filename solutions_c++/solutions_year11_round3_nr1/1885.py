#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

//#define SMALL
#define LARGE

#define STACKSIZE 110

int main()
{
#ifdef SMALL
  ifstream datain("A-small-attempt0.in");
  ofstream dataout("A-small-attempt0.out");
  char gr[10][10];
#endif
#ifdef LARGE
  ifstream datain("A-large.in");
  ofstream dataout("A-large.out");
  char gr[55][55];
#endif
  int t;
  datain>>t;
  for(int ti=1; ti<=t; ti++) {
    int R,C;
    int blgr = 0;
    datain>>R>>C;
    for (int i=0; i<R; i++)
      for (int j=0; j<C; j++){
        datain>>gr[i][j];
        if(gr[i][j]=='#')
          blgr++;
      }
    dataout<<"Case #"<<ti<<":"<<endl;
    if(blgr==0){
      for(int i=0; i<R; i++)
      {
        for(int j=0; j<C; j++)
          dataout<<gr[i][j];
        dataout<<endl;
      }
      continue;
    }
    if(blgr%4 != 0){
      dataout<<"Impossible"<<endl;
      continue;
    }
    bool imp=true;
    while(true){
      for (int i=0; i<R; i++){
        for (int j=0; j<C; j++){
          if(gr[i][j] == '#'){
            int bgrcnt = 0;
            if(i-1>=0 && gr[i-1][j]=='#')
              bgrcnt++;
            if(i+1<R && gr[i+1][j]=='#')
              bgrcnt++;
            if(j-1>=0 && gr[i][j-1]=='#')
              bgrcnt++;
            if(j+1<C && gr[i][j+1]=='#')
              bgrcnt++;
            if(bgrcnt<=1){
              imp=false;
              break;
            }
            if(bgrcnt==2){
              int a=0,b=0;
              if(i-1>=0 && gr[i-1][j]=='#')
                a++;
              if(i+1<R && gr[i+1][j]=='#')
                a--;
              if(j-1>=0 && gr[i][j-1]=='#')
                b--;
              if(j+1<C && gr[i][j+1]=='#')
                b++;
              if(a==0||b==0)
              {
                imp=false;
                break;
              }
              if(a==1&&b==1){
                gr[i][j]='\\';
                gr[i][j+1]='/';
                gr[i-1][j]='/';
                gr[i-1][j+1]='\\';
              } else if(a==1&&b==-1){
                gr[i][j]='/';
                gr[i-1][j]='\\';
                gr[i][j-1]='\\';
                gr[i-1][j-1]='/';
              } else if(a==-1&&b==1){
                gr[i][j]='/';
                gr[i+1][j]='\\';
                gr[i][j+1]='\\';
                gr[i+1][j+1]='/';
              } else if(a==-1&&b==-1){
                gr[i][j]='\\';
                gr[i+1][j]='/';
                gr[i][j-1]='/';
                gr[i+1][j-1]='\\';
              }
            }
          }
        }
        if(!imp)
          break;
      }
      if(!imp)
        break;
      int cnt=0;
      for (int i=0; i<R; i++)
        for (int j=0; j<C; j++)
          if(gr[i][j]=='#')
            cnt++;
      if(cnt==0){
        break;
      }
      if(cnt%4!=0)
      {
        imp=false;
        break;
      }
    }
    if(!imp)
    {
      dataout<<"Impossible"<<endl;
      continue;
    }
    for(int i=0; i<R; i++)
    {
      for(int j=0; j<C; j++)
        dataout<<gr[i][j];
      dataout<<endl;
    }
  }
  return 0;
}