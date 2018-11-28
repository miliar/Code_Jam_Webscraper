#include <stdio.h>


const int MAXVAL = 15000;

int delta[MAXVAL+1];


int main() {


  int T;
  scanf("%d", &T);

  for(int casen = 1; casen <= T; ++casen) {
    for(int i = 0; i < MAXVAL; ++i) {
      delta[i] = 0;
    }
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; ++i) {
      int v;
      scanf("%d", &v);
      ++delta[v];
      --delta[v+1];
    }
    if(n == 0) {
      printf("Case #%d: %d\n", casen, 0);
      continue;
    }
    int a = 1;
    int b = n;
    while(a < b) {
      int c = a+(b-a+1)/2;

      int p = c;
      int v = delta[p];
      for(int i = 0; i < MAXVAL && p < MAXVAL; ++i) {
	for(int j = 0; j < delta[i] && p < MAXVAL; ++j) {
	  while(p < MAXVAL && (p < i + c || v >= 0)) {
	    p += 1;
	    v = delta[p];
	  }
	  if(p >= MAXVAL) break;
	  v += 1;
	}
      }
      if(p < MAXVAL) {
	a = c;
      } else {
	b = c-1;
      }
    }
    printf("Case #%d: %d\n", casen, a);
  }


  return(0);
}
