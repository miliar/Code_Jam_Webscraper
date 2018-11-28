#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <vector>


void readAndSolveSingleCase() {

  int n, sum = 0, wrong_sum = 0, minimum = 1<<30, current;
  
  scanf("%d ",&n);
  for (int i=0; i<n; i++){
    scanf("%d",&current);
    wrong_sum ^= current;
    minimum = std::min(current, minimum);
    sum += current;
    
  }
  
  if (wrong_sum != 0) puts("NO");
  else printf("%d\n",sum - minimum);
}

int main(){
  int cases;
  scanf("%d", &cases);
  for (int i = 1; i <= cases; i++) {
    printf("Case #%d: ",i);
    readAndSolveSingleCase();
  }
  return 0;
}
