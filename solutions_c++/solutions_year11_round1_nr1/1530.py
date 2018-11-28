#define COMPILEA
#ifdef COMPILEA

#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cctype>

#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <functional>

#include <assert.h>

typedef unsigned int  uint;
typedef unsigned char uchar;

using namespace std;


int main(int argc, char *argv[]) {
  if(argc < 2 || argc > 2)
    return 1;
  FILE* inf = fopen(argv[1],"r");
  FILE* ouf = fopen("output.txt","w");

  int T;
  fscanf(inf,"%i", &T);

  for(int t = 0; t < T; ++t) {
    int N, Pd, Pg;
    fscanf(inf,"%i %i %i", &N, &Pd, &Pg);
    //determine if percents are possible
    for(int i = N; i > 0; --i) { //denom
      for(int j = 0; j <= i; ++j) { //num
        if(Pd * i == (j * 100)) {
          goto lbl_possible;
        }
      }
    }
    lbl_not_possible:
    fprintf(ouf, "Case #%i: Broken\n", t+1);
    continue;
    lbl_possible:
    if((Pd == Pg) || (Pg < 100 && Pg > 0))
      fprintf(ouf, "Case #%i: Possible\n", t+1);
    else goto lbl_not_possible;
  }

  fclose(inf);
  fclose(ouf);


  return 0;
}

#endif
