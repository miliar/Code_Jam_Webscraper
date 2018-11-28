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
typedef pair<int , int> PII;
typedef vector< PII > vpii;
int main() {
  int T;
  T = GETINT;
  FOR(test, T) {
    int r, k, n;
    r = GETINT; k = GETINT; n = GETINT;
    vi g; FOR(i, n) g.pb(GETINT);
    vpii fit; 
    set<int> seen;
    int start = 0;
    
    while(seen.find(start) == seen.end()) {
      seen.insert(start);
      int cur = 0;
      int orig = start;
      do {
        cur += g[start];
        start = (start + 1) % n;
      } while(start != orig && cur + g[start] <= k);
      fit.pb(mp(orig,cur));
    }
    
    ll tot = 0;
    while(r > 0 && start != fit[0].first) {
      tot += fit[0].second;
      fit.erase(fit.begin());
      r--;
    }
    
    if(r > 0) {
      n = s(fit);
      if(r >= n) FOR(i, n) tot += ll(r / n) * fit[i].second;
      FOR(i, r % n) tot += fit[i].second;
    }
    
    cout << "Case #" << 1 + test << ": " <<  tot << endl;
  }
}
