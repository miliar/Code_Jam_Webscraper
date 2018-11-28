#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>

#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <functional>
#include <map>
#include <set>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define pb push_back
#define mp make_pair

typedef unsigned long long ll;
typedef vector <int> vi;

const int maxn = 21;
const int maxx = 300;

int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};

int n, k;
char s[maxn][maxn];
int is[maxn][maxn][maxx * 2];
int len[maxn][maxn][maxx * 2];
string res[maxn][maxn][maxx * 2];

int aLen[maxx * 2];
string ans[maxx * 2];

struct state 
{
  int i, j, x;

  state() {}
  state( int a, int b, int c ) : i(a), j(b), x(c) {}
};

const int maxq = maxn * maxn * maxx * 2;

int qst, qen;
state q[maxq];

int Cor( int x ) 
{
  return 0 <= x && x < n;
}

void AddQ( int i, int j, int x, int fl, string fres )
{
  if (!is[i][j][x] || (len[i][j][x] == fl && res[i][j][x] > fres))
  {
    res[i][j][x] = fres;
    if (!is[i][j][x])
    {
      is[i][j][x] = 1;
      len[i][j][x] = fl;
      q[qen++] = state(i, j, x);
    }
  }
}

int main()
{
  int tn;
  scanf("%d", &tn);
  for (int tt = 1; tt <= tn; tt++)
  {
    fprintf(stderr, "tt=%d\n", tt);

    scanf("%d%d", &n, &k);
    forn(i, n)
      scanf("%s", s[i]);

    memset(is, 0, sizeof(is));
    qst = qen = 0;
    
    //puts("!");
    forn(i, n)
      forn(j, n)
        if (isdigit(s[i][j]))
          AddQ(i, j, s[i][j] - '0' + maxx, 0, string("") + s[i][j]);

    //puts("!");

    while (qst < qen)
    {
      state cur = q[qst++];

      forn(a, 4)
        forn(b, 4)
        {
          int x1 = cur.j + dx[a], y1 = cur.i + dy[a];
          int x2 = x1 + dx[b], y2 = y1 + dy[b];

          if (Cor(x1) && Cor(y1) && Cor(x2) && Cor(y2))
          {
            string str = res[cur.i][cur.j][cur.x] + s[y1][x1] + s[y2][x2];
            int newx = cur.x + (s[y2][x2] - '0') * (s[y1][x1] == '+' ? 1 : -1);

            if (!(0 <= newx && newx < maxx * 2))
              continue;            
            AddQ(y2, x2, newx, len[cur.i][cur.j][cur.x] + 1, str);
          }
        }     
    }

    //puts("!");

    memset(aLen, 0x10, sizeof(aLen));
    forn(i, n)
      forn(j, n)
        forn(x, 2 * maxx)
          if (is[i][j][x] && mp(len[i][j][x], res[i][j][x]) < mp(aLen[x], ans[x]))
            aLen[x] = len[i][j][x], ans[x] = res[i][j][x];
                                                                 
    //puts("!");

    printf("Case #%d:\n", tt);
    while (k--)
    {
      int x;
      scanf("%d", &x);
      printf("%s\n", ans[x + maxx].c_str());
    }
  }
  return 0;
}
