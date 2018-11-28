#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <cstdlib>

using namespace std;

#define pb push_back
#define all(x) x.begin(), x.end()
#define mp make_pair
#define x first
#define y second

typedef pair <int, int> pii;
typedef vector <int> vi;
typedef long long int64;
typedef set < int > si;

const int inf = (1 << 30) - 1;

int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

int operator * (pii a, pii b)
{
  return a.x * b.y - a.y * b.x;
}

string s;
bool u[7000][7000][4];
bool us[7000][7000];
vector <pii> a;

int main ()
{
  freopen ("input.txt", "r", stdin);
  freopen ("output.txt", "w", stdout);
  int nn;
  cin >> nn;
  for (int ii = 1; ii <= nn; ii ++)
    {
      a.clear ();
      memset (u, 0, sizeof (u));
      int minx, maxx, miny, maxy;
      minx = 3500;
      maxx = 3500;
      miny = 3500;
      maxy = 3500;
      int x = 3500;
      int y = 3500;
      int d = 0;
      a.pb (mp (x, y));
      int l;
      cin >> l;
      for (int i = 0; i < l; i ++)
        {
          int tm;
          cin >> s >> tm;
          for (int j = 0; j < tm; j ++)
            {
              for (int k = 0; k < s.length(); k ++)
                if (s[k] == 'F')
                  {
                    x += dx[d];
                    y += dy[d];
                    a.pb (mp (x, y));
                    u[x][y][0] = true;
                    u[x][y][1] = true;
                    u[x][y][2] = true;
                    u[x][y][3] = true;
                    minx = min (minx, x);
                    miny = min (miny, y);
                    maxx = max (maxx, x);
                    maxy = max (maxy, y);
                  }
                 else
                if (s[k] == 'R')
                  d = (d + 4 + 1) & 3;
                 else
                  d = (d + 4 - 1) & 3;
            }
        }
      int s = 0;
      for (int i = 0; i < a.size() - 1; i ++)
        s -= a[i] * a[i+1];
      s = - abs (s);
      s /= 2;
      for (int i = minx; i <= maxx; i ++)
        {
          for (int j = miny; j <= maxy; j ++)
            u[i][j][0] |= u[i][j-1][0];
    
          for (int j = maxy; j >= miny; j --)
            u[i][j][1] |= u[i][j+1][1];
        }
      for (int j = miny; j <= maxy; j ++)
        {
          for (int i = minx; i <= maxx; i ++)
            u[i][j][2] |= u[i-1][j][2];
          
          for (int i = maxx; i >= minx; i --)
            u[i][j][3] |= u[i+1][j][3];
        }
      memset (us, 0, sizeof (us));
      for (int i = minx; i <= maxx; i ++)
        for (int j = miny; j <= maxy; j ++)
          us[i][j] = (u[i][j][0] & u[i][j][1]) | (u[i][j][2] & u[i][j][3]);
      for (int i = minx; i <= maxx; i ++)
        for (int j = miny; j <= maxy; j ++)
          if (us[i][j] & us[i+1][j] & us[i][j+1] & us[i+1][j+1])
            s ++;
      printf ("Case #%d: %d\n", ii, s);
    }
}
