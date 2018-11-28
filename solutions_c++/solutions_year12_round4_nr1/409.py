#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
#include <complex>
using namespace std;

// begin insert defines
#define Rep(i,n) for(int n_ = (n), i = 0; i< n_; ++i)
template <class T> inline void gmax (T &a, T b) {if (a < b) a = b;}
typedef long long ll;

// end insert defines

const int N = 10000 + 10;

ll d[N], l[N];
ll lg[N], dd;

int main(int argc, char *argv[])
{
  int T;
  cin >> T;
  int n;
  Rep(Ca, T) {
    cout << "Case #" << Ca + 1 << ": ";
    cin >> n;
    Rep(i, n) cin >> d[i] >> l[i];
    cin >> dd;
    memset(lg, 0, sizeof(lg));
    lg[0] = d[0];
    Rep(i, n) {
      for (int j = i + 1; j < n && d[i] + lg[i] >= d[j]; j++) {
          gmax(lg[j], min(l[j], d[j] - d[i]));
      }
    }
    bool lab = false;
    for (int i = 0; i < n; i++)
      if (lg[i] + d[i] >= dd)
        lab = true;
    if (lab) cout << "YES" << endl;
    else cout << "NO" << endl;
  }
  return 0;
}
