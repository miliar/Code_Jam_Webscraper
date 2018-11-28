#include <cstdio>
#include <set>

int main() {
  int T;
  scanf("%d", &T);
  for(int i = 1; i <= T; ++i) {
    printf("Case #%d: ", i);

    int A, B, dc = 1;
    scanf("%d%d", &A, &B);

    for(int t = A; t; t /= 10)
      dc *= 10;

    int count = 0;
    std::set<int> S;

    for(int q = A; q <= B; ++q) {
      S.clear();
      for(int c = 10; c < dc; c *= 10) {
        if((q / (c / 10)) % 10 != 0) { //no leading zeroes
          int s = q / c + (q % c) * (dc / c);
          if(s > q && s <= B) {
            S.insert(s);
          }
        }
      }
      count += S.size();
    }

    printf("%d\n", count);
  }
}
