#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cassert>
#include <set>
using namespace std;

typedef long long int i64;

typedef pair<i64, i64> PII;

i64 cx[1008];
i64 cy[1008];

int main() {
  int t, T, i, j, k, N, A;
  i64 pA, pB, pC, pD, M, x, y;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    set<PII> st;
    scanf("%d", &N);
    scanf("%lld %lld %lld %lld", &pA, &pB, &pC, &pD);
    scanf("%lld %lld %lld", &cx[0], &cy[0], &M);
    st.insert(PII(cx[0], cy[0]));
    for (i=1; i<N; i++) {
      cx[i]=(pA*cx[i-1]+pB)%M;
      cy[i]=(pC*cy[i-1]+pD)%M;
      st.insert(PII(cx[i], cy[i]));
    }
    A=0;
    for (i=0; i<N-2; i++)
      for (j=i+1; j<N-1; j++)
	for (k=j+1; k<N-0; k++) {
	  x=cx[i]+cx[j]+cx[k];
	  y=cy[i]+cy[j]+cy[k];
	  if (x%3==0 && y%3==0)
	    // if (st.count(PII(x/3, y/3)))
	    A++;
	}
    printf("Case #%d: %d\n", t, A);
  }
  return 0;
}
