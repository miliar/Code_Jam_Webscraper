#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int _a;

#define FOR(i , n) for(int i = 0 ; i < n ; i++)
#define FOT(i , a , b) for(int i = a ; i < b ; i++)
#define GETINT (scanf("%d" , &_a) , _a)
#define pb push_back
#define mp make_pair
#define s(a) (int(a.size()))
#define PRINT(a) cerr << #a << " = " << a << endl
#define ALL(a) (a).begin(), (a).end()

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector< vs > vvs;
typedef pair<int , int> PII;

int main() {
  int T;
  cin >> T;
  FOR(test, T) {
    int n, k, b, t;
    cin >> n >> k >> b >> t;
    vi x, v; int _aa;

    FOR(i, n) { cin >> _aa; x.pb(_aa); }
    FOR(i, n) { cin >> _aa; v.pb(_aa); }
    
    int swaps = 0;
    int want = k;
    
    for(int i = n - 1; want > 0 && i >= 0; i--) {
      if(ll(t)*v[i]+x[i] >= b) want--;
      else swaps += want;
    }
    
    printf("Case #%d: ", 1+test);
    if(want == 0) printf("%d\n", swaps);
    else printf("IMPOSSIBLE\n");    
  }
  return 0;
}
