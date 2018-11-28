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

int T, N, K;

int main() {
    
  freopen("A-large.in", "rt", stdin);
  freopen("A-large.out", "wt", stdout);
  
  scanf("%d", &T);
  for(int tn = 1; tn <= T; tn++) {
          
    scanf("%d %d", &N, &K);
    printf("Case #%d: ", tn);
    int form = (1<<N) - 1;
    if ((K&form) == form) puts("ON"); else puts("OFF");    
          
  }   
  
  return 0;
    
}
