#include <cstdio>
using namespace std;

const char *format = "Case #%d: %s\n";
const char *on = "ON";
const char *off = "OFF";

bool solve(unsigned n, unsigned k)
{
  unsigned mask = (1 << n) - 1;
  if(k < mask)
    return false;
  k -= mask;
  return (k & mask) == 0;
}

int main(void)
{
  int t;
  scanf("%d", &t);
  for(int i = 1; i <= t; ++i) {
    unsigned n, k;
    scanf("%u%u", &n, &k);
    printf(format, i, solve(n, k) ? on : off);
  }
  return 0;
}
