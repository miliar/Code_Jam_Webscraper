#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <climits>
#include <cctype>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <list>

#define FOR(i, m, n) for (int i=m; i<n; i++)

using namespace std;

int L, N, C;
long long t;
int dist[2000000];
vector<int> vect;

void solve() {
  vect.clear();
  scanf("%d%lld%d%d", &L, &t, &N, &C);
  FOR (i, 0, C) {
    int a; scanf("%d", &a);
    int k = 0;
    while (k*C+i<N) {
      dist[k*C+i] = a;
      k++;
    }
  }
  int D = 0;
  FOR (i, 0, N) {
    if (D>=t)
      vect.push_back(2*dist[i]);
    else if (D+2*dist[i]>=t)
      vect.push_back(D+2*dist[i]-t);
    D += 2*dist[i];
  }
  sort(vect.begin(), vect.end());
  for (int i=0, j=vect.size()-1; i<L && i<vect.size(); i++, j--)
    D -= vect[j]/2;
  printf("%d\n", D);
}

int main() {
  int T; scanf("%d", &T);
  FOR (qq, 0, T) {
    printf("Case #%d: ", qq+1);
    solve();
  }
  return 0;
}
