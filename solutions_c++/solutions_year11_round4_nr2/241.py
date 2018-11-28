/******************************************************************************

 @File Name : {PROJECT_DIR}/templ.cc

 @Creation Date : 07-05-2011

 @Last Modified : Fri 24 Jun 2011 11:26:59 PM CST

 @Created By: Zhai Yan

 @Purpose :
        template for gcj

*******************************************************************************/


#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>

using namespace std;

static int value[10][10];
static int d;
static int c;
static int r;
static int maxk = -1;

struct Point {
  int x;
  int y;
};

static bool ok(int i, int j, int size)
{
  int last = size * 2 - 2;
  if (i == 0 && j == 0 ||
      i == 0 && j == last ||
      i == last && j == 0 ||
      i == last && j == last)
    return false;
  return true;
}

static bool get_2res(int posx, int posy, int size, struct Point& res)
{
  int centerx = size - 1;
  int centery = size - 1;
  int i, j;
  res.x = 0;
  res.y = 0;
  for (i = 0; i < size; i++) {
    for (j = 0; j < size; j++) if (ok(i * 2, j * 2, size)) {
      res.x += (d + value[posx + i][posy + j]) * (i * 2 - centerx);
      res.y += (d + value[posx + i][posy + j]) * (j * 2 - centery);
    }
  }
  //fprintf(stderr, "%d %d\n", res.x, res.y);
  if (res.x == 0 && res.y == 0) {
    fprintf(stderr, "%d %d %d\n", posx, posy, size);
  }
  return res.x == 0 && res.y == 0;
}

static int search(int startx, int starty)
{
  for (int k = 3; k <= min(r,c); k++) {
    if (startx + k <= c && starty + k <= r) {
      struct Point res;
      //startx = 1;starty = 1; k = 5;
      if (get_2res(startx, starty, k, res)) {
        maxk = max(k, maxk);
      }
    }
  }
}

static void solve(int t)
{
  maxk = -1;
  scanf("%d%d%d", &r, &c, &d);
  fprintf(stderr, "%d", d);
  getchar();
  for (int i = 0; i < r; i++) {
    for (int j = 0; j < c; j++) {
      char tmp;
      scanf("%c", &tmp);
      value[i][j] = tmp - '0';
   //   putchar(tmp);
    }
    getchar();
  //  putchar('\n');
  }
  fprintf(stderr, "%d", d);
  for (int i = 0; i < c; i++) {
    for (int j = 0; j < r; j++) {
      search(i, j);
    }
  }

  if (maxk == -1) printf("IMPOSSIBLE");
  else printf("%d", maxk);
}


int main()
{
  int T;
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    printf("Case #%d: ", i + 1);
    solve(i + 1);
    printf("\n", i + 1);
  }
  return 0;
}





