#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string>
using namespace std;
#define N 10000

int main()
{
  int t, index, i, j, len;
  int p,k,l;
  long long r, f[N];
  scanf("%d", &t);
  for(index = 1; index <= t; index++) {
    scanf("%d%d%d", &p, &k, &l);
    for(i = 0; i < l; i++)
      scanf("%lld", &f[i]);
    sort(f, f+l);
    r = 0;
    for(i = l-1, j=k, len = 1; i >= 0; i--, j--) {
      if(j==0) { j = k; ++len;}
      r += (long long)len * f[i];
    }
    printf("Case #%d: %lld\n", index, r);
  }
}

