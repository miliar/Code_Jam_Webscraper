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

#define N 2000

int n;
int a, b, p;
int num[N];
bool g[N][N];
bool mark[N];
VI ps[N];

bool check( int i, int j )
{
  FOR(k,0,SIZE(ps[i])-1)
    FOR(l,0,SIZE(ps[j])-1)
      if (ps[i][k] == ps[j][l])
        if (ps[i][k] >= p)
          return true;
  return false;
}
void dfs( int i )
{
  mark[i] = true;
  FOR(j,0,n-1)
    if (g[i][j])
      if (!mark[j])
        dfs(j);
}

int main()
{
  freopen("test.in", "r", stdin);
  freopen("test.out", "w", stdout);
  
  READ;
  foo >> tests;
  FOR(test,1,tests)
  {
    cin >> a >> b >> p;
    n = 0;
    FOR(i,a,b)
      num[n++] = i;
    FOR(i,0,n-1)
    {
      CLEAR(ps[i]);
      int tmp = num[i];
      for (int d = 2; d * d <= tmp; d++)
      {
        if (tmp % d == 0)
        {
          ps[i].PB(d);
          while (tmp % d == 0)
            tmp /= d;
        }
      }
      if (tmp > 1)
        ps[i].PB(tmp);
    }
    FILL(g);
    FOR(i,0,n-1)
      FOR(j,i+1,n-1)
        g[i][j] = g[j][i] = check(i, j);
    FILL(mark);
    int result = 0;
    FOR(i,0,n-1)
      if (!mark[i])
      {
        result++;
        dfs(i);
      }
    cout << "Case #" << test << ": " << result << endl;
  }

  return 0;
}
