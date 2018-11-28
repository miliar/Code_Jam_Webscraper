using namespace std;
 
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
 
#define PB push_back
#define SZ size()
#define REP(v, hi) for (int v=0; v<(hi); v++)
#define REPD(v, hi) for (int v=((hi)-1); v>=0; v--)
#define FOR(v, lo, hi) for (int v=(lo); v<(hi); v++)
#define FORD(v, lo, hi) for (int v=((hi)-1); v>=(lo); v--)
#define FORALL(it,x) for (typeof(x.begin()) it=x.begin(); it!=x.end(); it++)

typedef vector <int> VI;
typedef vector <VI> VVI;
typedef long long LL;
typedef vector<LL> VLL;
typedef vector<VLL> VVLL;
typedef vector<double> VD;
typedef vector<VD> VVD;
typedef vector <string> VS;

const int dy[4] = {-1,0,1,0};
const int dx[4] = {0,1,0,-1};

char m[12200][12200];

void solve () {

  int L;
  scanf ("%i",&L);
  string s;
  
  REP(i,L) {
    char t[100];
    int n;
    scanf ("%s %i",t,&n);
    REP(j,n) s+=t;
  }

  memset(m,0,sizeof(m));
  
  int x=6100, y=6100;
  int minx=x,maxx=x,miny=y,maxy=y;
  int d=0;
  REP(i,s.SZ) {
    m[y][x]=1;
    if (s[i]=='F') {
      x+=dx[d], y+=dy[d];
      m[y][x]=1;
      x+=dx[d], y+=dy[d];
    }      
    if (s[i]=='L') d=(d+1)%4;
    if (s[i]=='R') d=(d+3)%4;
    minx<?=x;
    maxx>?=x;
    miny<?=y;
    maxy>?=y;
  }

  miny--;
  maxy++;
  minx--;
  maxx++;
  
  queue<int> q;
  q.push(miny);
  q.push(minx);
  m[miny][minx] = 2;
  
  while (!q.empty()) {
    y = q.front(); q.pop();
    x = q.front(); q.pop();

    REP(d,4) {
      int ny=y+dy[d], nx=x+dx[d];
      int my=y+2*dy[d], mx=x+2*dx[d];
      if (ny<miny || ny>maxy || nx<minx || nx>maxx) continue;
      if (m[ny][nx] != 0) continue;
      if (m[my][mx] != 0) continue;
      m[my][mx]=2;
      q.push(my);
      q.push(mx);
    }
  }

  int res=0;
  
  for(y=miny+2; y<maxy; y+=2) {
    int fr=minx; while (m[y][fr]==2) fr+=2;
    int to=maxx; while (m[y][to]==2) to-=2;

    for (x=fr; x<=to; x+=2)
      if (m[y][x]==2) { m[y][x]=3; res++; }
  }
  
  for(x=minx+2; x<maxx; x+=2) {
    int fr=miny; while (m[fr][x]>=2) fr+=2;
    int to=maxy; while (m[to][x]>=2) to-=2;

    for (y=fr; y<=to; y+=2)
      if (m[y][x]==2) { m[y][x]=3; res++; }
  }
  /*
  printf ("\n");
  FOR(y,miny,maxy+1) {
    FOR(x,minx,maxx+1)
      printf ("%c",m[y][x]==0?'.':m[y][x]==1?'#':m[y][x]==2?'o':'X');
    printf ("\n");
  }
  */
  printf ("%i",res);
}

int main () {

  int runs;
  scanf ("%i\n",&runs);

  for (int run=1; run<=runs; run++) {
    printf ("Case #%i: ",run);
    solve();
    printf ("\n");
  }

  return 0;
}
