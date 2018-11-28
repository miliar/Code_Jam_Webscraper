#include <iostream>
#include <vector>
using namespace std;

typedef long long ent;
typedef vector<int> Vi;
typedef vector<bool> Vb;

// ent fact(int n) {
//   if (n == 0) return 1;
//   return n*fact(n - 1);
// }
// 
// ent nsk(int n, int k) {
//   if (k == 0 or k == n) return 1;
//   return nsk(n - 1, k - 1) + nsk(n - 1, k);
// }
// 
// ent des(int n) {
//   if (n == 0) return 1;
//   if (n == 1) return 0;
//   return (n - 1)*(des(n - 1) + des(n - 2));
// }
// 
// double fun(int n) {
//   if (n == 0) return 0;
//   double r = 0;
//   for (int k = 1; k <= n; ++k) {
//     r += ((nsk(n, k)*des(n - k))/double(fact(n)))*(1 + fun(n - k));
//   }
//   double p = des(n)/double(fact(n));
//   return (r + p)/(1 - p);
// }

int main() {
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    int n;
    cin >> n;
    Vi v(n);
    for (int i = 0; i < n; ++i) {
      cin >> v[i];
      --v[i];
    }
    
    int res = 0;
    Vb u(n, false);
    for (int i = 0; i < n; ++i) {
      if (u[i]) continue;
      int q = 0;
      for (int p = i; not u[p]; p = v[p]) {
        u[p] = true;
        ++q;
      }
      if (q > 1) res += q;
    }
    
    cout << "Case #" << cas << ": " << res << ".000000" << endl;
  }
}
