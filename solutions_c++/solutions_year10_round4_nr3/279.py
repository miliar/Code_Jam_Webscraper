#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<utility>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<cctype>
using namespace std;
#define inf 1e100
#define eps 1e-6
template<class T> void chkmax(T&a,T b){if(a<b)a=b;}
template<class T> void chkmin(T&a,T b){if(a>b)a=b;}



int mp[110][110],mp2[110][110];

int n;
bool check(){
  /*
  int i,j;
  for(i=1;i<=6;++i){
    for(j=1;j<=6;++j)printf("%d",mp[j][i]);
    putchar(10);
  }
  putchar(10);
  */
  int x,y;
  for(x=1;x<=100;++x){
    for(y=1;y<=100;++y){
      if(mp[x][y])return true;
    }
  }
  return false;
}
int main(){
  int Cas,ca=0;
  scanf("%d",&Cas);
  while(Cas--){
    int a1,a2,b1,b2,x,y,i;
    scanf("%d",&n);
    memset(mp,0,sizeof(mp));
    for(i=0;i<n;++i){
      scanf("%d%d%d%d",&a1,&b1,&a2,&b2);
      for(x=a1;x<=a2;++x){
        for(y=b1;y<=b2;++y){
          mp[x][y]=1;
        }
      }
    }

    int times=0;
    while(check()){
      for(x=1;x<=100;++x){
        for(y=1;y<=100;++y){
          if(mp[x][y]==1){
            if(x>1 && mp[x-1][y]==1 || y>1 && mp[x][y-1]==1){
              mp2[x][y]=1;
            }else mp2[x][y]=0;
          }else{
            if(x>1 && y>1 && mp[x-1][y]==1 && mp[x][y-1]==1){
              mp2[x][y]=1;
            }else mp2[x][y]=0;
          }
        }
      }
      memcpy(mp,mp2,sizeof(mp2));
      times++;


    }
    printf("Case #%d: %d\n",++ca,times);
  }
  return 0;
}
