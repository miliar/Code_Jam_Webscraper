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

#define N 200000 

int n;
long long A, B, C, D, M;
long long x[N], y[N];
long long t[N][4][3][3];

int main()
{
  freopen("test.in", "r", stdin);
  freopen("test.out", "w", stdout);
  
  READ;
  foo >> tests;
  FOR(test,1,tests)
  {
    cin >> n >> A >> B >> C >> D >> x[0] >> y[0] >> M;
    FOR(i,1,n-1)
    {
      x[i] = (A * x[i - 1] + B) % M;
      y[i] = (C * y[i - 1] + D) % M;
    //  cout << x[i] << "," << y[i] << endl;
    }
    FILL(t);
    long long cnt = 0;
    FOR(i,0,n-1)
      t[i][1][x[i] % 3][y[i] % 3] = 1;
    FOR(i,0,n-2)
      FOR(j,1,3)
        FOR(p,0,2)
          FOR(q,0,2)
          {
            t[i + 1][j][p][q] += t[i][j][p][q];
            if (j < 3)
            {
              int _p, _q;
              _p = (p + x[i + 1]) % 3;
              _q = (q + y[i + 1]) % 3;
              t[i + 1][j + 1][_p][_q] += t[i][j][p][q];
            }
          }
    cout << "Case #" << test << ": " << t[n - 1][3][0][0] << endl;
  }

  return 0;
}
