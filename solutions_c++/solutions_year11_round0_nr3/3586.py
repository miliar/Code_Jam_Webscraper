#include<stdio.h>
#include<vector>
#include<math.h>
#include<stdlib.h>
using namespace std;

int tests, n, sum, mini;
int bits[20];

int main() {
  scanf("%d",&tests);
  for(int t=1;t<=tests;t++) {
    scanf("%d",&n);
    sum = 0; mini = 10000000;
    memset(bits,0,sizeof(bits));    
    for(int i=0;i<n;i++) {
      int next;
      scanf("%d",&next);
      sum += next;
      if(mini > next)
        mini = next;
      for(int j=0;next > 0;next /= 2) {
        bits[j] += next%2;
        j++;
      }
    }
    bool ok = 1;
    for(int i=0;i<20;i++) {
      if(bits[i]%2 == 1) {
        ok = 0;
        break;
      }
    }
    if(ok)
      printf("Case #%d: %d\n",t,sum-mini);
    else
      printf("Case #%d: NO\n",t);
  }
  return 0;  
}
            
      
    
    
      
    
    
