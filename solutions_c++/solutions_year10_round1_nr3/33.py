#include <cstdio>
#include <algorithm>
using namespace std;

double const phi = 1.6180339887498948482L;

long long solve2(int a1, int a2, int b1, int b2)
{
  http://www.rpi.edu/~mitchj/math1900/topics/euclideangamestrategy/
  long long res = 0;
  for (int b = b1; b <= b2; b++) {
    int am = max(a1, int(b*phi) + 1);
    res += max(0, a2 - am + 1);
  }
  return res;
}

long long solve(int a1, int a2, int b1, int b2)
{
  return solve2(a1, a2, b1, b2) + solve2(b1, b2, a1, a2);
}

int main()
{
  int t;
  scanf("%d", &t);
  for (int case_ = 1; case_ <= t; case_++) {
    int a1, a2, b1, b2;
    scanf("%d %d %d %d", &a1, &a2, &b1, &b2);
    printf("Case #%d: %lld\n", case_, solve(a1, a2, b1, b2));
  }
  return 0;
}
