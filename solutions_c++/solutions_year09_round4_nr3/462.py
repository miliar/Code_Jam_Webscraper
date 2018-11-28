#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <math.h>
using namespace std;

#define all(V) (V).begin(),(V).end()
#define rall(V) (V).rbegin(),(V).rend()
#define _foreach(it, a, b) for (typeof(a) it = a; it != b; ++it)
#define foreach(x...) _foreach(x)
#define fu(a, b) foreach(a, 0, b)
#define MSET(a, b) memset(a, b, sizeof(a))
int aresta[20][20];
vector<int> preco[20];
int main() {
  int _42;
  scanf("%d", &_42);
  fu(_41, _42) {
    printf("Case #%d: ", _41+1);
    MSET(aresta, 0);
    int n, k;
    scanf("%d %d", &n, &k);
    fu(i, n) {
      preco[i].clear();
      fu(j, k) {
        int a;
        scanf("%d", &a);
        preco[i].push_back(a);
      }
    }
    fu(i, n) fu(j, i) {
      if (preco[i][0] == preco[j][0]) {
        aresta[i][j] = aresta[j][i] = 1;
        continue;
      }
      bool acima = true;
      if (preco[i][0] < preco[j][0])
        acima = false;
      fu(ii, k) {
        if (acima && preco[i][ii] <= preco[j][ii]) {
          aresta[i][j] = aresta[j][i] = 1;
          continue;
        }
        if (!acima && preco[i][ii] >= preco[j][ii]) {
          aresta[i][j] = aresta[j][i] = 1;
          continue;
        }
      }
    }
    int resp = 0;
    fu (m, 1<<n) if (__builtin_popcount(m) > resp) {
      bool foi = true;
      fu(i, n) if ((m >> i) & 1) fu(j, i) if ((m>>j)&1) {
        if (aresta[i][j] == 0)
          foi = false;
      }
      if (foi)
        resp = __builtin_popcount(m);
    }
    printf("%d\n", resp);
  }
  return 0;
}
