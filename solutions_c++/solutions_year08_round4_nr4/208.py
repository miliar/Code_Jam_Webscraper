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
const double EPS = 1e-9;
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

const int N = 10005;

char s[N];
char t[N];
int k, n;

int calc() {
  int ret = INF;
  VI p(k);
  REP(i,k) p[i]=i;
  do {
    int m = n/k;
    REP(start, m) {
      REP(i,k) {
        t[start*k+i] = s[start*k+p[i]];
      }
    }
    int cur = 1;
    FOR(i,1,n) if (t[i-1]!=t[i]) ++cur;
    ret = min(ret, cur);
  } while(next_permutation(ALL(p)));
  return ret;
}

int main() {
  freopen("D.in", "r", stdin);
  freopen("D.out", "w", stdout);

  int T;
  scanf("%d", &T);

  FOR(NT,1,T+1) {
    scanf("%d", &k);
    getchar();
    gets(s);
    n = strlen(s);
    int ans = calc();
    printf("Case #%d: %d\n", NT, ans);

    
  }


  return 0;
}