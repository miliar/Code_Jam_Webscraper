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
//#include <gmpxx.h>

using namespace std;

int main(int argc, char * argv[]){

  int C;

  scanf("%d", &C);
  for(int c=0; c<C; c++){

    int N, K, B, T;
    scanf("%d %d %d %d", &N, &K, &B, &T);

    std::vector<int> pos(N);
    std::vector<int> speed(N);

    for(int n=0; n<N; n++){
      int tmp;
      scanf("%d", &tmp);
      pos[n] = tmp;
    }
    for(int n=0; n<N; n++){
      int tmp;
      scanf("%d", &tmp);
      speed[n] = tmp;
    }

    
    int count=0;
    int swaps=0;
    int swapc=0;

    for(int i=N-1; i>=0; i--){
      int endpos = pos[i] + speed[i]*T;
      if(endpos>=B){
        count++;   //TODO check
        swaps+=swapc;
      }else swapc++;
      if(count>=K) break;
    }

    if(count<K) printf("Case #%d: IMPOSSIBLE\n", c+1); 
    else printf("Case #%d: %d\n", c+1, swaps);

  }

  return 0;

}
