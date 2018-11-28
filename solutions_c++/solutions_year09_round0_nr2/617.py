#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cassert>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define DEBUG(format, args...) do { fprintf(stderr, format, ## args); fflush(stderr); } while (0)
#define PRINT(format, args...) do { fprintf(stdout, format, ## args); DEBUG(format, ## args); } while (0)

#define SIZE(__c) (int)(__c).size()
#define FOREACH(__i, __c) for (typeof(__c.begin()) __i=__c.begin(); __i!=__c.end(); ++__i)

typedef signed long long int i64;

const int INF=INT_MAX/2;

const int DY[]={-1, 0, 0, 1};
const int DX[]={0, -1, 1, 0};

int Y, X;
int al[108][108];
char lb[108][108];
char c;

bool inBounds(int y, int x);
char recurse(int y, int x);

int main() {
  int i, j, t, T;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    scanf("%d %d", &Y, &X);
    for (i=0; i<Y; i++)
      for (j=0; j<X; j++) {
        lb[i][j]=0;
        scanf("%d", &al[i][j]);
      }
    c='a';
    for (i=0; i<Y; i++)
      for (j=0; j<X; j++)
        if (lb[i][j]==0)
          recurse(i, j);
    PRINT("Case #%d:\n", t);
    for (i=0; i<Y; i++) {
      PRINT("%c", lb[i][0]);
      for (j=1; j<X; j++)
        PRINT(" %c", lb[i][j]);
      PRINT("\n");
    }
  }
  return 0;
}

bool inBounds(int y, int x) {
  return y>=0 && x<X && y<Y && x>=0;
}

char recurse(int y, int x) {
  if (lb[y][x]!=0)
    return lb[y][x];
  int i, ny, nx, a=INF;
  for (i=0; i<4; i++)
    if (inBounds(y+DY[i], x+DX[i]))
      a=min(a, al[y+DY[i]][x+DX[i]]);
  if (a>=al[y][x])
    return lb[y][x]=c++;
  for (i=0; i<4; i++) {
    ny=y+DY[i];
    nx=x+DX[i];
    if (inBounds(ny, nx))
      if (al[ny][nx]==a)
        return lb[y][x]=recurse(ny, nx);
  }
  assert(0);
}
