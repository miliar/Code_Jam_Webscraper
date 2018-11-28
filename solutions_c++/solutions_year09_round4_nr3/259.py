#include <algorithm>
#include <string>
#include <vector>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cctype>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <list>
#include <functional>
#include <numeric>
#include <bitset>
#include <ext/hash_set>
#include <ext/hash_map>
#include <stdexcept>
using namespace std;
using namespace __gnu_cxx;

typedef long long ll;
const int infinity = 1000000000;

int p[128][128];

/* der[i] es el vértice a la derecha que le corresponde al v de la izquierda */
#define maxtam 128
int der[maxtam], izq[maxtam];
bool visitado[maxtam];

vector<int> arista[maxtam];

/* Devuelve true si puede hacer un alternating path partiendo
 * de un vértice alcanzable desde v de la izquierda, y lo hace
 * (de longitud máxima) */
bool altpath(int v) {
  visitado[v] = true;
  for (int i = 0; i < arista[v].size(); i++) {
    int w = arista[v][i];
    if (izq[w] == -1 || (!visitado[izq[w]] && altpath(izq[w]))) {
      der[v] = w;
      izq[w] = v;
      return true;
    }
  }
  return false;
}

int bpm(int numizq, int numder) {
  fill(&izq[0], &izq[numder], -1);
  fill(&der[0], &der[numizq], -1);
  
  int cnt = 0;
  for (;;) {
    bool fin = true;
    fill(&visitado[0], &visitado[numizq], false);
    for (int n = 0; n < numizq; n++)
      if (der[n] == -1 && !visitado[n] && altpath(n)) { cnt++; fin = false; }
    if (fin) break;
  }
  return cnt;
}

int main() {
  int cases;
  scanf("%i\n", &cases);
  for (int caseno = 1; caseno <= cases; ++caseno) {
    printf("Case #%i: ", caseno);
    int n, k;
    scanf("%i%i", &n, &k);
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < k; ++j)
        scanf("%i", &p[i][j]);

    for (int i = 0; i < n; ++i)
      arista[i].clear();
    for (int i = 0; i < n; ++i) {
      arista[i].clear();
      for (int j = 0; j < n; ++j)
        if (p[i][0] > p[j][0]) {
          int s;
          for (s = 0; s < k; ++s)
            if (p[i][s] <= p[j][s]) break;
          if (s == k)
            arista[i].push_back(j);
        }
    }
    int r = bpm(n, n);
    printf("%i\n", n - r);
    fflush(stdout);
  }
  return 0;
}
