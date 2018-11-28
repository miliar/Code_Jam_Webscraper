#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

int main() {
  int K, N, T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cin >> N >> K;
    int price[N][K];
    for (int i = 0; i < N; ++i)
      for (int j = 0; j < K; ++j)
        cin >> price[i][j];
    bool share[N][N];
    for (int i = 0; i < N; ++i) {
      share[i][i] = true;
      for (int j = i+1; j < N; ++j) {
        bool ok = true;
        for (int k = 0; k < K && ok; ++k)
          if (price[i][k] == price[j][k])
            ok = false;
        for (int k = 0; k < K-1 && ok; ++k) {
          if (price[i][k] <= price[j][k] && price[i][k+1] >= price[j][k+1])
            ok = false;
          if (price[i][k] >= price[j][k] && price[i][k+1] <= price[j][k+1])
            ok = false;
        }
        share[i][j] = share[j][i] = ok;
      }
    }
    int best = 0;
    for (int i = 1; i < (1<<N); ++i) {
      vector<int> stock;
      for (int j = 0; j < N; ++j)
        if ((i&(1<<j))>0)
          stock.push_back(j);
      bool ok = true;
      for (int a = 0; a < stock.size() && ok; ++a)
        for (int b = a+1; b < stock.size() && ok; ++b)
          if (share[stock[a]][stock[b]])
            ok = false;
      if (ok) {
        best = max<int>(best, stock.size());
      }
    }
    printf("Case #%d: %d\n", t, best);
  }
  return 0;
}
