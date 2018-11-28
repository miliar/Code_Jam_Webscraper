#include <vector>
#include <list>
#include <map>
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

const int N = 2005;

int set[N];
int rank[N];

int set_find(int x)
{
  if (set[x] != x) set[x] = set_find(set[x]);
  return set[x];  
}
void set_union(int x, int y)
{
  x = set_find(x);
  y = set_find(y);
  if (rank[x] > rank[y])
    set[y] = x;
  else
  {
    set[x] = y;
    if (rank[x] == rank[y]) ++rank[y];
  }
}

int A, B, P;

bool prime[N];
int p[N];
int n;




int main() {
  freopen("B.in", "r", stdin);
  freopen("B.out", "w", stdout);

  CLR(prime,1);
  for (int i = 2; i*i<N;++i) {
    if (!prime[i]) continue;
    for (int j = i*i; j < N; j+=i)
      prime[j] = false;
  }
  n = 0;
  for (int i = 2; i < N; ++i)
    if (prime[i]) p[n++] = i;

  int T;
  scanf("%d", &T);

  FOR(TN,1,T+1) {

    scanf("%d %d %d", &A, &B, &P);

    FOR(i,A,B+1) {
      set[i] = i;
      rank[i] = 0;
    }




    int from = 0;
    for (; from < n; ++from) {
      if (p[from] >= P) break;
    }

    
    
    FOR(j,from,n) {
      FOR(k,A,B+1) FOR(l,k+1,B+1) {
        if (set_find(k) == set_find(l)) continue;
        if (k % p[j] == 0 && l % p[j] == 0) 
          set_union(k, l);
      }
    }

    int ans = 0;
    FOR(j,A,B+1)
      if (set_find(j) == j) ++ans;
    



    printf("Case #%d: %d\n", TN, ans);

  }


  return 0;
}