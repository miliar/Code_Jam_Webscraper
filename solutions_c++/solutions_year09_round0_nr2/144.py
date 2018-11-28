#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <stack>
#include <bitset>
#include <complex>
#include <ctime>
#include <utility>
#include <numeric>
#include <functional>
using namespace std;

#define max2(a,b) (((a) > (b)) ? (a) : (b))
#define min2(a,b) (((a) < (b)) ? (a) : (b))
#define sqr(x) ((x) * (x))
#define debug(x) cout << (#x) << ": " << (x) << endl
#define echo(x) cout << (#x) << endl
#define SZ(x) (int(x.size()))

#define PB push_back
#define MP make_pair
#define FI first
#define SE second

const double eps = 1e-8;
const double pi = acos(-1.0);
const int oo = 0x7f7f7f7f;

typedef long long LL;

const int dx[4] = {-1, 0, 0, 1};
const int dy[4] = {0, -1, 1, 0};

int TN, TC;

int X, Y;
int hgt[100][100];
char label[100][100];

bool vis[100][100];
pair<int, int> sink[100][100];
map<pair<int, int>, char> index;

pair<int, int> calc_sink (int x, int y)
{
  if (vis[x][y])
    return sink[x][y];
  vis[x][y] = true;
  pair<int, int> &ret = sink[x][y];
  int op_hgt = oo, op_x = -1, op_y = -1;
  for (int d = 0; d < 4; ++d)
  {
    int x2 = x + dx[d], y2 = y + dy[d];
    if (x2 >= 0 && x2 < X && y2 >= 0 && y2 < Y)
      if (hgt[x2][y2] < op_hgt)
      {
        op_hgt = hgt[x2][y2];
        op_x = x2;
        op_y = y2;
      }
  }
  if (op_hgt < hgt[x][y])
    ret = calc_sink(op_x, op_y);
  else
    ret = MP(x, y);
  return ret;
}

int main ()
{
  scanf("%d", &TN);
  for (TC = 1; TC <= TN; ++TC)
  {
    scanf("%d%d", &X, &Y);
    for (int x = 0; x < X; ++x)
      for (int y = 0; y < Y; ++y)
        scanf("%d", &hgt[x][y]);
    memset(vis, false, sizeof(vis));
    index.clear();
    char lb = 'a';
    for (int x = 0; x < X; ++x)
      for (int y = 0; y < Y; ++y)
      {
        pair<int, int> sk = calc_sink(x, y);
        if (index.count(sk))
          label[x][y] = index[sk];
        else
          label[x][y] = index[sk] = lb++;
      }
    printf("Case #%d:\n", TC);
    for (int x = 0; x < X; ++x)
      for (int y = 0; y < Y; ++y)
        printf("%c%c", label[x][y], y < Y - 1 ? ' ' : '\n');
  }
}
