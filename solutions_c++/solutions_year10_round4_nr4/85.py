
#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

int n, m;

int x[5000], y[5000];
int cx[1000], cy[1000];

long double area(int q)
{
  long double d = sqrt((x[0]-x[1])*(x[0]-x[1]) + (y[0]-y[1])*(y[0]-y[1]));
  long double r0 = sqrt((x[0]-cx[q])*(x[0]-cx[q]) + (y[0]-cy[q])*(y[0]-cy[q]));
  long double r1 = sqrt((x[1]-cx[q])*(x[1]-cx[q]) + (y[1]-cy[q])*(y[1]-cy[q]));

  return r0*r0*acos((d*d + r0*r0 - r1*r1)/(2*d*r0))
       + r1*r1*acos((d*d + r1*r1 - r0*r0)/(2*d*r1))
       - 0.5*sqrt((-d + r0 + r1)*(d + r0 - r1)*(d - r0 + r1)*(d + r0 + r1));
}

void solve(int CASE)
{
  cin >> n >> m;

  for (int i = 0; i < n; i++)
    cin >> x[i] >> y[i];

  for (int i = 0; i < m; i++)
    cin >> cx[i] >> cy[i];

  printf("Case #%d:", CASE);
  for (int i = 0; i < m; i++)
    printf(" %.7llf", fabsl(area(i)));

  puts("");
}

int main()
{
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) solve(i+1);
  return 0;
}
