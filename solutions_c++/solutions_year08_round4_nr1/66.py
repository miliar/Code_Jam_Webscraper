#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
using namespace std;
 
#define all(c) ((c).begin()), ((c).end()) 
#define iter(c) __typeof((c).begin())
#define present(c, e) ((c).find((e)) != (c).end()) 
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)
 
typedef long long ll;

const int INF = 999999;

int dp[10010][2]; // dp[n][v] --- ノード n が v になるために必要なそれ以下のゲート変更数

int M;
bool leaf[10010];
int C[10010];
int A[10010];

int saiki(int n, int v) {
  if (v == 2) return min(saiki(n, 0), saiki(n, 1));

  if (dp[n][v] != -1) return dp[n][v];

  if (leaf[n]) {
    if (A[n] == v) return 0;
    else return INF;
  }

  int res = INF;
  if (A[n] == 1) { // AND gate
    if (v == 1) res <?= saiki(n * 2, 1) + saiki(n * 2 + 1, 1);
    else res <?= min(saiki(n * 2, 2) + saiki(n * 2 + 1, 0),
                     saiki(n * 2, 0) + saiki(n * 2 + 1, 2));

    if (C[n]) {
      if (v == 0) res <?= 1 + saiki(n * 2, 0) + saiki(n * 2 + 1, 0);
      else res <?= 1 + min(saiki(n * 2, 2) + saiki(n * 2 + 1, 1),
                           saiki(n * 2, 1) + saiki(n * 2 + 1, 2));
    }
  }
  else { // OR gate
    if (v == 0) res <?= saiki(n * 2, 0) + saiki(n * 2 + 1, 0);
    else res <?= min(saiki(n * 2, 2) + saiki(n * 2 + 1, 1),
                     saiki(n * 2, 1) + saiki(n * 2 + 1, 2));

    if (C[n]) {
      if (v == 1) res <?= 1 + saiki(n * 2, 1) + saiki(n * 2 + 1, 1);
      else res <?= 1 + min(saiki(n * 2, 2) + saiki(n * 2 + 1, 0),
                       saiki(n * 2, 0) + saiki(n * 2 + 1, 2));
    }
  }

  return dp[n][v] = res;
}

int main() {
  int N;
  scanf("%d", &N);
  for (int n = 1; n <= N; n++) {
    int V;
    scanf("%d%d", &M, &V);
 
    for (int i = 1; i <= (M - 1) / 2; i++) {
      leaf[i] = false;
      scanf("%d%d", &A[i], &C[i]);
      //printf("%d: %d %d\n", i, A[i], C[i]);
    }

    for (int i = (M + 1) / 2; i <= M; i++) {
      leaf[i] = true;
      scanf("%d", &A[i]);
      //printf("%d: %d\n", i, A[i]);
    }

    memset(dp, -1, sizeof(dp));
    int res = saiki(1, V);
    
    printf("Case #%d: ", n);
    if (res >= INF) puts("IMPOSSIBLE");
    else printf("%d\n", res);
  }

}
