int N, T;
int K;

#include <stdio.h>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
  // Input
  scanf("%d\n",&T);
  fprintf(stderr,"T = %d: \n",T);

  // Output
  for (int x=1; x<=T; x++) {
    scanf("%d %d\n",&N, &K);
    //fprintf(stderr,"N = %d: \n",N);

    //fprintf(stderr,"Case #%d: %s\n",x, (((K+1) ^ K) & (1<<N)) ? "ON" : "OFF");
    printf("Case #%d: %s\n",x, (((K+1) ^ K) & (1<<N)) ? "ON" : "OFF");
  }
  return 0;
}
