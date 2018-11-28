#include <cstdio>
#include <cstdlib>
#include <cmath>

int main(){
  unsigned tests, test;
  scanf("%d", &tests);

  for (test=0;test<tests;test++){
    unsigned l, p, c;
    scanf("%d %d %d", &l, &p, &c);
    unsigned iter = 0;
    while (l<p){
      l *= c;
      iter++;
    }
    iter--;

    unsigned answer;
    if (iter == 0)
      answer = 0;
    else answer = (log((double)iter)/log(2.0))+1;

    printf("Case #%i: %i\n", test+1, answer);
  }
}
