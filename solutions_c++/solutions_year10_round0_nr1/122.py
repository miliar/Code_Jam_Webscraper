#include <iostream>

using namespace std;

int test,nTests;
int N,K;

int main() {
  scanf("%d",&nTests);
  for (test = 1; test <= nTests; ++test) {
    scanf("%d %d",&N,&K);
    printf("Case #%d: ",test);
    if ((((1 << N) - 1) & K) == ((1 << N) - 1))
      printf("ON\n");
    else
      printf("OFF\n");
  }
  return 0;
}
