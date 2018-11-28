#include <cstdio>
#include <map>

using namespace std;
int A, B;
int digits;

int generate(int x) {
  int i = x;
  int sum = 0;
  do {
      i = (i / 10) + (i % 10) * digits;
    if (i > x && i <= B)
      sum++;
  } while(i != x);
  return sum;
}

int main() {
  int ccN;
  scanf("%d", &ccN);
  for (int cc = 1; cc <= ccN; cc++) {
    scanf("%d%d", &A, &B);
    int tmp = A;
    int sum = 0;
    digits = 1;
    while(tmp > 0) {
      digits *= 10;
      tmp /= 10;
    }
    digits /= 10;
    for (int i = A; i <= B; i++) {
      sum += generate(i);
    }
    printf("Case #%d: %d\n", cc, sum);
  }
  return 0;
}
