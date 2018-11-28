// login: 001963
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <map>
#include <set>      
#include <algorithm>
#include <cmath>
#include <cctype>
#include <cassert>
#include <cstdio>
#include <numeric>
#include <limits>
#include <functional>

using namespace std;

#define ALL(c) (c).begin(), (c).end()
#define DBG(x) cout << #x << " = " << x << endl


typedef long long ll;
typedef pair<int,int> ii;
typedef pair<ii,int> iii;
typedef vector<int> vi;
typedef vector< vi > vvi;
typedef vector< ii > vii;
typedef vector< vii > vvii;
typedef unsigned int uint;

#define DEBUG

const int lim = 501;
const ll mod = 100003;

ll c[lim][lim];
ll d[lim][lim];

ll f(int m, int n)
{
  if (m >= n) {
    return 0;
  }

  if (m == 1) {
    return 1;
  }

  if (d[m][n] == -1) {
    d[m][n] = 0;
    for (int k = 1;k <= m - 1;++k) {
      if (n - m - 1 >= 0 && m - k - 1 >= 0) {
        d[m][n] = (d[m][n] + (f(k,m) * c[n - m - 1][m - k - 1]) % mod) % mod;
      }
    }
  }

  return d[m][n];
}

int main()
{
  #ifdef DEBUG
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
  #endif

  c[0][0] = 1;

  for (int i = 0;i < lim;++i) {
    c[i][i] = 1;
    c[i][0] = 1;
    for (int j = 1;j < i;++j) {
      c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % mod;
    }
  }

  int T;
  cin >> T;

  for (int test = 1;test <= T;++test) {
    int n;
    memset(d,-1,sizeof(d));
    cin >> n;

    ll res = 0;
    for (int i = 1;i <= n - 1;++i) {
      res = ( res + f(i,n) ) % mod;
    }

    cout << "Case #" << test << ": " << res << endl;
  }


  #ifdef DEBUG
    fclose(stdin);
    fclose(stdout);
  #endif
  
  return 0;
}
