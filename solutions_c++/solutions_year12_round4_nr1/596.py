#include <stdio.h>
#include <queue>
#include <vector>
#include <cmath>
using namespace std;
#define FOR(q,n) for(int q=0; q<n; q++)


void solve(int _case) {
  vector<int> pos;
  vector<int> length;
  int n;
  scanf("%d", &n);
  FOR(q, n) {
    int x,y;
    scanf("%d %d",&x, &y);
    pos.push_back(x);
    length.push_back(y);
  }
  n++;
  {
    int x;
    scanf("%d", &x);
    pos.push_back(x);
    length.push_back(0);
  }
  
  vector<int> best;
  FOR(q,n) best.push_back(-1);
  queue<int> fronta;
  if (pos[0] <= length[0]) {
    best[0]=pos[0];
    fronta.push(0);
  }

  while (!fronta.empty()) {
    int f = fronta.front(); fronta.pop();
//    printf("---> %d %d\n",pos[f], best[f]);
    FOR(q, n) if (q!=f) {
      // try to swing from q to f
      int mydist = best[f];
      if (pos[q] < pos[f] - mydist || pos[q] > pos[f] + mydist) continue;
      // we have some opportunity
      int nb = abs(pos[f]-pos[q]);
      if (nb > length[q]) nb=length[q];
      if (nb > best[q]) {
        best[q] = nb;
        fronta.push(q);
      }
    }

  }

  int ok = best[n-1]>=0;


  printf("Case #%d: %s\n", _case, ok ? "YES" : "NO");
}


int main() {
  int t;
  scanf("%d", &t);
  FOR(q, t) {
    solve(q+1);
  }
}
