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

#define N (6001*6001)
#define W 7000

int n;
int d;
int x[N], y[N];
int max_x[W], max_y[W], min_x[W], min_y[W];

inline int di( int d )
{
  if (d == 1)
    return -1;
  if (d == 3)
    return +1;
  return 0;
}
inline int dj( int d )
{
  if (d == 0)
    return +1;
  if (d == 2)
    return -1;
  return 0;
}

void go( string str, int k )
{
  FOR(i,0,k-1)
  {
    FOR(j,0,LEN(str)-1)
    {
      if (str[j] == 'F')
      {
        x[n] = x[n - 1] + di(d);
        y[n] = y[n - 1] + dj(d);
        n++;
      }
      else
      if (str[j] == 'L')
        d = (d + 1) % 4;
      else
      if (str[j] == 'R')
      {
        d = d - 1;
        if (d < 0)
          d = 4 + d;
      }
    }
  }
}

int main()
{
  freopen("test.in", "r", stdin);
  freopen("test.out", "w", stdout);
  
  READ;
  foo >> tests;
  FOR(test,1,tests)
  {
    int l;
    scanf("%i\n", &l);
    n = 1;
    d = 0;
    x[0] = 3000;
    y[0] = 3000;
    FOR(i,0,l-1)
    {
      string str;
      int k;
      cin >> str >> k;
      //cout << str << ", " << k << endl;
      go(str, k);
    }
    //x[n] = x[0];
    //y[n] = y[0];    
    
    FOR(i,0,n-2)
    {
      //printf("(%i, %i)\n", x[i], y[i]);
    }
   // printf("%i\n", n);
    
    long long area = 0;
    FOR(i,0,n-2)
      area = area + (x[i] + x[i + 1]) * (y[i] - y[i + 1]);
    area = abs(area);
    area /= 2;
    //cout << "S = " << area << endl;
    
    FOR(i,0,W)
    {
      min_x[i] = min_y[i] = W + 1;
      max_x[i] = max_y[i] = -1;
    }
    FOR(i,0,n-2)
    {
      if (y[i] == y[i + 1])
      {
        int _x = min(x[i], x[i + 1]);
        min_y[_x] = min(min_y[_x], y[i]);
        max_y[_x] = max(max_y[_x], y[i]);        
      }
      if (x[i] == x[i + 1])
      {
        int _y = min(y[i], y[i + 1]);
        min_x[_y] = min(min_x[_y], x[i]);
        max_x[_y] = max(max_x[_y], x[i]);
      }
    }
    
    long long ans = 0;
    FOR(i,0,W)
    {
      if (min_x[i] < max_x[i])
      {
        //printf("add horizontal line with y = %i [%i, %i]\n", i, min_x[i], max_x[i]); 
        ans += (max_x[i] - min_x[i]);
        //printf(" + %i\n", (max_x[i] - min_x[i]));
      }
      if (min_y[i] < max_y[i])
      {
        //printf("add vertical line with x = %i [%i, %i]\n", i, min_y[i], max_y[i]);         
        ans += (max_y[i] - min_y[i]);
        //printf(" + %i\n", (max_y[i] - min_y[i]));        
      }
    }
    //cout << "asn = " << ans << endl;
    
    FOR(i,0,W)
      if (min_x[i] < max_x[i])
        FOR(j,0,W)
          if (min_y[j] < max_y[j])
          {
            if (i >= min_y[j] && i + 1 <= max_y[j])
              if (j >= min_x[i] && j +1  <= max_x[i])
              {
                //printf("intersect (%i, %i)\n", j, i); 
                ans -= 1;
              }
          }
    
    ans -= area;
    
    cout << "Case #" << test << ": " << ans << endl;
  }

  return 0;
}
