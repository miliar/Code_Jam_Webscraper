#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
 
using namespace std;
 
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
typedef long long ll;
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define mp make_pair
#define go(i,n) for(int i=0;i<n;i++)
#define go3(i,j,n) for(int i=j;i<n;i++)

#define owin 1
#define xwin 2
#define draw 3
#define ncom 4 

int win(vector<string> g){

 int tc,oc,xc;

 
 for(int i=0;i<4;i++){
  tc=0;
  oc=0;
  xc=0;

  for(int j=0;j<4;j++){
   tc+=g[i][j]=='T';
   oc+=g[i][j]=='O';
   xc+=g[i][j]=='X';

   if(tc+oc==4) return owin;
   if(tc+xc==4) return xwin;
  }
 }

 for(int i=0;i<4;i++){
   tc=0;
   oc=0;
   xc=0;

   for(int j=0;j<4;j++){
    tc+=g[j][i]=='T';
    oc+=g[j][i]=='O';
    xc+=g[j][i]=='X';
   }

   if(tc+oc==4) return owin;
   if(tc+xc==4) return xwin;

  }

  tc=oc=xc=0;
  for(int i=0;i<4;i++){
    tc+=g[i][i]=='T';
    oc+=g[i][i]=='O';
    xc+=g[i][i]=='X';
    
  }
  if(tc+oc==4) return owin;
  if(tc+xc==4) return xwin;

  tc=oc=xc=0;
  for(int i=0;i<4;i++){
    tc+=g[i][3-i]=='T';
    oc+=g[i][3-i]=='O';
    xc+=g[i][3-i]=='X';
  }
  if(tc+oc==4) return owin;
  if(tc+xc==4) return xwin;

  for(int i=0;i<4;i++) for(int j=0;j<4;j++) if(g[i][j]=='.') return ncom;

  return draw;

}

void oku(){

 int T;
 scanf("%d",&T);
 vector<string> g;
 string s;

 go(cs,T){
  g.clear();
  go(i,4) {
   cin>>s;
   g.pb(s);
  }

  int w=win(g);
  printf("Case #%d: ",cs+1);
  if(w==1) puts("O won"); else
  if(w==2) puts("X won"); else
  if(w==3) puts("Draw"); else
  if(w==4) puts("Game has not completed");

 }


}


int main(){
#ifndef ONLINE_JUDGE
freopen("in","r",stdin);
#endif



oku();

return 0;}