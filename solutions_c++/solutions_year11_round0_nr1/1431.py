
#include <stdio.h>

main() {

  int T;

  scanf("%d",&T);

  for (int t = 1; t <= T; t++) {

    int secs = 0;

    int N;

    scanf("%d\n",&N);
    
    int posO = 1;
    int posB = 1;
    int secO = 0;
    int secB = 0;
    
    for (int n = 0; n < N; n++) {
      char r;
      int button;
      scanf("%c %d\n",&r,&button);

      // robot r needs to move to button, and then press it;
      if (r == 'O') {
	int s = button - posO;
	if (s < 0) s = -s;
	if (secs - secO > 0) {
	  s -= (secs - secO);
	}
	if (s < 0) s = 0;
	secs += s + 1;
	secO = secs;
	posO = button;
      }
      if (r == 'B') {
	int s = button - posB;
	if (s < 0) s = -s;
	if (secs - secB > 0) {
	  s -= (secs - secB);
	}
	if (s < 0) s = 0;
	secs += s + 1;
	secB = secs;
	posB = button;
      }
      

    }
    
    
    printf( "Case #%d: %d\n",t,secs);


  }



}
