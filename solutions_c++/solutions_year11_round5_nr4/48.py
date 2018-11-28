#include <cstdio>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <sstream>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

char s[150];

int check(long long x) {
  long long y = (long long)sqrt(x) - 1;
  while (y * y < x) {
    y++;
  }
  if (y * y == x) {
    int l = (int)strlen(s) - 1;
    while (l >= 0)
      putchar(((x >> l) & 1) + '0'), l--;
    puts("");
    return 1;
  }
  return 0;
}
int nt, tn;

int main(void)
{
  freopen("D-small-attempt0.in", "r", stdin);
  freopen("D-small-attempt0.out", "w", stdout);
//  freopen("D-large.in", "r", stdin);
//  freopen("D-large.out", "w", stdout);

  scanf("%d", &nt);
  for (tn=0; tn<nt; tn++)
  {
    fprintf(stderr, "Case #%d: \n", tn+1);

    printf("Case #%d: ", tn+1);

    scanf("%s", s);
    long long m1=0, m2=0;
    for (int i=0; s[i]; i++) {
      m1 <<= 1;
      m2 <<= 1;
      if (s[i] == '?')
        m2 |= 1ll;
      else 
        m1 |= (long long)(s[i] - '0');
    }

    for (long long i=m2; i>0; i=m2 & (i-1))
      if (check(i+m1)) {
        break;
      }
    check(m1);
  }
  return 0;
}
