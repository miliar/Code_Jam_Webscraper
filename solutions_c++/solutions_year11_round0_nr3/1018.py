#include <cstdio>
#include <cstdlib>
#include <algorithm>    

int getRobot(char x) {
  return (x == 'O') ? 0 : 1;
}

int main() {
  int t;
  scanf("%d", &t);
  for (int ti = 0; ti < t; ++ti) {
    int sum = 0;
    int minElement = 1000001;
    int xsum = 0;
    
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
      int x;
      scanf("%d", &x);
      sum += x;
      xsum ^= x;
      minElement = std::min(x, minElement);
    }
    
    printf("Case #%d: ", ti + 1);
    if (xsum == 0) {
        printf("%d\n", sum - minElement);
    }
    else {
        printf("NO\n");
    }
  }

  return 0;
}
