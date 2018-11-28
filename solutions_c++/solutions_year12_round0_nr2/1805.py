#include <stdio.h>

using namespace std;

int main (){

  int T, N, S, p, i, j, max;
  int ti [200];

  scanf ("%d ", &T);

  for (i = 0; i < T; i++){
    
    max = 0;
    scanf ("%d %d %d ", &N, &S, &p);
    
    for (j = 0; j < N; j++){
      scanf ("%d ", &ti[j]);
    
    }
 
    for (j = 0; j < N; j++){
      if (ti[j] / 3. >= p)
	max++;
      else if (ti[j] / 3. >= p - 2){
	if (p > 0 && p - 1 + p - 1 + p == ti[j])
	  max++;
	else if (p - 1 + p + p == ti[j])
	  max++;
	else if (S != 0){
	  if (p > 1 && p - 2 + p - 2 + p == ti[j]){
	    max++;
	    S--;
	  }
	  else if (p > 1 && p - 2 + p - 1 + p == ti[j]){
	    max++;
	    S--;
	  }
	  else if (p > 1 && p - 2 + p + p == ti[j]){
	    max++;
	    S--;
	  }	  
	}
      }
    }

    printf ("Case #%d: %d\n", i + 1, max);
    
    
  }
  return 0;
}
