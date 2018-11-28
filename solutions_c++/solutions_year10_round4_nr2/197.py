#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int _a;

#define FOR(i , n) for(int i = 0 ; i < n ; i++)
#define FOT(i , a , b) for(int i = a ; i < b ; i++)
#define GETINT (scanf("%d" , &_a) , _a)
#define pb push_back
#define mp make_pair
#define s(a) (int(a.size()))
#define PRINT(a) cerr << #a << " = " << a << endl
#define ALL(a) (a).begin(), (a).end()

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int , int> PII;

int teams, c[1024];
int cost[2048];

ll best[2048][11];

//leaves = teams - 1 to teams + teams - 1


ll find(int match, int missed) {
  if(best[match][missed] != -1) return best[match][missed];
  ll& ans = best[match][missed];
  ans = 0;
  ans = min(find(2*match+1,missed)+find(2*match+2,missed)+cost[match],
            find(2*match+1,missed+1)+find(2*match+2,missed+1));
  return ans;
}

int main() {
  int T;
  T = GETINT;

  FOR(test, T) {
    int p;
    
    p = GETINT;
    teams = (1 << p);

    FOR(i, teams) c[teams-1-i] = GETINT;
    for(int i = teams - 2; i >= 0; i--) cost[i] = GETINT;

    FOR(i, 2*teams) FOR(j, 11) best[i][j] = -1;

    for(int i = 0; i < teams; i++)
      for(int j = 0; j < 11; j++)
        best[teams-1+i][j] = (j <= c[i] ? 0LL : 12345678901234LL);
    
    printf("Case #%d: %Ld\n", 1+test, find(0, 0));
  }
  return 0;
}
