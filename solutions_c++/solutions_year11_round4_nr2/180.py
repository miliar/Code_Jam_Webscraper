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

struct tazisko{
   double x,y,h;
   tazisko(){};
   tazisko(double x, double y, double h): x(x),y(y),h(h){};
};

int n,m;
double D;
char vstup[505][505];
double h[505][505];
tazisko t[505][505];
tazisko r[505][505];
tazisko s[505][505];
int ret;

tazisko cell(int x, int y){
   tazisko ret;
   ret.x=(double)x +0.5;
   ret.y=(double)y +0.5;
   ret.h=h[x][y];
   return ret;
}

tazisko operator + (tazisko a, tazisko b){
   double xx=(a.x*a.h + b.x*b.h)/(a.h+b.h);
   double yy=(a.y*a.h + b.y*b.h)/(a.h+b.h);
   return tazisko(xx,yy,a.h+b.h);
}

tazisko operator - (tazisko a, tazisko b){
   b.h*=-1;
   return a+b;
}


void checkni(int i, int j, int v){
   tazisko tt=t[i][j];
   tt=tt-cell(i,j);
   tt=tt-cell(i+v-1,j);
   tt=tt-cell(i,j+v-1);
   tt=tt-cell(i+v-1,j+v-1);   
   if(fabs(tt.x - (i+(double)v/2.0) ) >1e-8) return;
   if(fabs(tt.y - (j+(double)v/2.0) ) >1e-8) return;
//   printf("%d %d %d\n",i,j,v);
   ret=max(ret,v);
}

void solve(){
   scanf("%d %d %lf",&n,&m,&D);
   D=1;
   FOR(i,n) scanf("%s",vstup[i]);
   FOR(i,n) FOR(j,m) h[i][j]=D+(double)(int)(vstup[i][j]-'0');
   FOR(i,n+1) FOR(j,m+1) r[i][j]=s[i][j]=t[i][j]=tazisko(0,0,0);
   ret=0;
   for(int v=1;v<=min(n,m)+1;v++){
      //updatnut riadok
      FOR(i,n-v+1) FOR(j,m-v+1){
         r[i][j]=r[i][j]+cell(i,j+v-1);
         s[i][j]=s[i][j]+cell(i+v-1,j);
         t[i][j]=t[i+1][j+1]+r[i][j]+s[i][j];
         t[i][j]=t[i][j]-cell(i,j);
         //uz len zistit, ci to nahodou netvori ten zazrak..
         if(v>=3) checkni(i,j,v);
      }
   }
   if(ret<3) printf("IMPOSSIBLE\n"); else
   printf("%d\n",ret);
}

int main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
