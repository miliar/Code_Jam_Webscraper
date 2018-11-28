#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define CLR(x,a) memset(x,a,sizeof(x))
#define setmin(a,b) a = min(a,b)

int T,H,W;
int alt[100][100];
int next[100][100];
int which[100][100];
char label[26];
int nsink;

int dr[] = { -1, 0, 1, 0 },
    dc[] = { 0, -1, 0, 1 };
int ks[] = { 0, 1, 3, 2 };

void dfs(int r, int c) {
  which[r][c] = nsink;
  FOR(k,4) {
    int r2 = r+dr[k], c2 = c+dc[k];
    if (r2<0||r2>=H||c2<0||c2>=W) continue;
    if (next[r2][c2] == -1) continue;
    if ((next[r2][c2]+2)%4 != k) continue;

    assert(alt[r2][c2] > alt[r][c]);
    dfs(r2,c2);
  }
}
int cas=0;
void doit() {
  scanf("%d%d",&H,&W);

  FOR(r,H) {
    FOR(c,W) {
      scanf("%d",&alt[r][c]);
    }
  }

  FOR(r,H) {
    FOR(c,W) {
      int mn = 10000;

      FOR(k,4) {
	int r2 = r+dr[k], c2 = c+dc[k];
	if (r2<0||r2>=H||c2<0||c2>=W) continue;
	setmin(mn, alt[r2][c2]);
      }

      if (mn >= alt[r][c]) {
	next[r][c] = -1;
      } else {
	FOR(zz,4) {
	  int k = ks[zz];
	  int r2 = r+dr[k], c2 = c+dc[k];
	  if (r2<0||r2>=H||c2<0||c2>=W) continue;
	  if (alt[r2][c2] == mn) {
	    next[r][c] = k;
	    break;
	  }
	}
      }
    }
  }

  nsink=0;
  FOR(r,H) {
    FOR(c,W) if (next[r][c] == -1) {
      dfs(r,c);
      ++nsink;
      assert(nsink <= 26);
    }
  }

  char nextlabel = 'a';
  CLR(label,0);
  printf("Case #%d:\n",++cas);
  FOR(r,H) {
    FOR(c,W) {
      if (c) printf(" ");
      if (!label[which[r][c]]) {
	label[which[r][c]] = nextlabel++;
      }
      printf("%c",label[which[r][c]]);
    }
    printf("\n");
  }
}
int main() {
  scanf("%d",&T);
  FOR(i,T) doit();
}
