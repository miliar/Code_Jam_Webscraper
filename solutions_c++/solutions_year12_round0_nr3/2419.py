#include <cstdio>
#include <vector>

int main() {
  int tests, min, max, sol, size, size10, tmp, rest;
  bool taken[2000001];
  std::vector<int> takes;
  scanf("%d", &tests);
  for(int i=0; i<2000000; i++) taken[i] = false;
  for(int z=0; z<tests; z++) {
    scanf("%d%d", &min, &max);
    sol = 0;
    for(int i=min; i<=max; i++) {
      size = 0; size10 = 1; tmp = i;
      while(tmp != 0) { size++; size10*=10; tmp /= 10; }
      size10 /= 10;
      tmp = i;
      takes.clear();
      //for(int l=min; l<=max; l++) taken[l]=false;
      for(int l=0; l<size; l++) {
        rest = tmp % 10;
        tmp /= 10;
        tmp += rest*size10;
        if(tmp <= max && tmp >= min && tmp > i && rest != 0 && !taken[tmp]) { 
          sol++;
          taken[tmp]=true;
          takes.push_back(tmp);
          //printf("%d - %d\n", i, tmp);
        }
      }
      for(int i=0; i<takes.size(); i++) {
        taken[takes[i]]=false;
      }
      takes.clear();
    }
    printf("Case #%d: %d\n", z+1, sol);
  }
}
