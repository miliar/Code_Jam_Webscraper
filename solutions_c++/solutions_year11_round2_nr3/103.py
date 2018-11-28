#include <iostream>
#include <vector>
using namespace std;

int N, M, ncomp;
vector<int> comp[16], e[16];
bool edge[16][16], cont[16][16];
int compsz[16];

bool check(int idx, vector<int>& cur, vector<int>& ct, int ncolor) {
  for (int i = 0; i < comp[idx].size(); i++)
    if (ct[comp[idx][i]] == compsz[comp[idx][i]]) {
      int c = comp[idx][i];
      vector<bool> seen(ncolor, false);
      for (int j = 0; j <= idx; j++)
        if (cont[c][j])
          seen[cur[j]] = true;
      for (int j = 0; j < ncolor; j++)
        if (!seen[j])
          return false;
    }
  return true;
}

bool go(int idx, vector<int>& cur, vector<int>& ct, int ncolor) {
  if (cur.size() == N) return true;

  for (int i = 0; i < ncolor; i++) {
    cur.push_back(i);
    for (int j = 0; j < comp[idx].size(); j++) ct[comp[idx][j]]++;

    bool res = false;
    if (check(idx, cur, ct, ncolor)) res = go(idx+1, cur, ct, ncolor);
    if (res) return true;

    for (int j = 0; j < comp[idx].size(); j++) ct[comp[idx][j]]--;
    cur.pop_back();
  }
  return false;
}

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    cin >> N >> M;
    memset(edge, 0, sizeof(edge));
    int U[16], V[16];
    for (int i = 0; i < M; i++) cin >> U[i];
    for (int i = 0; i < M; i++) cin >> V[i];
    for (int i = 0; i < M; i++)
      edge[U[i]-1][V[i]-1] = edge[V[i]-1][U[i]-1] = true;

    for (int i = 0; i < N; i++) {
      int a = (i+N-1)%N, b = (i+1)%N;
      edge[a][i] = edge[i][a] = true;
      edge[b][i] = edge[i][b] = true;
    }

    ncomp = 0;
    memset(cont, 0, sizeof(cont));
    memset(compsz, 0, sizeof(compsz));
    for (int i = 0; i < N; i++) {
      comp[i].clear(); e[i].clear();

      for (int j = i+N-1; j > i; j--)
        if (edge[i][j%N])
          e[i].push_back(j%N);

//      cout << "edge " << i << ": ";
//      for (int j = 0; j < e[i].size(); j++)
//        cout << e[i][j] << " ";
//      cout << endl;

      for (int j = 1; j < e[i].size(); j++) {
        int a = e[i][j-1], b = e[i][j];
        if (a < i) {
          for (int k = 0; k < e[a].size(); k++)
            if (e[a][k] == i) {
              comp[i].push_back(comp[a][k-1]);
              break;
            }
        } else if (b < i) {
          for (int k = 0; k < e[b].size(); k++)
            if (e[b][k] == i) {
              comp[i].push_back(comp[b][k-1]);
              break;
            }
        } else
          comp[i].push_back(ncomp++);
      }

      for (int j = 0; j < comp[i].size(); j++) {
        cont[comp[i][j]][i] = true;
        compsz[comp[i][j]]++;
      }

//      cout << "comp " << i << ": ";
//      for (int j = 0; j < comp[i].size(); j++)
//        cout << comp[i][j] << " ";
//      cout << endl;
    }

    int mincsz = N;
    for (int i = 0; i < ncomp; i++)
      mincsz = min(mincsz, compsz[i]);

    vector<int> res;
    int best = 1;
    for (int i = mincsz; i > 1; i--) {
      vector<int> ct(ncomp, 0);
      go(0, res, ct, i);
      if (res.size() != 0) { best = i; break; }
    }
    if (res.size() == 0) res = vector<int>(N, 0);

    cout << "Case #" << c << ": " << best << endl;
    for (int i = 0; i < res.size(); i++)
      cout << res[i]+1 << (i == res.size()-1 ? "\n" : " ");
  }
  return 0;
}
