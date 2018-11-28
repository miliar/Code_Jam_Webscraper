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

#define maxn 2110

int T, P, n;
int miss[maxn];

int price[15][maxn];
int f[15][15][maxn];

int solveit(int p, int chosen, int nowp) {
  int &ret = f[p][chosen][nowp];
  if (ret != -1) return ret;
  if (p == P) {
    if (P-chosen > miss[nowp]) ret = infinity; else ret = 0;
    return ret;
  }
  else {
    ret = infinity;
    //choice 1: do not choose this match
    int tans = solveit(p+1, chosen, nowp*2) + solveit(p+1, chosen, nowp*2+1);
    if (tans < ret) ret = tans;
    //choice 2: choose this match
    tans = solveit(p+1, chosen+1, nowp*2) + solveit(p+1, chosen+1, nowp*2+1) + price[p][nowp];
    if (tans < ret) ret = tans;
    return ret;
  }
}

int main() {
    
  freopen("B-large.in", "rt", stdin);
  freopen("B-large.out", "wt", stdout);
  
  scanf("%d", &T);
  for(int tn = 1; tn <= T; tn++) {
          
    scanf("%d", &P);
    n = 1<<P;
    for(int i = 0; i < n; i++)  scanf("%d", &miss[i]);
    memset(price,0,sizeof(price));
    int pn = 1;
    for(int i = P-1; i >= 0; i--)
      for(int j = 0; j < (1<<i); j++) 
        scanf("%d", &price[i][j]);
      
    for(int i = P; i >= 0; i--)
      for(int j = 0; j <= P; j++)
       for(int k = 0; k < n; k++)
         f[i][j][k] = -1;
    int ans = solveit(0, 0, 0);
    
   /* printf("f[1][1][0] = %d\n", f[1][1][0]);
    printf("f[2][1][0] = %d, f[2][1][1] = %d\n", f[2][1][0], f[2][1][1])*/
    
    printf("Case #%d: %d\n", tn, ans);
        
  }   
  
  return 0;
    
}
