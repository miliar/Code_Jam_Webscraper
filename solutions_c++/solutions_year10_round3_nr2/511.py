#include<stdio.h>
#include<algorithm>
using namespace std;

int t, c;

int solve(int a, int b) {
  if(a*c >= b)
    return 0;
  int ret = 1000000;
  int fac = c;
  for(int i=0;;i++) {
    int b2 = b/fac;
    if(b2 < a)
      break;
    if(b2*fac != b)
      b2++;
    int ass =(i+2)/2;
    if(i == 0) ass = 0;
    ret = min(ret, 1+max(ass,solve(a,b2)));
    fac *= c;
  }
  return ret;
}
     

int main() {
  scanf("%d",&t);
  for(int test=1;test<=t;test++) {
    int a, b, ret = 0;
    scanf("%d %d %d",&a,&b,&c);    
    printf("Case #%d: %d\n",test,solve(a,b));
  }
  return 0;
}
    
