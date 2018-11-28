#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <vector>
#include <algorithm>

using namespace std;

#define PI 3.1415926535897932384626433832795
#define INF (int)1e9
#define EPS 1e-9

#define SQR(a) ((a)*(a))

#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define SORT(a) sort(a.begin(), a.end())
#define CLEAR(a) a.clear()
#define FILL(a) memset(a, 0, sizeof(a))
#define SIZE(a) (int)a.size()
#define LEN(a) (int)a.length()
#define SUBSTR(i,j) substr(i,j-i+1)
#define PB push_back
#define MP make_pair
#define VI vector<int>
#define VS vector<string>

stringstream foo("");
string buf;

#define READ getline(cin, buf), foo.clear(), foo.str(buf)

int tests;

#define N 256

#define MOD 10007

int n, m;
int t;
bool bad[N][N];
int dp[N][N];

bool good( int i, int j )
{
  return (i >= 0 && j >= 0 && i < n && j < m);
}

int main()
{
  freopen("test.in", "r", stdin);
  freopen("test.out", "w", stdout);
  
  READ;
  foo >> tests;
  FOR(test,1,tests)
  {
    scanf("%i%i%i", &n, &m, &t);
    FILL(bad);
    FOR(i,0,t-1)
    {
      int p, q;
      scanf("%i%i", &p, &q);
      bad[p - 1][q - 1] = true;
    }
    FILL(dp);
    dp[0][0] = 1;
    FOR(i,0,n-1)
      FOR(j,0,m-1)
      {
        if (good(i + 1, j + 2))
          if (!bad[i + 1][j + 2])
          {
            //printf("(%i, %i) -> (%i, %i)\n", i, j, i + 1, j + 2);
            dp[i + 1][j + 2] = (dp[i + 1][j + 2] + dp[i][j]) % MOD;
          }
        if (good(i + 2, j + 1))
          if (!bad[i + 2][j + 1])
          {
            //printf("(%i, %i) -> (%i, %i)\n", i, j, i + 2, j + 1);            
            dp[i + 2][j + 1] = (dp[i + 2][j + 1] + dp[i][j]) % MOD;
          }
      }
    cout << "Case #" << test << ": " << dp[n - 1][m - 1] << endl;
  }

  return 0;
}
