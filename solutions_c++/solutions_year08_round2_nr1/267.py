#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

const int INF = 1<<30;                
const double EPS = 1e-10;
const double PI = acos(-1.0);

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
typedef long double LD;

#define ALL(a) a.begin(),a.end()
#define PB push_back
#define MP make_pair
#define SZ(a) (int)a.size()
#define CLR(a,v) memset((a),(v),sizeof(a))
#define FOR(i,a,n) for(int i=(a);i<(n);++i)
#define FORD(i,a,n) for(int i=(a);i>=(n);--i)
#define REP(i,n) FOR(i,0,n) 


/// CODE HERE

LL X, Y;
LL A, B;
LL C, D;
LL M;
int n;

LL rem[3][3];

LL calc(LL n) {
  if (n < 2) return 0;
  return n*(n-1)*(n-2)/6;
}

int main() {
  freopen("A.in", "r", stdin);
  freopen("A.out", "w", stdout);

  int T;
  scanf("%d", &T);

  FOR(TN,1,T+1) {

    scanf("%d", &n);
    scanf("%I64d %I64d", &A, &B);
    scanf("%I64d %I64d", &C, &D);
    scanf("%I64d %I64d", &X, &Y);
    scanf("%I64d", &M);    
    CLR(rem, 0);
    rem[X%3][Y%3]++;
    FOR(i,1,n) {
      X = (X*A+B)%M;
      Y = (Y*C+D)%M;
      rem[X%3][Y%3]++;
    }       

    LL ans = 0;   

    REP(i,3) {
      REP(j,3)
        ans += calc(rem[i][j]);
      ans += rem[i][0]*rem[i][1]*rem[i][2];
    }      

    REP(i,3) REP(j,3) REP(k,3) {    
      if ((i+j+k)%3==0)
        ans += rem[0][i]*rem[1][j]*rem[2][k];
    }
 
    printf("Case #%d: %I64d\n", TN, ans);


  }


  return 0;
}