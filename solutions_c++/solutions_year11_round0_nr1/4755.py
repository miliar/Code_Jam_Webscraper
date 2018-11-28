#include <cstdio>
#include <iostream>

using namespace std;
int main ()
{
  int T=0, N=0, K=0, M=0;
  char R, A='Z';
  
  cin >> T;
  for (K=0; K<T; K++) {
    cin >> N;

    int B_POS=1, O_POS=1, TARGET=1, POS=1, PAR=0, APAR=0, TOT=0, TMP=0;

    for (M=0; M<N; M++) {

      cin >> R;
      cin >> TARGET;
      
      POS = (R=='O')?O_POS:B_POS;
      TMP = (TARGET>=POS)?(TARGET-POS):(POS-TARGET);
      

      if (R!=A && M != 0) {
	if (TMP >= APAR) {
	  TOT += TMP-APAR+1;
	  APAR = TMP-APAR+1;
	} else {
	  TOT += 1;
	  APAR = 1;
	}
      } else {
	APAR += TMP+1;
	TOT += TMP+1;
      }
      
      A = R;

      if (R == 'O') O_POS = TARGET;
      else B_POS = TARGET;

      
    }
    printf("Case #%d: %d\n", K+1, TOT);

  }
  
  return 0;
}
