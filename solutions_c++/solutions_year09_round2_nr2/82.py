#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>

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

void go() {
  string s;
  cin >> s;
  if(next_permutation(ALL(s))) cout << s << endl;
  else {
    int i=0;
    while(s[i]=='0') i++;
    cout << s[i] << "0" << s.substr(0,i) << s.substr(i+1) << endl;
  }
}

int main() {
  int nruns;
  cin >> nruns;
  REP(i, nruns) {
//    printf("Ikben hier %d\n",i)
    cout << "Case #" <<i+1<<": ";
    go();
  }
}

