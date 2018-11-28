#include <cstdio>

int main() {
  int n_tests;
  scanf("%d",&n_tests);
  long long N, PD, PG;
  for (int j = 1 ; j <= n_tests ; j++) {
    scanf("%lld %lld %lld",&N,&PD,&PG);
    bool ok = false;
    
    if (PD == 0 && PG == 0)
      ok = true;
    else if (PG == 0) {
      ok = false;
    }
    else if (PD != 100 && PG == 100)
      ok = false;
    else if (N < 100) {
      for (long long i = N ; i >= 1 ; i--) {
	if ((i*PD)%100 != 0)
	  continue;
	ok = true;
	break;
      }
    }
    else  {
      ok = true;
    }

    printf("Case #%d: ",j);
    if (ok)
      printf("Possible\n");
    else
      printf("Broken\n");
  }
  return 0;
}
