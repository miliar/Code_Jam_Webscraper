#include <cstdio>
#include <cstring>

#include <algorithm>

using namespace std;

typedef pair<int,int> II;

#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)

#define INF 1000000000

int H, W;
int A[128][128];
II D[128][128];
int dr[] = {-1,  0,  0, +1};
int dc[] = { 0, -1, +1,  0};

char S[128][128];

void flood_fill(II p, char ch) {
   S[p.first][p.second] = ch;
   for (int k = 0; k < 4; ++k) {
      II np(p.first+dr[k], p.second+dc[k]);
      if (D[np.first][np.second] == p)
         flood_fill(np, ch);
   }
}

int main(int argc, char* argv[]) {
   int T;
   scanf("%d", &T);
   FOR(t, 1, T) {
      scanf("%d %d", &H, &W);
      FOR(r, 0, H+1)
         FOR(c, 0, W+1) {
            A[r][c] = INF;
            D[r][c] = II(0,0);
         }
      FOR(r, 1, H)
         FOR(c, 1, W)
            scanf("%d", &A[r][c]);
      FOR(r, 1, H)
         FOR(c, 1, W) {
            D[r][c] = II(r,c);
            REP(k, 4) {
               int nr = r + dr[k], nc = c + dc[k];
               if (A[nr][nc] < A[D[r][c].first][D[r][c].second])
                  D[r][c] = II(nr,nc);
            }
         }

      memset(S, ' ', sizeof(S));
      char ch = 'a';
      FOR(r, 1, H)
         FOR(c, 1, W) {
            if (S[r][c] != ' ') continue;
            II p(r,c);
            while (p != D[p.first][p.second])
               p = D[p.first][p.second];
            flood_fill(p, ch);
            ++ch;
         }

      printf("Case #%d:\n", t);
      FOR(r, 1, H) {
         FOR(c, 1, W) {
            if (c > 1)
               putchar(' ');
            putchar(S[r][c]);
         }
         putchar('\n');
      }
   }
   return 0;
}
