#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<string> vs;
typedef vector<long long> vll;
#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define mset(arr,val)  memset(arr,val,sizeof(arr))
#define tr(c,i)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define forr(var,from,to) for(int var=(from);var<=(to);var++) 
#define found(s,e)  ((s).find(e)!=(s).end())
#define remove_(c,val) (c).erase(remove((c).begin(),(c).end(),(val)),(c).end())
#define lastc(str) (*((str).end()-1))

#ifdef DEBUG
#include "cout.h"
#endif
/*
######
#..X.#
#.#..#
#...##
######
*/
int gcd(int x, int y) {
  while(x) swap(x, y%=x);
  return y;
}
main(){
  int _T; cin>>_T; //1-100
  rep(_t,_T){
    int H,W; cin>>H>>W; // 3-30
    int D; cin>>D; //1-50
    vector<string> M(H);
    rep(h,H) cin>>M[h];

    int mex,mey;
#ifdef DEBUG
    printf("H=%d, W=%d; D=%d;\n", H,W,D);
#endif
    rep(y,H) {
      rep(x,W) if (M[y][x]=='X') { mex=x; mey=y; }
#ifdef DEBUG
      cout << M[y] << endl;
#endif
    }
#ifdef DEBUG
    cout << "me:" << mex << " " << mey << endl;
#endif
    //printf("gcd(15,12)=%d\n", gcd(15,12));

    int w=W-2, h=H-2;
    int xofs = 64 - mex, yofs = 64 - mey;
    vector<vector<int> > xx(128,vector<int>(128,-1)); // [0,127][0,127]
    // x:1..W-1 y:1..H-1
    //int xorig = // mex+xofs->64, 1+xofs->w
    rep(x,w) rep(y,h) {
      xx[xofs+(1+x)][yofs+(1+y)] = 0;
    }
    xx[64][64] = 1; // xx[xofs+mex][yofs+mey]
    // 左展開
    rep(x,w) rep(y,h) {
      xx[xofs-x][yofs+(1+y)] = xx[xofs+(1+x)][yofs+(1+y)];
    }
    // 上展開
    rep(x,w) rep(y,h) {
      xx[xofs+(1+x)][yofs-y] = xx[xofs+(1+x)][yofs+(1+y)];
      xx[xofs-x][yofs-y] = xx[xofs+(1+x)][yofs+(1+y)];
    }

    int xorg=xofs+1-w, yorg=yofs+1-h;
    int xj=(xorg+w*2-1)/(w*2), yj=(yorg+h*2-1)/(h*2);
    int xk=((128-xorg)+w*2-1)/(w*2), yk=((128-yorg)+h*2-1)/(h*2);
#ifdef DEBUG
    printf("x:{%d..%d}, y:{%d..%d}\n", xj,xk, yj,yk);
#endif
    // コピー
    for (int xmg=-xj; xmg<=xk; xmg++) {
      for (int ymg=-yj; ymg<=yk; ymg++) {
        if (xmg==0 && ymg==0) continue;
        rep(x,w*2) rep(y,h*2) {
          int i = xorg+x + w*2*xmg;
          int j = yorg+y + h*2*ymg;
          if (0<=i && i<128 && 0<=j && j<128) {
            xx[i][j] = xx[xorg+x][yorg+y];
          }
        }
      }
    }

    int ans = 0;

    set<pair<int,int> > ps;
    for (int dy=-D-1; dy<=D+1; dy++) {
      for (int dx=-D-1; dx<=D+1; dx++) {
        if (dy==0 && dx==0) {
#ifdef DEBUG
          putchar('X');
#endif
          continue;
        } else {
#ifdef DEBUG
          putchar("?.x"[1+xx[64+dx][64+dy]]);
#endif
          if (dx*dx + dy*dy <= D*D) {
            //if (dx*dx + dy*dy < (D+1)*(D+1)) {
            int g = gcd(abs(dx),abs(dy));
            int x=dx/g, y=dy/g;
            if (!found(ps,make_pair(x,y))) {
              if (xx[64+dx][64+dy]==1) {
                ans++;
                ps.insert(make_pair(x,y));
              }
            }
          }
        }
      }
#ifdef DEBUG
      printf("\n");
#endif
    }

    printf("Case #%d: %d\n", 1+_t, ans);
  }
}
