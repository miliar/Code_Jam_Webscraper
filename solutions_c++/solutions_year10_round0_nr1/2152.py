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

  int T, N, K;

  scanf("%d", &T);
  for(int t=0; t<T; t++){

    scanf("%d %d", &N, &K);
    bool bit = (K & ((1 << N)-1)) == ((1 << N)-1);
    if(bit) printf("Case #%d: ON\n", t+1);
    else printf("Case #%d: OFF\n", t+1);

  }

  return 0;

}




