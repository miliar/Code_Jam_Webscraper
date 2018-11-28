
#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <cstring>

using namespace std;

int main()
{
  int N;
  cin >> N;

  for (int cas = 1; cas <= N; cas++) {
    vector<unsigned> arr;
    int m, n;
    cin >> m >> n;
    for (int i = 0; i < m; i++) {
      string x;
      cin >> x;
      unsigned v = 0;
      for (int j = 0; j < n; j++) {
        if (x[j] == 'x') v |= (1 << j);
      }
      //cout << v << endl;
      arr.push_back(v);
    }

#define SZ (1 << 12)
    int table[16][SZ];
    memset(table, 0, sizeof(table));

    unsigned mask = (1 << n) - 1;
    for (int i = 1; i <= m; i++) {
      for (unsigned j = 0; j < (1 << n); j++) {
        int count = table[i-1][j];
        for (unsigned k = 0; k <= (~j & mask); k++) {
          if (k & (k << 1)) continue;
          if (k & j) continue;
          if (k & arr[m-i]) continue;
          int bits = 0;
          for (int b = 0; b < n; b++) {
            if (k & (1 << b)) bits++;
          }
          int ncount = count + bits;
          unsigned l = (k << 1) | (k >> 1);
          l &= mask;
          if (table[i][l] < ncount) {
            table[i][l] = ncount;
            //cout << i << " " << j << " " << l << " " << k << " " << ncount << endl;
          }
        }
      }
    }

    int res = 0;
    for (unsigned j = 0; j < (1 << n); j++) {
      if (res < table[m][j]) res = table[m][j];
    }

    cout << "Case #" << cas << ": ";
    cout << res << endl;
  }
  
  return 0;
}

