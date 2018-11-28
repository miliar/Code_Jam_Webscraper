#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
using namespace std;

typedef long long ll;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int test_count;
  cin >> test_count;
  for (int test_index = 0; test_index < test_count; ++test_index) {
    vector<int> prime[1000];
    for (int i = 0; i < 1000; ++i)
      prime[i].resize(1001);
    int n;
    
    cin >> n;
    if (n == 1)
    {
      cout << "Case #" << test_index + 1 << ": " << 0<< endl;
      continue;
    }
    for (int i = 0; i < n; ++i) {
      int numb = i + 1;
      for (int j = 2; j * j <= numb; ++j) {
        while (numb % j == 0) {
          ++prime[i][j];
          numb /= j;
        }
      }
      if (numb > 1)
        ++prime[i][numb];
    }
    int lcm[1001];
    memset(lcm, 0, sizeof(lcm));
    int min_res = 0;
    for (int j = 0; j < 1001; ++j)
      for (int i = 0; i < n; ++i)
        lcm[j] = max(lcm[j], prime[i][j]);
    for (int i = 0; i < 1001; ++i)
      if (lcm[i])
        ++min_res;
    int max_res = 1;
    for (int i = 0; i < 1001; ++i)
      max_res += lcm[i];

    cout << "Case #" << test_index + 1 << ": " << max_res - min_res << endl;
  }
  return 0;
}