#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;
typedef long long i64;

int main() {
  int T;
  scanf("%d", &T);
  for(int Ti=1; Ti<=T; ++Ti) {
    int A, B;
    scanf("%d %d", &A, &B);
    //fprintf(stderr, "%d, %d\n", A, B);
    int digit=0, result=0;
    if(B<10)
      result = -1;
    else if(B<100)
      digit=2;
    else if(B<1000)
      digit=3;
    else if(B<10000)
      digit=4;
    else if(B<100000)
      digit=5;
    else if(B<1000000)
      digit=6;
    else if(B<=2000000)
      digit=7;
    //fprintf(stderr, "%d, \n", digit);

    if(result == -1)
      printf("Case #%d: 0\n", Ti);
    else {
      for(int n=A; n<=B; n++) {
        int nPrev = 0;
        int mPrev = 0;
        for(int Dn=0; Dn <= digit; ++Dn) {
          int D = (int)pow(10.0, (double)(digit-Dn));
          int Dm = (int)pow(10.0, (double)(digit-(digit-Dn)));
          int m = (n-((n/D)*D)) * Dm + (n/D);
          //fprintf(stderr, "%d, %d, %d, %d\n", n, m, D, (n-((n/D)*D)));
          if( (n < m) && (m <= B) ) {
            //fprintf(stderr, "n:%d, m:%d\n", n, m);
            if((nPrev == n) && (mPrev == m))
              fprintf(stderr, "skip n:%d, m:%d\n", n, m);
            else
              result++;

            nPrev = n;
            mPrev = m;
          }
        }
      }
      printf("Case #%d: %d\n", Ti, result);
    }
  }
  return 0;
}

