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

int A[1010];
LD d[1010];
LD c[1010][1010];
LL ans[1010];

int main()
{
/*
  d[1] = 0;
  d[2] = 1;

  FOR(n,3,1000) {
    d[n] = (n-1) * ( d[n-1] + d[n-2]);
    D(d[n]);
  }

  FOR(i,1,1000) {
    c[i][0] = c[i][i] = 1;
    FOR(j,1,i-1) {
      c[i][j] = c[i-1][j-1] + c[i-1][j];
    }
  }
*/

  ans[1] = 0;
  ans[2] = 2;
  FOR(i,3,1005) ans[i]=i;//holy crap?

  int t; scanf("%d",&t);
  REP(__,t) {
    int n; scanf("%d", &n);
    FOR(i,1,n) scanf("%d",&A[i]);
    double out=0;
    FOR (i,1,n) {
      if (A[i] != i) out++;
    }
    printf("Case #%d: %.8lf\n", __+1, out);
  }
  
  return 0;
}

