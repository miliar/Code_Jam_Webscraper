#include <stdio.h>
#include <iostream>
#include <vector>
#include <map>
#include <string>
using namespace std;

int m[20][20];
map<int,string> d[20][20];
map<int,string> dd2[20][20];
int main( void )
{
 int T;
 cin>>T;
 for(int X=1;X<=T;++X){
  int W,Q;
  cin>>W>>Q;
  for(int y=0;y<W;++y){
   string str;
   cin>>str;
   for(int x=0;x<W;++x)
    m[y][x]=str[x];
  }
  printf("Case #%d:\n",X);
  while(Q-->0){
   int N;
   cin>>N;
   string ret;
   for(int y=0;y<W;++y){
    for(int x=0;x<W;++x){
     d[y][x].clear();
     if(isdigit(m[y][x])){
      int c=m[y][x]-'0';
      char ss[2]={c+'0',0};
      d[y][x][c]=ss;
     }
    }
   }
   int dx[]={0,0,1,-1};
   int dy[]={-1,1,0,0};
   while(true){
    ret="";
    for(int y=0;y<W;++y){
     for(int x=0;x<W;++x){
      if(d[y][x].count(N)>0){
       string ss=d[y][x][N];
       if(ret==""||ret>ss)ret=ss;
      }
     }
    }
    if(ret!="")break;

    for(int y=0;y<W;++y)
    for(int x=0;x<W;++x)
     dd2[y][x]=d[y][x];

    for(int y=0;y<W;++y){
     for(int x=0;x<W;++x){
      for(map<int,string>::const_iterator it=d[y][x].begin();it!=d[y][x].end();++it){
       for(int di=0;di<4;++di){
        int xx=x+dx[di];
        int yy=y+dy[di];
        if(0<=xx&&xx<W&&0<=yy&&yy<W){
        for(int di2=0;di2<4;++di2){
         int xxx=xx+dx[di2];
         int yyy=yy+dy[di2];
         if(0<=xxx&&xxx<W&&0<=yyy&&yyy<W){
         int d2=it->first;
         if(m[yy][xx]=='+')d2+=m[yyy][xxx]-'0';else d2-=m[yyy][xxx]-'0';
         string s2=it->second+(char)m[yy][xx]+(char)m[yyy][xxx];
         if(dd2[yyy][xxx].count(d2)==0||(dd2[yyy][xxx][d2].size()==s2.size()&&dd2[yyy][xxx][d2]>s2))
          dd2[yyy][xxx][d2]=s2;
        }}}
       }
      }
     }
    }

    for(int y=0;y<W;++y)
    for(int x=0;x<W;++x)
     d[y][x]=dd2[y][x];

   } // while
   printf("%s\n",ret.c_str());
  } // query
 } // case
}

