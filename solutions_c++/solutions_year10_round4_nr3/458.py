#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <cmath>
#include <cassert>
using namespace std;
#define psb push_back
#define mpr make_pair
#define infinity 1000000010
#define mineps 1e-8
#define sqr(x) ((x)*(x))
#define MIN(x,y) ((x)<(y)?(x):(y))
#define MAX(x,y) ((x)>(y)?(x):(y))
#define LL long long
#define UC unsigned long
#define UI unsigned int
#define pi 3.14159265358979323846 
inline int cmp(double x) {
  if (fabs(x) < mineps) return 0;
  else if (x < 0) return -1;
  else return 1;       
}
//////////////////////////////////////////////
//Start here

#define maxn 310
const int axis = 152;

int T, n;
int countit;

bool a[maxn][maxn], ta[maxn][maxn];
int rounds;

inline bool emptymap() {
  for(int i = 0; i < maxn; i++)
    for(int j = 0; j < maxn; j++)
      if (a[i][j]) return false;
  return true;       
}

void doit() {
     
  memcpy(ta, a, sizeof(ta));
  for(int i = 0; i < maxn; i++)
    for(int j = 0; j < maxn; j++) 
      if (ta[i][j]) {
        int i1 = i-1, j1 = j, i2 = i, j2 = j-1;
        if (i1 >= 0 && j2 >= 0 && !ta[i1][j1] && !ta[i2][j2]) a[i][j] = false;
      }
      else if (!ta[i][j]) {
        int i1 = i-1, j1 = j, i2 = i, j2 = j-1;
        if (i1 >= 0 && j2 >= 0 && ta[i1][j1] && ta[i2][j2]) a[i][j] = true;     
      }
     
}

int main() {
    
  freopen("C-small.in", "rt", stdin);
  freopen("C-small.out", "wt", stdout); 
  
  scanf("%d", &T);
  for(int tn = 1; tn <= T; tn++) {
          
    memset(a,0,sizeof(a));
    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
      int x1, y1, x2, y2;
      scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
      x1 += axis; y1 += axis; x2 += axis; y2 += axis;
      swap(x1, y1); swap(x2, y2);
      for(int j = x1; j <= x2; j++)
        for(int k = y1; k <= y2; k++)
          a[j][k] = true;        
    }
    
    rounds = 0;
    while (!emptymap()) {
      doit();
      rounds ++;      
    }        
    
    printf("Case #%d: %d\n", tn, rounds);
          
  }  
  
  return 0;
    
}
