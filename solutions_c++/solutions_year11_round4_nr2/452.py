#include<stdio.h>
#include<string>
#include<stdlib.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define CLR(s) memset(s,0,sizeof(s))
#define EPS 1e-10
typedef long long LL;

LL a[600][600];

struct P{
  LL x,y;
  P(){}
  P(LL x,LL y):x(x),y(y){}

  P operator + (const P &a)const{ return P(x+a.x,y+a.y); }
  P operator - (const P &a)const{ return P(x-a.x,y-a.y); }
  P operator * (const LL &a)const{ return P(x*a,y*a); }
} b[600][600], c[600][600];

LL ps[600][600];

inline LL sum(int x1,int y1,int x2,int y2){
  LL ans = ps[x2][y2]-(x1?ps[x1-1][y2]:0)-(y1?ps[x2][y1-1]:0)+((x1&&y1)?ps[x1-1][y1-1]:0);
  ans -= a[x1][y1]; ans -= a[x1][y2]; ans -= a[x2][y1]; ans -= a[x2][y2];
  return ans;
}
inline P bsum(int x1,int y1,int x2,int y2){
  P ans = c[x2][y2]-(x1?c[x1-1][y2]:P(0,0))-(y1?c[x2][y1-1]:P(0,0))+((x1&&y1)?c[x1-1][y1-1]:P(0,0));
  ans = ans - b[x1][y1]; ans = ans - b[x1][y2]; ans = ans - b[x2][y1]; ans = ans -b[x2][y2];
  return ans;
}


int n,m;
LL D;

int main(){
  int tc; scanf("%d",&tc);
  FOE(ca,1,tc){
    scanf("%d%d%lld",&n,&m,&D);
    FOR(i,0,n){
      char s[1000]; scanf("%s",s);
      FOR(j,0,m) a[i][j] = D+(s[j]-'0');
    }
    FOR(i,0,n){
      FOR(j,0,m) ps[i][j] = a[i][j] + ((i>0)?ps[i-1][j]:0) + ((j>0)?ps[i][j-1]:0) - ((i>0 && j>0)?ps[i-1][j-1]:0);
    }
    /*
    FOR(i,0,n){
      FOR(j,0,m) printf("%lld ",a[i][j]); puts("");
    }
    FOR(i,0,n){
      FOR(j,0,m) printf("%lld ",ps[i][j]); puts("");
    }
    */

    FOR(i,0,n){
      FOR(j,0,m){
        b[i][j] = P(i*2,j*2)*a[i][j];
      }
    }
    FOR(i,0,n){
      FOR(j,0,m){
        c[i][j] = b[i][j];
        if (i) c[i][j] = c[i][j] + c[i-1][j];
        if (j) c[i][j] = c[i][j] + c[i][j-1];
        if (i&&j) c[i][j] = c[i][j] + (c[i-1][j-1]*(-1));
      }
    }
    int ans = 0;

    FOR(i,0,n){
      FOR(j,0,m){
        int lim = min(n,m);
        FOR(k,max(2,ans),lim){
          if (i+k>=n || j+k>=m) break;
//          printf("!! %d %d: %d\n",i,j,k);

          LL ms = sum(i,j,i+k,j+k);
          P cc = P(i*2+k, j*2+k) * ms;
//          printf("    == ms:%lld (%lld,%lld)\n",ms,cc.x,cc.y);

          P mp = bsum(i,j,i+k,j+k);
 //         printf("   == mp: (%lld,%lld)\n",mp.x,mp.y);
          if (cc.x==mp.x && cc.y==mp.y){
            ans = k+1;
          }
        }
      }
    }
    printf("Case #%d: ",ca);
    if (ans<3) printf("IMPOSSIBLE\n");
    else printf("%d\n",ans);
  }
  return 0;
}
