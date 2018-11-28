#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solve(const string& S) {
  vector<int> V;
  int L = S.size();
  for (int i = 0; i < L; ++i) if (S[i] == ' ') V.push_back(i);
  int K = V.size(), X, Y, Z, ans = 0;
  if (K < 3) return 0;
  for (register int x = 0; x < K-2; ++x) { X = V[x];
  for (register int y = x+1; y < K-1; ++y) { Y = V[y];
  for (register int z = y+1; z < K; ++z) { Z = V[z];
    for (int a = 0; a < X-6; ++a) if (S[a] == 'w')
    for (int b = a+1; b < X-5; ++b) if (S[b] == 'e')
    for (int c = b+1; c < X-4; ++c) if (S[c] == 'l')
    for (int d = c+1; d < X-3; ++d) if (S[d] == 'c')
    for (int e = d+1; e < X-2; ++e) if (S[e] == 'o')
    for (int f = e+1; f < X-1; ++f) if (S[f] == 'm')
    for (int g = f+1; g < X; ++g) if (S[g] == 'e')
      for (int i = X+1; i < Y-1; ++i) if (S[i] == 't')
      for (int j = i+1; j < Y; ++j) if (S[j] == 'o')
        for (int l = Y+1; l < Z-3; ++l) if (S[l] == 'c')
        for (int m = l+1; m < Z-2; ++m) if (S[m] == 'o')
        for (int n = m+1; n < Z-1; ++n) if (S[n] == 'd')
        for (int o = n+1; o < Z; ++o) if (S[o] == 'e')
          for (int q = Z+1; q < L-2; ++q) if (S[q] == 'j')
          for (int r = q+1; r < L-1; ++r) if (S[r] == 'a')
          for (int s = r+1; s < L; ++s) if (S[s] == 'm')
          {
            ++ans;
            if (ans > 10000000) ans %= 10000;
          }
  }}}
  return ans % 10000;
}

int main() {
  int N; scanf("%d\n", &N);
  string S;
  for (int t = 1; t <= N; ++t) {
    getline(cin, S);
    printf("Case #%d: %04d\n", t, solve(S));
  }
  return 0;
}

//welcome to code jam
//abcdefgXijYlmnoZqrs

