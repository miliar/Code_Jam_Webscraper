#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>


using namespace std;

#define FOR(i , n) for(int i = 0 ; i < n ; i++)
#define FOT(i , a , b) for(int i = a ; i < b ; i++)
int _a;
#define GETINT (scanf("%d" , &_a) , _a)
#define pb push_back
#define mp make_pair
#define s(a) (int(a.size()))
#define PRINT(a) cerr << #a << " = " << a << endl
#define ALL(a) a.begin(), a.end()


typedef long long ll;
typedef pair< ll , ll > PLL;
typedef vector< PLL > vpll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int , int> PII;
typedef vector< PII > vpii;


int main()
{
  int best[31][2];
  FOR(i, 31) FOR(j, 2) best[i][j] = 0;
  FOR(i, 11) FOT(j, i, i + 3) FOT(k, j, i + 3) {
    int s = (k == ( i + 2));
    best[i+j+k][s] = max(best[i+j+k][s], k);
  }

  int tests = GETINT;
  for(int t = 1; t <= tests; t++) {
    int N = GETINT;
    int S = GETINT;
    int P = GETINT;
    int ans[101][101];
    FOR(i, 101) FOR(j, 101) ans[i][j] = -123456;
    ans[0][0] = 0;
    FOT(i, 1, N + 1) {
      int num = GETINT;
      FOR(s, 2) {
	int b = best[num][s];
	FOT(t, s, S + 1) {
	  ans[i][t] = max(ans[i][t], ans[i-1][t - s] + (b >= P));
	}
      }
    }
    printf("Case #%d: %d\n", t, max(0, ans[N][S]));
  }
  return 0;
}
