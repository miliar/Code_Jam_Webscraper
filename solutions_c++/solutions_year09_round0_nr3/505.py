#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>

#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

#include <ext/hash_set>
#include <ext/hash_map>
#include <ext/numeric>
#include <ext/functional>
#include <ext/rope>
#include <ext/rb_tree>
#include <ext/iterator>
#include <ext/slist>

#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define SZ(x) ((int)(x).size())
#define REP(i, n) for(int i=0; i<n; ++i)
#define REPD(i, n) for(int i=(n)-1; i>=0; --i)
#define FOR(i, b, e) for(typeof(e) i=b; i!=e; ++i)

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef istringstream ISS;

const int INF=10000000;

string t="welcome to code jam";
string str;

int cache[1000][100];

int calc(int x, int y) {
  if(y==SZ(t)) return 1;
  if(x==SZ(str)) return 0;
  if(cache[x][y]!=-1) return cache[x][y];
  LL res=0;
  FOR(i, x, SZ(str)) if(str[i]==t[y]) res+=calc(i+1,y+1);
  return cache[x][y]=res%10000;
}

void go() {
  memset(cache,-1,sizeof(cache));
  getline(cin, str);
  printf("%04d\n", calc(0, 0));
}

int main() {
  int nruns;
  cin >> nruns;
  string tmp;
  getline(cin,tmp);
  REP(i, nruns) {
    cout << "Case #" << (i+1) <<": ";
    go();
  }
  return 0;
}
