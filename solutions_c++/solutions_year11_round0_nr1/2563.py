#include <cstdio>

using namespace std;

int abs(int a) {
  return a>0?a:-a;
}

int main() {
  int T; scanf("%d", &T);
  for(int t=1; t<=T; ++t) {
    int n; scanf("%d", &n);
    int ans = 0;
    int pos[2] = {1, 1};
    int when[2] = {0, 0};
    for(int i=0; i<n; ++i) {
      char ch; int k; scanf(" %c %d", &ch, &k);
      int who = ch == 'O';
      int req = abs(pos[who]-k);
      req -= ans-when[who];
      req = req<0?0:req;
      ans += req + 1;
      pos[who]  = k;
      when[who] = ans;
    }
    printf("Case #%d: %d\n", t, ans);
  }
}
