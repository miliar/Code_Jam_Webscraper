#include <iostream>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <algorithm>
#include <vector>
#include <map>
#include <deque>
#include <list>
#include <set>
#include <stack>
#include <queue>
#include <string>

//External
#include <gmpxx.h>

using namespace std;

int main(int argc, char * argv[]){

  int T, B, C;

  scanf("%d", &T);
  for(int t=0; t<T; t++){

    int total=0;
    int R, k, N;
    scanf("%d %d %d", &R, &k, &N);
    int * g = (int *) malloc(sizeof(int) * N);

    for(int n=0; n<N; n++){
      scanf("%d", g+n);
    }

    int gpos=0;
    for(int r=0; r<R; r++){
      int gstart=gpos;
      int p=0;
      while(p+g[gpos]<=k){
        p+=g[gpos++];
        if(gpos >= N) gpos=0;
        if(gpos == gstart){
          break;
        }
      }
      total += p;
    }

    printf("Case #%d: %d\n", t+1, total);
    
  }

  return 0;

}
