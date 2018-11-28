#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int nt, nt0;
int n, c;

int main() {
  scanf(" %d", &nt0);
  for(nt = 1 ; nt <= nt0 ; nt++) {
    scanf(" %d", &n);

    int xorc = 0, sumc = 0, small = 1048576;
    for(int i=0 ; i<n ; i++) {
      scanf(" %d", &c);
      xorc ^= c;
      sumc += c;
      small = min(small, c);
    }

    printf("Case #%d: ", nt);
    if(xorc) printf("NO\n");
    else printf("%d\n", sumc-small);
  }
  return 0;
}
