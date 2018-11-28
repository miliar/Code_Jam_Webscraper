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
    int pos[2] = {1, 1};
    int time[2] = {0, 0};
    
    int result = 0;
    
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
      char r;
      int p;
      scanf(" %c%d", &r, &p);
      int ri = getRobot(r);
      result = std::max(std::abs(pos[ri] - p) + time[ri], result) + 1;
      time[ri] = result;
      pos[ri] = p;
    }
    
    printf("Case #%d: %d\n", ti + 1, result);
  }

  return 0;
}
