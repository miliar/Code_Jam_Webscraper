#include <stdio.h>
#include <vector>
#include <string>
#include <set>
#include <math.h>


using namespace std;


int main() 
{
  int cases;

  scanf("%d", &cases);
  
  for(int i=0;i< cases; i++) {
    long long l,p,c;

    scanf("%lld%lld%lld", &l, &p, &c);
    
    int tests = 0;//ceil(log(p-l) * log(c+1));
    
    // printf("ratio between %d and %d (%f) and want %d\n", l, p, (double)p / (double) l, c);


    //printf("log guess is %f\n", log(log(p) / log(p-l)) / log(2));// log(log(p-l) / log(c+1)) / log(c));
    while(p > l * c) {
      int diff = p-l;
      long long guess = sqrt(l*p) - 5;

      while(guess * guess < l * p) {
	guess++;
      }

      
	p = guess;
      
      //l = l + (diff / (c+1));
      //printf("diff is %d, top is %d, bottom is %d doing a test at %d\n", diff, p, p-diff,  l); 
      tests++;
    }
    //printf("ratio between %d and %d (%f) and want %d\n", l, p, (double)p / (double) l, c);

     
    printf("Case #%d: %d\n", i+1, tests);
  }

  return 0;
}
