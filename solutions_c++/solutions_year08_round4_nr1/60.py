#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cctype>
#include <vector>
#include <map>

using namespace std;

#define rep(i,n) for (int i=0;i<(n);i++)
#define foru(i,a,b) for (int i=(a);i<=(b);i++)
#define ford(i,a,b) for (int i=(a);i>=(b);i--)

const int maxn = 1000000, inf = 1000000000;
const int AND = 1, OR = 0;

int cas, n, tar;
int chg[maxn], opr[maxn], g[maxn][2], vl[maxn];

int calc(int a, int b, int c) {
  if (a + b + c > inf) return inf;
  return a + b + c;
}

void solve() {
  ford(i, n, 1) {    
    g[i][0] = g[i][1] = inf;
    if (opr[i] == -1) {
      g[i][vl[i]] = 0;
      continue;
    }
    if (chg[i]) {
      rep(a, 2) rep(b, 2) {
	if (a & b) {
	  g[i][1] <?= calc(g[i * 2][a], g[i * 2 + 1][b], opr[i] == OR);
	} else {
	  g[i][0] <?= calc(g[i * 2][a], g[i * 2 + 1][b], opr[i] == OR);
	}
	
	if (a | b) {
	  g[i][1] <?= calc(g[i * 2][a], g[i * 2 + 1][b], opr[i] == AND);	
	} else {
	  g[i][0] <?= calc(g[i * 2][a], g[i * 2 + 1][b], opr[i] == AND);
	}      	
      }
    } else {
      if (opr[i] == OR) 
	rep(a, 2) rep(b, 2) g[i][a|b] <?= g[i * 2][a] + g[i * 2 + 1][b];
      if (opr[i] == AND)
	rep(a,2) rep(b,2) g[i][a&b] <?= g[i*2][a] + g[i*2 + 1][b];
    }
    
  }
  //  foru(i, 1, n) printf("%d %d\n", g[i][0], g[i][1]);
  if (g[1][tar] == inf) 
    printf("IMPOSSIBLE\n");
  else
    printf("%d\n", g[1][tar]);
    
}

int main() {
  scanf("%d", &cas);
  rep(tt, cas) {
    scanf("%d%d", &n, &tar);
    foru(i, 1, (n - 1) / 2) {
      scanf("%d%d", &opr[i], &chg[i]);      
    }
    foru(i, (n - 1) / 2 + 1, n) {
      opr[i] = -1;
      scanf("%d", &vl[i]);
    }
    printf("Case #%d: ", tt + 1);
    solve();
  }    
}
