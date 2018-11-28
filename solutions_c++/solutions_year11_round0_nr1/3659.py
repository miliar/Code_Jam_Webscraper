#include <cstdio>
#include <cstring>
#include <cctype>
#include <queue>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;

int main() {
  int ca;
  scanf(" %d", &ca);

  for (int ii = 0; ii < ca; ii++) {
    int N;
    int pa, pb, ta, tb, cur;
    cur = ta = tb = pa = pb = 1;
    
    scanf(" %d", &N);
    for (int i = 0; i < N; i++) {
      int p; char c;
      scanf(" %c %d", &c, &p);
      if (c == 'O') {
	cur = max(cur + 1, ta + abs(pa - p) + 1);
	ta = cur;
	pa = p;
      } else {
	cur = max(cur + 1, tb + abs(pb - p) + 1);
	tb = cur;
	pb = p;
      }
    } 
    printf("Case #%d: %d\n", ii+1, cur - 1);
  }
}
