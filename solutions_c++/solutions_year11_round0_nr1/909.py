#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<cassert>
#include<climits>
using namespace std;

#define REP(i,n) for(int i=0, _e(n); i<_e; i++)
#define FOR(i,a,b) for(int i(a), _e(b); i<=_e; i++)
#define FORD(i,a,b) for(int i(a), _e(b); i>=_e; i--) 
#define FORIT(i, m) for (__typeof((m).begin()) i=(m).begin(); i!=(m).end(); ++i)
#define SET(t,v) memset((t), (v), sizeof(t))
#define ALL(x) x.begin(), x.end()
#define UNIQUE(c) (c).resize( unique( ALL(c) ) - (c).begin() )

#define sz size()
#define pb push_back
#define VI vector<int>
#define VS vector<string>
#define x first
#define y second

typedef long long LL;
typedef long double LD;
typedef pair<int,int> pii;

#define D(x) if(0) cout << __LINE__ <<" "<< #x " = " << (x) << endl;
#define D2(x,y) if(0) cout << __LINE__ <<" "<< #x " = " << (x) \
   <<", " << #y " = " << (y) << endl;

int iabs(int n) {
  if (n<0) return -n;
  return n;
}

int main() {
  int t;scanf("%d",&t);
  REP(__,t) {
    D(__);
    int n; scanf("%d",&n);
    D(n);
    int p1 = 1, p2 = 1;
    int t1 = 0, t2 = 0;
    int out = 0;
    REP (k, n) {
      int button;
      char which[10];
      scanf("%s %d", which, &button);
      D2(button, which);
      if(which[0] == 'B') {
        // player 2
        int d = iabs(p2 - button);
        int steps = d;
        int freemove = (out - t2);
        out += max(0, steps - freemove) + 1;
        t2 = out;
        p2 = button;
        D2(which, out);
      } else {
        // player 1
        int d = iabs(p1 - button);
        int steps = d;
        int freemove = (out - t1);
        out += max(0, steps - freemove) + 1;
        t1 = out; 
        p1 = button;
        D2(which, out);
      }
    }
    printf("Case #%d: %d\n",(__+1), out);
  }
  
  return 0;
}

