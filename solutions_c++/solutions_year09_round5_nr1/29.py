#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <sstream>
#include <cassert>
#include <ctime>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ext/hash_map>
#include <ext/hash_set>

#define eps 1e-9

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define forit(i, s) for(__typeof(s.begin()) i = s.begin(); i != s.end(); i++)
#define sz(v)((v).size())

#define fi first
#define se second
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef unsigned long long ull;
typedef double dbl;
typedef long double ldbl;

using namespace std;

using namespace __gnu_cxx;

#define maxn 15

ll mul = 999983;
ll code[maxn][maxn];
char a[maxn][maxn];

set <ll> was;


#define maxq 10000010
ll q[maxq], l, r, qd[maxq], qpx[maxq][5], qpy[maxq][5], curx[5], cury[5], cn, tmpx[5], tmpy[5];


void putP()
{
  for (int i = 0; i < cn; i++)
    a[cury[i]][curx[i]] = '!';
}
void removeP()
{
  for (int i = 0; i < cn; i++)
    a[cury[i]][curx[i]] = '.';
}

void add( ll c, int d )
{
  if (was.count(c)) return;
  was.insert(c);

  q[r] = c;
  qd[r] = d;

  for (int i = 0; i < cn; i++)
  {
    qpx[r][i] = curx[i];
    qpy[r][i] = cury[i];
  }
  r++;
  assert(r < maxq);
}

int dx[] = {-1, 1, 0, 0},
    dy[] = {0, 0, 1, -1}, _w[maxn][maxn], h, w;

int dfs( int y, int x )
{
  int res = 1;
  _w[y][x] = 1;
  for (int i = 0; i < 4; i++)
    if (!_w[y + dy[i]][x + dx[i]] && a[y + dy[i]][x + dx[i]] == '!')
      res += dfs(y + dy[i], x + dx[i]);
  return res;
}

bool isConnected()
{
  int cnt = dfs(cury[0], curx[0]);
  for (int i = 0; i < cn; i++)
    _w[cury[i]][curx[i]] = 0;
  return cnt == cn;
}

void out()
{
  for (int i = 1; i <= h; i++)
  {
    for (int j = 1; j <= w; j++)
      putc(a[i][j], stdout);
    puts("");
  }
}

int main( void )
{
  int tn;
  scanf("%d", &tn);

  for (int tt = 1; tt <= tn; tt++)
  {
    printf("Case #%d: ", tt);

    memset(a, '#', sizeof(a));

    scanf("%d%d", &h, &w);

    for (int i = 1; i <= h; i++)
     scanf("%s", a[i] + 1), a[i][w + 1] = '#';

    ll prev = 1;
    for (int i = 1; i <= h; i++)
      for (int j = 1; j <= w; j++)
        code[i][j] = prev, prev *= mul;

    ll st = 0, en = 0;

    cn = 0;

    for (int i = 1; i <= h; i++)
      for (int j = 1; j <= w; j++)
      {
        if (a[i][j] == 'o' || a[i][j] == 'w')
        {
          cury[cn] = i;
          curx[cn++] = j;
          st += code[i][j];

        }
        if (a[i][j] == 'x' || a[i][j] == 'w')
          en += code[i][j];
      }

    was.clear();
    l = r = 0;
    add(st, 0);
    for (int i = 1; i <= h; i++)
      for (int j = 1; j <= w; j++)
        if (a[i][j] != '#')
          a[i][j] = '.';
    ll res = -1;
    while (l < r)
    {
    //  fprintf(stdout, "!!!\n");
      int cd = qd[l];
      ll curr = q[l];

      for (int i = 0; i < cn; i++)
      {
        curx[i] = qpx[l][i];
        cury[i] = qpy[l][i];
      }
      l++;


      if (curr == en)
      {
        res = cd;
        break;
      }

      putP();

  //    out();
      bool ok = isConnected();
      for (int i = 0; i < cn; i++)
        for (int j = 0; j < 4; j++)
          if (a[cury[i] - dy[j]][curx[i] - dx[j]] == '.' && a[cury[i] + dy[j]][curx[i] + dx[j]] == '.')
          {
            ll ncode = curr - code[cury[i]][curx[i]] + code[cury[i] + dy[j]][curx[i] + dx[j]];

            a[cury[i] + dy[j]][curx[i] + dx[j]] = '!';
            a[cury[i]][curx[i]] = '.';
            cury[i] += dy[j];
            curx[i] += dx[j];

//            out();
            if (ok || isConnected())
              add(ncode, cd + 1);

            cury[i] -= dy[j];
            curx[i] -= dx[j];
            a[cury[i] + dy[j]][curx[i] + dx[j]] = '.';
            a[cury[i]][curx[i]] = '!';
          }
        
      
      removeP();
    }

    cout << res << endl;
  }

  return 0;
}