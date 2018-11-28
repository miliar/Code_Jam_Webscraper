#include <cstdio>
#include <climits>
#include <cstring>
#include <cctype>
#include <queue>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>

using namespace std;
typedef long long ll;
ll tone[10010];

int main() {
  int ca;
  scanf(" %d", &ca);

  for (int ii = 0; ii < ca; ii++) {
    ll N, L, H;
    scanf(" %lld%lld%lld", &N, &L, &H);

    for (int i = 0; i < N; i++) scanf(" %lld", tone + i);

    ll ans = -1;

    for (int i = L; i <= H; i++) {
      bool f = true;
      for (int j = 0; j < N; j++) {
	if (tone[j] % i != 0 && i % tone[j] != 0) {
	  f = false;
	  break;
	}
      }
      if (f) {
	ans = i;
	break;
      }
    }
    
    printf("Case #%d: ", ii+1);
    if (ans != -1) {
      printf("%lld\n", ans);
    } else {
      printf("NO\n");
    }
  }
}
