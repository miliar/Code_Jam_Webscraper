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

#define D(x) if(1) cout << __LINE__ <<" "<< #x " = " << (x) << endl;
#define D2(x,y) if(1) cout << __LINE__ <<" "<< #x " = " << (x) \
   <<", " << #y " = " << (y) << endl;

int main()
{
  int t;scanf("%d",&t);
  REP (__,t) {
    int n; scanf("%d",&n);
    int small = 0;
    int sum = 0;
    int xo = 0;
    REP(i,n) {
      int a; scanf("%d",&a);
      if(i == 0 || a < small) {
        small = a;
      }
      xo ^= a;
      sum += a;
    }
    if(xo) {
      printf("Case #%d: NO\n", (__+1));
    } else {
      printf("Case #%d: %d\n", (__+1), sum-small);
    }
  }
  
  return 0;
}

