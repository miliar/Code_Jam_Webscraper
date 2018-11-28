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

vs getpath() {
  string st;
  cin >> st;
  st = "root" + st;
  FOR(i, s(st)) if(st[i] == '/') st[i] = ' ';
  istringstream in(st);
  vs ret;
  string abcd;
  while(in >> abcd) ret.pb(abcd);
  return ret;
}


int main() {
  int T;
  cin >> T;
  FOR(test, T) {
    int n, m;
    cin >> n >> m;
    vvs have, want;
    FOR(i, n) have.pb(getpath());
    FOR(i, m) want.pb(getpath());

    sort(ALL(have)); sort(ALL(want));
    
    set< vs > made;
    FOR(i, n) made.insert(have[i]);
    made.insert(vs(1,"root"));
    
    int ret = 0;
    
    FOR(i, m) {
      vs cur = want[i];
      while(made.find(cur) == made.end()) {
        ret++;
        made.insert(cur);
        cur.pop_back();
      }
    }
    printf("Case #%d: %d\n", 1+test, ret);
  }
  return 0;
}
