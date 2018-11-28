#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <bitset>
#include <numeric>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <sys/time.h>
#include <regex.h>

using namespace std;

#define DEBUG(x) cout << #x << ": " << x << endl

#define sz(a) int((a).size())

#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

#define REPD(i,n) for(int i=(n)-1;i>=0;--i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACHD(it,c) for(typeof((c).rbegin()) it=(c).rbegin();it!=(c).rend();++it)

#define ALL(c) (c).begin(),(c).end()

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;

typedef pair<int,int> II;

int main(int argc, char *argv[]) {
   int N;
   cin >> N;

   for (int tc = 1; tc <= N; ++tc) {
      int n;
      cin >> n;
      vector<long long> v1(n), v2(n);
      REP(i, n)
         cin >> v1[i];
      REP(i, n)
         cin >> v2[i];
      sort(ALL(v1));
      sort(ALL(v2));
      reverse(ALL(v2));
      long long res = 0;
      REP(i, n)
         res += v1[i]*v2[i];
      cout << "Case #" << tc << ": " << res << endl;
   }

   return 0;
}
