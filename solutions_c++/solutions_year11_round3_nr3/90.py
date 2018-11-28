#include <iostream>
#include <cstdio>
using namespace std;

const int MaxN = 10001;

int n;
long long freq[MaxN];

long long l, h;


int main() {
  int t; scanf("%d", &t);
  for (int test = 1; test <= t; test++) {
    scanf("%d %lld %lld", &n, &l, &h);
    for (int i = 0; i < n; i++)
      scanf("%lld", &freq[i]);

    long long sol = -1;
    for (long long d = l; d <= h; d++){
      bool ok = true;
      for (int i = 0; i < n; i++)
	if (freq[i] % d != 0 && d % freq[i] != 0){
	  ok = false;
	  break;
	}
      if (ok){
	sol = d;
	break;
      }
    }

    if (sol == -1) printf("Case #%d: NO\n", test);
    else printf("Case #%d: %lld\n", test, sol);
  }

  return 0;
}


   
