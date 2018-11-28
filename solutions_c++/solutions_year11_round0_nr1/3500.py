// pre-written code {{{
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <numeric>
#include <iostream>
#include <cassert>
#include <set>
#define FOR(i,n) for(int _n=n,i=0;i<_n;++i)
#define FR(i,a,b) for(int _b=b,i=a;i<_b;++i)
#define CL(x) memset(x,0,sizeof(x))
#define PN printf("\n");
#define MP make_pair
#define PB push_back
#define SZ size()
#define ALL(x) x.begin(),x.end()
#define FORSZ(i,v) FOR(i,v.size())
#define FORIT(it,x) for(__typeof(x.begin()) it=x.begin();it!=x.end();it++)
using namespace std;
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
///////////////////////////////////////////////////////////////////////////////////
// }}}

int n;
int but[105],r[105];
int v[102][102][102];
queue<pair<pair<int,int>,int> > Q;

void pridaj(int x, int y, int done, int vzd){
   if(0<=x && x<100)
      if(0<=y && y<100)
         if(!v[x][y][done]){
            v[x][y][done]=vzd;
            Q.push(MP(MP(x,y),done));
         }
}

void solve(){
   scanf("%d",&n);
   FOR(i,n){
      char s[20];
      scanf("%s",s); if(s[0]=='O') r[i]=0; else r[i]=1;
      scanf("%d",&but[i]);
      but[i]--;
   }
   while(!Q.empty()) Q.pop();
   CL(v);
   Q.push(MP(MP(0,0),0));
   v[0][0][0]=1;
   int ret=0;
   while(!Q.empty()){
      int x=Q.front().first.first;
      int y=Q.front().first.second;
      int done=Q.front().second;
      Q.pop();
      int vzd=v[x][y][done];
      if(done==n){ ret=vzd; break; }
      FR(dx,-1,+2) FR(dy,-1,+2){
         if(dx==0){
            if(x==but[done] && r[done]==0) pridaj(x+dx,y+dy,done+1,vzd+1);
         } 
         if(dy==0){
            if(y==but[done] && r[done]==1) pridaj(x+dx,y+dy,done+1,vzd+1);
         }
         pridaj(x+dx,y+dy,done,vzd+1);
      }
   }
   printf("%d\n",ret-1);
}

int main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
