#include <string>
#include <cstring>
#include <vector>
#include <cmath> 
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
 
using namespace std;
 
#define REP(a,n) for(int a=0; a<(n); ++a)
#define FOR(a,b,c) for(int a=(b); a<=(c); ++a)
#define INIT(a, v) __typeof(v) a = (v)
#define FOREACH(a, v) for (INIT(a, (v).begin()); a!=(v).end(); ++a)
 
template<class T>
inline int size(const T&t){return t.size();}
 
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef long long LL;

#define INF 1000000000
#define PB push_back
#define MP make_pair
 
//////////////////////////////////////////

#define MOD 1000003

char tab[5][5];
int xs, ys;
bool zaj[5][5];

int ile ;

void probuj(int y, int x) {
  if (x==xs) { x =  0; ++y; }
  if (y==ys) { ile = (ile+1)%MOD; return;}
  int xm = 0,ym = 0;
  if (tab[y][x]=='-') { xm = 1;}
  if (tab[y][x]=='|') { ym = 1;}
  if (tab[y][x]=='\\') { xm = ym = 1;}
  if (tab[y][x]=='/') { xm = 1; ym = -1; }
  int nx = (x+xm+xs)%xs;
  int ny = (y+ym+ys)%ys;
  if (!zaj[ny][nx]) {
    zaj[ny][nx] = 1;
    probuj(y, x+1);
    zaj[ny][nx] = 0;
  }
  nx = (x-xm+xs)%xs;
  ny = (y-ym+ys)%ys;
  if (!zaj[ny][nx]) {
    zaj[ny][nx] = 1;
    probuj(y, x+1);
    zaj[ny][nx] = 0;
  }
}

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        scanf("%d%d", &ys, &xs);
        REP(a, ys) {
          scanf("%s", tab[a]);
          REP(b, xs)
            zaj[a][b] = 0;
        }
        ile = 0;
        probuj(0,0);
        printf("Case #%d: %d\n", (tt+1), ile);
    }
}


