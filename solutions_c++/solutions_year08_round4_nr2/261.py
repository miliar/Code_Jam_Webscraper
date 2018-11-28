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

int n, m, a;
bool flag;

bool check( int dx1, int dy1, int dx2, int dy2 )
{
//  printf("%i %i %i %i\n", dx1, dy1, dx2, dy2);  
 // printf("%i %i\n", abs(dx1 * dy2 - dx2 * dy1), a);
  if (abs(dx1 * dy2 - dx2 * dy1) != a)
  {
 //   printf("kosyak\n");
    return false;
  }  
  if (abs(dx1) + abs(dy1) == 0)
    return false;
  if (abs(dx2) + abs(dy2) == 0)
    return false;    
  if (max(dx1, dx2) > n)
    return false;
    
  int u, v;
  u = min(dy1, dy2);
  u = min(0, u);
  v = max(dy1, dy2);
  v = max(v, 0);
  if ((v - u) > m)
    return false;
  
 // printf("good!\n");
  int x0, y0, x1, y1, x2, y2, x3, y3;
  
  x0 = 0;
  x1 = dx1;
  x2 = dx2;
  
  if (u < 0)
    y0 = -u;
  y1 = y0 + dy1;
  y2 = y0 + dy2;
  
  printf("%i %i %i %i %i %i", x0, y0, x1, y1, x2, y2);
  flag = true;
  return true;
  
}

int main()
{
  freopen("test.in", "r", stdin);
  freopen("test.out", "w", stdout);
  
  READ;
  foo >> tests;
  FOR(test,1,tests)
  {
    scanf("%i%i%i", &n, &m, &a);
    cout << "Case #" << test << ": ";    
    
    flag = false;
    FOR(dx1,0,n)
      FOR(dy1,-m,m)
        FOR(dx2,0,n)
        {
          int dy2;
          
          int P, Q;
          P = dx1;
          Q = dy1 * dx2;
          
          if (P == 0)
          {
            dy2 = 0;
            if (check(dx1, dy1, dx2, dy2))
              goto finish;
            continue;
          }
          if (abs(a + Q) % P == 0)
          {
            dy2 = (a + Q) / P;
            if (check(dx1, dy1, dx2, dy2))
              goto finish;
          }
          if (abs(Q - a) % P == 0)
          {
            dy2 = (Q - a) / P;
            if (check(dx1, dy1, dx2, dy2))
              goto finish;            
          }
        }
    printf("IMPOSSIBLE");
    finish:
    printf("\n");
  }

  return 0;
}
