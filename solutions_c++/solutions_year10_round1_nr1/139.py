#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;
typedef long long i64;

const int di[] = {+1, 0, +1, +1};
const int dj[] = {0, +1, -1, +1};
const string tokens = "RB";
const string answers[] = {"Neither", "Red", "Blue", "Both"};

vector<string> RotateRight(const vector<string>& v1) {
  const int n = (int)v1.size();
  vector<string> v2(n, string(n, '?'));
  for (int i = 0; i < n; ++i) for (int j = 0; j < n; ++j)
    v2[j][n - 1 - i] = v1[i][j];
  return v2;
}
void MakeFall(vector<string>& v) {
  const int n = (int)v.size();
  for (int j = 0; j < n; ++j) {
    for (int i = n - 1, low = n; i >= 0; --i) if (v[i][j] != '.') {
      for (; low > 0 && v[low - 1][j] != '.'; --low);
      if (i < low) swap(v[i][j], v[low - 1][j]);
    }
  }
}
bool HasRow(const vector<string>& v, char c, int x) {
  const int n = (int)v.size();
  bool ok = false;
  for (int i = 0; i < n && !ok; ++i) for (int j = 0; j < n && !ok; ++j) if (v[i][j] == c)
    for (int o = 0; o < 4 && !ok; ++o) {
      const int li = i + di[o] * (x - 1), lj = j + dj[o] * (x - 1);
      ok = li >= 0 && li < n && lj >= 0 && lj < n;
      for (int k = 0; k < x && ok; ++k)
        ok = v[i + di[o] * k][j + dj[o] * k] == c;
    }
  return ok;
}
int main() {
  int T; scanf("%d", &T);
  for (int Ti = 1; Ti <= T; ++Ti) {
    int n, k; scanf("%d %d", &n, &k);
    vector<string> v;
    for (int i = 0; i < n; ++i) {
      char str[100]; scanf("%s", str);
      v.push_back(string(str));
    }
    MakeFall(v = RotateRight(v));
    int res = 0;
    for (int i = 0; i < (int)tokens.size(); ++i)
      if (HasRow(v, tokens[i], k))
        res |= 1 << i;
    printf("Case #%d: %s\n", Ti, answers[res].c_str());
  }
  return 0;
}
