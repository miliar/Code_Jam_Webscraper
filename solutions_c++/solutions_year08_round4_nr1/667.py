#include <iostream>

using namespace std;

const int maxM = 10000 + 10;
const int INF = 10000000;


int N, M, V;

int f[maxM][2];
int G[maxM];
int C[maxM];

void find(int u) {
  int l, r;
  if ((l = u * 2) <= M) {
    find(l);
  } else {
    return;
  }
  if ((r = u * 2 + 1) <= M) {
    find(r);
  }
  int or0, or1, and0, and1;
  or0 = f[l][0] + f[r][0];
  or1 = min(min(f[l][0] + f[r][1], f[l][1] + f[r][0]), f[l][1] + f[r][1]);
  and0 = min(min(f[l][0] + f[r][0], f[l][0] + f[r][1]), f[l][1] + f[r][0]);
  and1 = f[l][1] + f[r][1];

  if (C[u] == 1) {
    if (G[u] == 0) {
      f[u][0] = min(or0, and0 + 1);
      f[u][1] = min(or1, and1 + 1);
    } else {
      f[u][0] = min(or0 + 1, and0);
      f[u][1] = min(or1 + 1, and1);
    }
  }
  else
  {
    if (G[u] == 0) {
      f[u][0] = or0;
      f[u][1] = or1;
    } else {
      f[u][0] = and0;
      f[u][1] = and1;
    }
  }
}

int main()
{
  int i;
  cin >> N;
  for (int e = 1; e <= N; ++e) {
    cout << "Case #" << e << ": ";
    cin >> M >> V;
    for (i = 1; i <= (M - 1) / 2; ++i) {
      cin >> G[i] >> C[i];
    }
    for (; i <= M; ++i) {
      int t;
      cin >> t;
      f[i][t] = 0;
      f[i][!t] = INF;
    }
    find(1);
    int result = f[1][V];
    if (result >= INF) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << result << endl;
    }
  }
  return 0;
}

