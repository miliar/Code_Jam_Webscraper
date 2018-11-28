#include <iostream>
#include <vector>
using namespace std;

// Stanford ACM Notebook Bipartite Matching Code

typedef vector<int> VI;
typedef vector<VI> VVI;

bool FindMatch (int i, const VVI &w, VI &mr, VI &mc, VI &seen){
  for (int j = 0; j < w[i].size(); j++){
    if (w[i][j] && !seen[j]){
      seen[j] = true;
      if (mc[j] < 0 || FindMatch (mc[j], w, mr, mc, seen)){
        mr[i] = j;
        mc[j] = i;
        return true;
      }
    }
  }
  return false;
}

int BipartiteMatching (const VVI &w, VI &mr, VI &mc){
  mr = VI (w.size(), -1);
  mc = VI (w[0].size(), -1);

  int ct = 0;
  for (int i = 0; i < w.size(); i++){
    VI seen (w[0].size());
    if (FindMatch (i, w, mr, mc, seen)) ct++;
  }

  return ct;
}

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    int n, m; cin >> n >> m;
    VVI w(n, VI(n, 0));
    VVI pr(n, VI(m, 0));
    for (int i = 0; i < n; i++)
      for (int j = 0; j < m; j++)
        cin >> pr[i][j];

    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++) {
        bool cross = false;
        for (int k = 0; k < m; k++) {
          if (pr[i][k] == pr[j][k]) {
            cross = true;
            break;
          }
          if (k < m-1 && ((pr[i][k] > pr[j][k]) ^ (pr[i][k+1] > pr[j][k+1]))) {
            cross = true;
            break;
          }
        }
        if (!cross) {
          if (pr[i][0] < pr[j][0]) w[i][j] = 1;
          else w[j][i] = 1;
        }
      }

    VI mr, mc;
    int sz = BipartiteMatching(w, mr, mc);
    cout << "Case #" << c << ": " << n - sz << endl;
  }
  return 0;
}
