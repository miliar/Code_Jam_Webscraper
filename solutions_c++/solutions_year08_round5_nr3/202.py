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

#define N 11

int n, m;
char board[N][N];
long long dp[N][1 << N];

int count( int pos )
{
  if (!pos)
    return 0;
  else
    return (count(pos / 2) + pos % 2);
}
bool get_bit( int mask, int p )
{
  return ((mask >> p) & 1);
}
int put_bit( int mask, int p )
{
  return (mask | (1 << p));
}
bool match( int mask, int pos, int k )
{
  FOR(j,0,m-1)
    if (get_bit(pos, j))
    {
      if (j - 1 >= 0)
        if (get_bit(pos, j - 1))
          return false;
      if (j + 1 < m)
        if (get_bit(pos, j + 1))
          return false;
    }
  FOR(j,0,m-1)
    if (get_bit(pos, j))
    {
      if (get_bit(mask, j))
        return false;
      if (board[k][j] == 'x')
        return false;
    }
  return true;
}
int get_mask( int pos )
{
  int mask = 0;
  FOR(j,0,m-1)
    if (get_bit(pos, j))
    {
      if (j - 1 >= 0)
        mask = put_bit(mask, j - 1);
      if (j + 1 < m)
        mask = put_bit(mask, j + 1);
    }
  return mask;
}

int main()
{
  freopen("test.in", "r", stdin);
  freopen("test.out", "w", stdout);
  
  READ;
  foo >> tests;
  FOR(test,1,tests)
  {
    scanf("%i%i\n", &n, &m);
    FOR(i,0,n-1)
    {
      FOR(j,0,m-1)
        scanf("%c", &board[i][j]);
      scanf("\n");
    }
    FILL(dp);
    dp[0][0] = 0;
    FOR(i,0,n-1)
    {
      FOR(mask,0,(1<<m)-1)
        {
          FOR(pos,0,(1<<m)-1)
            if (match(mask, pos, i))
            {
              //printf("%i -> %i\n", mask, pos);
              int next_mask = get_mask(pos);
              dp[i + 1][next_mask] = max(dp[i + 1][next_mask], dp[i][mask] + count(pos));
            }
        }
    }
    long long ans = 0;
    FOR(mask,0,(1<<m)-1)
      ans = max(ans, dp[n][mask]);
        
    cout << "Case #" << test << ": " << ans << endl;
  }

  return 0;
}
