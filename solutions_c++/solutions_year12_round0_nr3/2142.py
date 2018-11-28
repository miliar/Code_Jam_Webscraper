#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef long long ll;
typedef vector<int> Vi;

const int SZ = 10000000;
const int LIM = 2000000;

int P10[10];

int M;
int C[SZ];

inline int digits(int n) {
  int d = 1;
  while (n >= 10) {
    n /= 10;
    ++d;
  }
  return d;
}

int main() {
  P10[0] = 1;
  for (int i = 1; i < 10; ++i) P10[i] = 10*P10[i - 1];
  
  for (int n = 0; n < SZ; ++n) C[n] = -1;
  for (int n = 0; n < SZ and n <= LIM; ++n) {
    if (C[n] != -1) continue;
    int d = digits(n);
    for (int i = 0; i < d; ++i) {
      int x = n/P10[i], y = n%P10[i];
      int z = y*P10[d - i] + x;
      if (C[z] == -1) C[z] = M;
    }
    ++M;
  }
  
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    int a, b;
    cin >> a >> b;
    
    ll res = 0;
    Vi v(M, 0);
    for (int i = a; i <= b; ++i) res += v[C[i]]++;
    
    cout << "Case #" << cas << ": " << res << endl;
  }
}
