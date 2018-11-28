#include <iostream>
#include <cmath>
using namespace std;

int main()
{ 
  int T;
  fscanf(stdin, "%d", &T);
  int N, K;
  for(int t = 1; t <= T; t++) {
    fscanf(stdin, "%d %d", &N, &K);
    int pow_2_N = (int)pow(2,N);
    if(K%pow_2_N == pow_2_N-1)
      printf("Case #%d: ON\n", t);
    else
      printf("Case #%d: OFF\n", t); 
  }
  return 0;
}
