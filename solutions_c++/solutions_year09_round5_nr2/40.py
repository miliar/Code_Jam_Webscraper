/* GCJ'09 Template v.2e-9
 * Per Austrin
 */
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cctype>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<pii> vpii;
typedef map<string, int> msi;
typedef map<vi, int> mvi;
typedef map<int, int> mii;

const int MOD = 10009;
int CASES;

void init() {
  scanf("%d", &CASES);
}

int k, n;
int dict[200][27];
int ans[27][27][27][27][11];

int Ans(int t[4], int k) {
  sort(t, t+4);
  int &res = ans[t[0]][t[1]][t[2]][t[3]][k];
  int r = 0;
  while (r < 4 && t[r] < 26) ++r;
  if (res == -1) {
    res = 0;
    if (k == 1) {
      for (int i = 0; i < n; ++i) {
	int f = 1;
	for (int j = 0; j < r; ++j)
	  (f *= dict[i][t[j]]) %= MOD;
	(res += f) %= MOD;
      }
    } else {
      for (int i = 0; i < n; ++i) {
	for (int M = 0; M < (1<<r); ++M) {
	  int f = 1, nt[4];
	  for (int j = 0; j < 4; ++j)
	    if (M & (1<<j)) {
	      (f *= dict[i][t[j]]) %= MOD;
	      nt[j] = 26;
	    } else {
	      nt[j] = t[j];
	    }
	  (res += f*Ans(nt, k-1)) %= MOD;
	}
      }
    }
    //    printf("go %d %d %d %d, %d\n", t[0], t[1], t[2], t[3], k);
    //    printf("  = %d\n", res);
  }
  return res;
}

void solve(int P) {
  char expr[2000];
  int terms[20][4];
  scanf("%s%d%d", expr, &k, &n);
  int T = 0, Ts = 0;
  for (int i = 0; i < 20; ++i)
    for (int j = 0; j< 4; ++j)
      terms[i][j] = 26;
  for (char *s = expr; *s; ++s) {
    if (*s == '+') ++T, Ts = 0;
    else terms[T][Ts++] = *s-'a';
  }
  ++T;
  memset(dict, 0, sizeof(dict));
  for (int i = 0; i < n; ++i) {
    dict[i][26] = 1;
    scanf("%s", expr);
    for (char *s = expr; *s; ++s)
      ++dict[i][*s-'a'];
    //    for (int k = 0; k < 27; ++k)    printf("%d ", dict[i][k]);
    //  printf("\n");
  }
  memset(ans, -1, sizeof(ans));
  printf("Case #%d:", P);

  for (int i = 1; i <= k; ++i) {
    int tot = 0;
    for (int t = 0; t < T; ++t)
      (tot += Ans(terms[t], i)) %= MOD;
    printf(" %d", tot);
  }
  printf("\n");
}

int main(void) {
  init();
  for (int i = 1; i <= CASES; ++i) solve(i);
  return 0;
}
