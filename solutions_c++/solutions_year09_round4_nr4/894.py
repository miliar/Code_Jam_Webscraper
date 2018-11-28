#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

struct circle {
 int x, y, r;
};

int N;

circle inp[41];

double dist(int x1, int y1, int x2, int y2)
{
 return sqrt( (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
}

double solve()
{
 if (N == 1)
  return inp[0].r;
  
 if (N == 2)
  return max(inp[0].r, inp[1].r);
 
 double ans = 10000000000000.;
 
 double case1 = dist(inp[0].x, inp[0].y, inp[1].x, inp[1].y);
 case1 += inp[0].r + inp[1].r;
 case1 /= 2.; 
 case1 >?= inp[2].r;
 
 double case2 = dist(inp[0].x, inp[0].y, inp[2].x, inp[2].y);
 case2 += inp[0].r + inp[2].r;
 case2 /= 2.;
 case2 >?= inp[1].r;
 
 double case3 = dist(inp[1].x, inp[1].y, inp[2].x, inp[2].y);
 case3 += inp[1].r + inp[2].r;
 case3 /= 2.;
 case3 >?= inp[0].r;
 
 ans <?= case1;
 ans <?= case2;
 ans <?= case3;
 
 return ans; 
}

int main()
{
 int T;
 scanf("%d", &T);
 
 for (int t = 0; t < T; t++)
 {
  scanf("%d", &N);
  for (int i = 0; i < N; i++)
   scanf("%d %d %d", &inp[i].x, &inp[i].y, &inp[i].r);
  printf("Case #%d: %.8lf\n", t + 1, solve());
 }
 
 return 0;
}
