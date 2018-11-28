#include <iostream>
#include <cmath>

using namespace std;

int x[6], y[6], r[6];

double CalcRadius(int i, int j)
{
  int minr = min(r[i], r[j]), maxr = max(r[i], r[j]);
  double dist = sqrt( (x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]) );
  if (dist + minr < maxr) return (double) maxr;
  else return (dist + maxr + minr) / 2.0;
}

double Solve()
{
  int n;
  scanf("%d", &n);
  for (int i = 0; i < n; i++)
    scanf("%d %d %d", &x[i], &y[i], &r[i]);
  
  if (n == 1) return (double) r[0];
  if (n == 2) return (double) max(r[0], r[1]);
  
  double minn = 1e100;
  
  // 1 & 2 + 3
  double rr = CalcRadius(0, 1);
  double tmp = max(rr,(double) r[2]); 
  minn = min(minn, tmp);
  
  // 1 & 3 + 2
  rr = CalcRadius(0, 2);
  tmp = max(rr, (double) r[1]);
  minn = min(minn, tmp);
  
  // 2 & 3 + 1
  rr = CalcRadius(1, 2);
  tmp = max(rr, (double) r[0]);
  minn = min(minn, tmp);
  
  return minn;
}

int main()
{
  int tests;
  scanf("%d", &tests);
  for (int i = 1; i <= tests; i++)
    {
      double res = Solve();
      printf("Case #%d: %.6f\n", i, res);
    }
    
  //system("pause");
  return 0;
}
