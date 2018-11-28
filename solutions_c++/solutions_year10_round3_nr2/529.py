int N;

#include <stdio.h>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <assert.h>

using namespace std;

int verify(int L, int P, int C) {
  int range = 0;
  while (L*C < P) {
    L*=C;
    range ++;
  }
  int result = 0;
  while (range > 0) {
    range >>= 1;
    result ++;
  }
  return result;
}

int main()
{
  // Input
  scanf("%d\n",&N);
  fprintf(stderr,"N = %d: \n",N);

  // Output
  for (int x=1; x<=N; x++) {
    fprintf(stderr,"Case #%d: \n",x);

    int L,P,C;
    scanf("%d %d %d\n",&L,&P,&C);
    
#if 0
    double low = log((double)L) / log((double)C);
    double high = log((double)P) / log((double)C);
    double range = high - low;
    int tests = ceil(log(high - low) / log(2));
    if (tests < 0) tests = 0;
    int tests2 = verify(L,P,C);
    assert(tests == tests2);
#else
    int tests = verify(L,P,C);
#endif
    
    printf("Case #%d: %d\n",x, tests);
  }
  return 0;
}
