#include<algorithm>
#include<bitset>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<deque>
#include<functional>
#include<iostream>
#include<limits>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<string>
#include<vector>
#include<numeric>
#include<ext/numeric>  // iota
//#include<ext/hash_set>
//#include<ext/hash_map>

using namespace std;
using namespace __gnu_cxx; // Pour utiliser les ext/...

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int, int> pii;
//typedef int int128 __attribute__ ((mode(TI)));
//typedef unsigned int uint128 __attribute__ ((mode(TI)));

#define MAX 10002

int infty = numeric_limits<int>::max();

int T, N, D;
int dist[MAX];
int length[MAX];
int mark[MAX][MAX];

int reachable(int start, int held) {
  //printf("reachable %d %d\n", start, held);
  int pos_start = 0;
  int i;
  if (start >= 0 && mark[start][held]) return 0; // NO
  if (start == held) return 0;
  if (start >= 0) mark[start][held] = 1;
  if (start >= 0) {
    pos_start = dist[start];
    pos_start = min(pos_start, dist[held] + length[held]);
    pos_start = max(pos_start, dist[held] - length[held]);
  }
  if (start < held) {
    if (pos_start + 2*(dist[held] - pos_start) >= D) {
      return 1;
    }
    //printf("from %d to %d\n", start+1, N);
    for (i=held+1; i<N; i++) {
      //printf("from %d %d consider %d %d\n", start, pos_start, i, dist[i]);
      //if (dist[i] <= pos_start) continue;
      //if (dist[i] > pos_start + 2*(dist[held] - pos_start))
      if (dist[i] > dist[held] + (dist[held] - pos_start))
        break;
      if (reachable(held, i)) return 1;
    }
  } else {
    for (i=held-1; i>=0; i--) {
      //if (dist[i] <= pos_start) continue;
      if (dist[i] < dist[held] - (pos_start - dist[held]))
        break;
      if (reachable(held, i)) return 1;
    }
  }
  //printf("end\n");
  return 0;
}

int main(int argc, char **argv) {
  int i, j, k;
  scanf("%d", &T);
  for (i=0; i<T; i++) {
    scanf("%d", &N);
    for (j=0; j<N; j++) {
      scanf("%d", &(dist[j]));
      scanf("%d", &(length[j]));
    }
    for (j=0; j<N; j++) {
      for (k=0; k<N; k++) {
        mark[j][k] = 0;
      }
    }
    scanf("%d", &D);
    printf("Case #%d: %s\n", i+1, reachable(-1, 0) ? "YES" : "NO");
  }
}
