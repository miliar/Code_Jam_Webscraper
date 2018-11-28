#include<cstdio>
#include<algorithm>

int main() {
  int tests, num, sur, more, sol, tmp;
  scanf("%d", &tests);
  for(int z=0; z<tests; z++) {
    scanf("%d%d%d", &num, &sur, &more);
    sol = 0;
    for(int i=0; i<num; i++) {
      scanf("%d", &tmp);
      if(tmp >= 3*more-2 || more == 0) sol++;
      else if(sur > 0 && ((more == 1 && tmp >= 2) || (more > 1 && tmp >= 3*more-4))) {
        sol++;
        sur--;
      }
    }
    printf("Case #%d: %d\n", z+1, sol);
  }
}
