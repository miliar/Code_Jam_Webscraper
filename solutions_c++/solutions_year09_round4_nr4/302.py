
#include <cmath>
#include <iostream>
using namespace std;

struct plant { int x, y, r; };

plant p[50];

double cover(int i, int j)
{
  int dx = p[i].x - p[j].x;
  int dy = p[i].y - p[j].y;
  double d = sqrt(dx*dx + dy*dy);
  return (d + p[i].r + p[j].r) / 2;
}

void solve(int CASE)
{
  int n;
  cin >> n;
  for (int i = 0; i < n; i++)
    cin >> p[i].x >> p[i].y >> p[i].r;

  if (n == 1)
    printf("Case #%d: %d\n", CASE, p[0].r);
  if (n == 2)
    printf("Case #%d: %d\n", CASE, std::max(p[0].r, p[1].r));

  if (n == 3)
  {
    double min0 = std::max((double)p[0].r, cover(1, 2));
    double min1 = std::max((double)p[1].r, cover(0, 2));
    double min2 = std::max((double)p[2].r, cover(1, 0));
    printf("Case#%d: %.6lf\n", CASE, std::min(min0, std::min(min1, min2)));
  }
}

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++)
    solve(i);

  return 0;
}
