#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>

using namespace std;

#define LET(x,a) typeof(a) x(a)
#define FOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define REP(i,n) FOR(i,0,n)
#define EACH(x,v) FOR(x,(v).begin(),(v).end())
#define sz size()
#define pb push_back
#define DBG(x) cout<< #x << " --> "<< x << "\t"
#define DBE(x) cout<< #x << " --> "<< x << "\n"
#define GI ({int t; scanf(" %d", &t); t;})
typedef pair<int,int> PII;
typedef long long LL;

using namespace std;

int main() {
  int T = GI;
  REP(kase, T) {
    int N = GI, K = GI;
    int val = (1<<N) - 1;
    //DBE((1<<N));
    if (K % (1<<N) == val )
      cout << "Case #" << kase+1 << ": ON\n";
    else
      cout << "Case #" << kase+1 << ": OFF\n";
  }
  return 0;
}
