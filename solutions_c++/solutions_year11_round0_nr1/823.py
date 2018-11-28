#include <iostream>
#include <vector>
using namespace std;

typedef vector<int> Vi;

int main() {
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    int n;
    cin >> n;
    Vi qui(n), que(n);
    for (int i = 0; i < n; ++i) {
      char c;
      cin >> c >> que[i];
      qui[i] = (c == 'O' ? 0 : 1);
    }
    Vi va(n + 1, 17), vb(n + 1, 17);
    for (int i = n - 1; i >= 0; --i) {
      va[i] = (qui[i] == 0 ? que[i] : va[i + 1]);
      vb[i] = (qui[i] == 1 ? que[i] : vb[i + 1]);
    }
    int a = 1, b = 1, p = 0, t = 0;
    while (p < n) {
      bool ok = (qui[p] == 0 and a == que[p]) or (qui[p] == 1 and b == que[p]);
      if (a < va[p]) ++a;
      else if (a > va[p]) --a;
      if (b < vb[p]) ++b;
      else if (b > vb[p]) --b;
      if (ok) ++p;
      ++t;
    }
    cout << "Case #" << cas << ": " << t << endl;
  }
}
