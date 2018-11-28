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

int n,k,b,t;
ll x[51];
ll v[51];
bool can[51];


int main()
{
  #ifdef DEBUG
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
  #endif

  int T;
  cin >> T;

  for (int test = 1;test <= T;++test) {
    cin >> n >> k >> b >> t;

    for (int i = 0;i < n;++i) {
      cin >> x[i];
    }

    for (int i = 0;i < n;++i) {
      cin >> v[i];
    }

    for (int i = 0;i < n;++i) {
      if (x[i] + t * v[i] < b) {
        can[i] = false;
      } else {
        can[i] = true;
      }
    }

    int res = 0;
    for (int i = n - 1;i >= 0;--i) {
      if (k && can[i]) {
        for (int j = i + 1;j < n;++j) {
          if (!can[j]) {
            ++res;
          }
        }
        --k;
      }
    }

    cout << "Case #" << test << ": ";
    if (k == 0) {
      cout << res << endl;
    } else {
      cout << "IMPOSSIBLE" << endl;
    }
  }


  #ifdef DEBUG
    fclose(stdin);
    fclose(stdout);
  #endif
  
  return 0;
}
