#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <map>
#include <utility>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>

using namespace std;

#define CLEAR(X) memset(X,0,sizeof(X))
#define REP(i,n) for(int i=0;i<(n);i++) 
template <class T> vector<T>parse(string s,const char d=' '){
  vector<T> v; string p; s+=d; int i=0; 
  while(i<(int)s.size())
    if (s[i] == d){stringstream u; u<<p; T t; u>>t; v.push_back(t); p=""; while(i<(int)s.size() && s[i]==d)i++;} else p+=s[i++];   
  return v;
} 

typedef long long ll;
typedef long double ld;

int main(){
  int _cases; scanf("%d",&_cases);
  for(int _case=1;_case<=_cases;_case++){
    printf("Case #%d:",_case);
    int r;scanf("%d",&r);
    int a[111][111];
    CLEAR(a);
    int mx=0,my=0;

    REP(i,r){
      int x1,y1,x2,y2;
      scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
      mx=max(mx,x2);my=max(my,y2);
      for(int x=x1;x<=x2;x++)for(int y=y1;y<=y2;y++)a[y+1][x+1]=1;
    }
    int sel=0;
    REP(i,105)REP(j,105)sel+=a[i][j];
    int res=0;
    int b[111][111];
    mx+=3;my+=3;
    while(sel>0){
      CLEAR(b);
      sel=0;
      for(int i=1;i<=105;i++)for(int j=1;j<=105;j++){
        if(a[i][j]){
          if(!a[i-1][j] && !a[i][j-1])b[i][j]=0;
          else {sel++;b[i][j]=1;}
        }else{
          if(a[i-1][j] && a[i][j-1]){b[i][j]=1;sel++;}
        }
      }
      REP(i,106)REP(j,106)a[i][j]=b[i][j];
      res++;
    }
    printf(" %d\n",res);
  }
  return 0;
}
