#include <vector>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <string>
#include <cassert>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
#define PB push_back
#define ff first
#define ss second
#define rep(i, n) for(LL i = 0; i < (LL)n; i++)
#define INF (1 << 30)
#define debug(x) cout << x << endl

int T, N, S, P, t[100];
int sup, ans;

int main()
{
  
  cin >> T;
  rep(i, T) {
    ans = 0; sup = 0;
    cin >> N >> S >> P;
    rep(j, N) cin >> t[j];
    rep(j, N) {
      if (t[j] >= 3 * P - 2) ans++;
      else if(t[j] > 0 && t[j] >= 3 * P - 4) sup++;
    }
    ans += min(sup, S);
    cout << "Case #" << i + 1 << ": " << ans << endl;
  }
  return 0;
}
			       
    
    
