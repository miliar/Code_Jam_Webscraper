#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>

int loop,m,n,a;

using namespace std; typedef unsigned long ulong; typedef long long llong;

inline int area(int x1,int x2,int x3,int y1,int y2,int y3)
{
  return(abs(x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3));
}

int doit()
{
  for(int i1=0;i1<1;i1++) for(int i2=n;i2<=n;i2++) for(int i3=0;i3<=n;i3++)
  for(int j1=0;j1<=m/2;j1++) for(int j2=0;j2<=m;j2++) for(int j3=0;j3<=m;j3++)
  if (area(i1,i2,i3,j1,j2,j3) == a) { printf("Case #%d: %d %d %d %d %d %d\n",loop,i1,j1,i2,j2,i3,j3); return 1; }
  return 0;
}

int main()
{
int cases;

cin >> cases;

for(loop=1;loop<=cases;loop++)
{
  set<int> A;
  cin >> n>>m>>a;

  if (a>m*n) { printf("Case #%d: IMPOSSIBLE\n",loop); continue; }
  while(m*n>=a) m--; m++;

  doit();
}

}
