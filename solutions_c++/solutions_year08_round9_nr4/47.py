#include <iostream>
#include <cstdio>

#include <map>
#include <queue>
#include <set>
#include <vector>
#include <string>

#include <cmath>
#include <algorithm>
#include <sstream>
#include <ctype.h>

#define FOR(i,a,b) for (int i=(a); i<(int)(b); i++)
#define FI(b)      FOR(i,0,b)
#define FJ(b)      FOR(j,0,b)
#define FK(b)      FOR(k,0,b)
#define FC(b)      FOR(c,0,b)
#define EACH(x,it) for(__typeof(x.begin()) it=x.begin(); it!=x.end(); it++)

#define ZERO(x) memset((x),0,sizeof(x))
#define NEG(x) memset((x),-1,sizeof(x))

#define ASIZE(x) sizeof(x) / sizeof(x[0])

using namespace std;

string m[55];
int dist[2][55][55];
int pr[2][55][55];
int pc[2][55][55];
int rown,coln;
int dx[] = {-1,0,1,0};
int dy[] = {0,-1,0,1};
bool sp[55][55];

void bfs(int id, int startr, int startc) {
   queue<pair<pair<int,int>,int> > q;
   q.push(make_pair(make_pair(startr,startc), 0));

   while(!q.empty()) {
      int r = q.front().first.first;
      int c = q.front().first.second;
      int curdist = q.front().second;
      q.pop();

      if (m[r][c] != '.') {
         FOR(d,0,4) {
            int nr=r+dx[d], nc=c+dy[d];
            if (nr>=0 && nc>=0 &&nr<rown && nc<coln && dist[id][nr][nc] == -1) {
               q.push(make_pair(make_pair(nr,nc), curdist+1));
               dist[id][nr][nc] = curdist+1;
               pr[id][nr][nc] = r;
               pc[id][nr][nc] = c;
            }
         }
      }
   }
}

int main() {
   int cases;
   cin >> cases;

   FC(cases) {
      cin >> rown>>coln;
      FI(rown) cin >> m[i];

      int fr,fc;
      FI(rown) FJ(coln) if (m[i][j]=='T') { fr = i; fc=j; }

      NEG(dist);
      bfs(0, 0, 0);
      bfs(1, fr, fc);

      ZERO(sp);
      int rr=fr, cc=fc;
      int ans=0;
      while(rr != 0 || cc != 0) {
         ans += dist[0][rr][cc];
         sp[rr][cc] = 1;
         int rr2, cc2;
         rr2 = pr[0][rr][cc]; cc2 = pc[0][rr][cc];
         rr = rr2; cc = cc2;
      }

      FI(rown) FJ(coln) {
         if (m[i][j] == '#' && !sp[i][j]) {
            ans += dist[0][i][j] <? dist[1][i][j];
         }
      }
      //FI(rown) { FJ(coln) cout << dist[0][i][j]; cout <<endl; }

      cout << "Case #" << (c+1) <<": "<<ans<<endl;
   }
}
