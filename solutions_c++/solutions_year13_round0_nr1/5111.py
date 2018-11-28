//#define FILE_IO

#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>

using namespace std;

typedef long long ll;
#ifdef unix
#define LLD "%lld"
#else
#define LLD "%I64d"
#endif 

char a[4][4];

int check(char a,char b,char c,char d){
  char t[4]={a,b,c,d},i;
  for(i=0;i<4;++i)
    if(t[i]!='T'&&t[i]!='X')
      break;
  if(i==4)return 1;
  for(i=0;i<4;++i)
    if(t[i]!='T'&&t[i]!='O')
      break;
  if(i==4)return 2;
  return 0;
}

int main(){
#ifdef FILE_IO
  freopen("t.in","r",stdin);
  freopen("t.out","w",stdout);
#endif
  int T,Test=0;
  int s,t,i,j;
  char ch;
  scanf("%d",&T);
  while(T--){
    s=0,t=0;
    for(i=0;i<4;++i)
      for(j=0;j<4;++j){
        while(ch=getchar(),ch!='X'&&ch!='.'&&ch!='O'&&ch!='T');
        a[i][j]=ch;
        if(ch!='.')++s;
      }
    for(i=0;i<4;++i)
      t|=check(a[i][0],a[i][1],a[i][2],a[i][3]);
    for(i=0;i<4;++i)
      t|=check(a[0][i],a[1][i],a[2][i],a[3][i]);
    t|=check(a[0][0],a[1][1],a[2][2],a[3][3]);
    t|=check(a[0][3],a[1][2],a[2][1],a[3][0]);
    printf("Case #%d: ",++Test);
    if(t==1)puts("X won");
    else if(t==2)puts("O won");
    else if(s==16)puts("Draw");
    else puts("Game has not completed");
  }
  return 0;
}
