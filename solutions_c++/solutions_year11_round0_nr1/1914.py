#include <stdio.h>
#define FOR(q,n) for(int q = 0; q < n; q++)

char tmp[200][10];
int pos[200];

int abs(int x) {
  return (x>0) ? x: -x;
}

void solve() {
 int n;
 scanf("%d", &n);
 FOR(q,n) scanf("%s %d", tmp[q], &pos[q]);
 int t[2] = {0, 0};
 int rpos[2] = {1, 1};
 int lasttime = 0;
 FOR(q, n) {
   int robot = (tmp[q][0] == 'O');
   int distance = abs(rpos[robot] - pos[q]);
   int time = t[robot] + distance + 1;
   if (time < lasttime + 1) time = lasttime + 1;
   t[robot] = time;
   lasttime = time;
   rpos[robot] = pos[q];
 }
 printf("%d\n", lasttime);
}


int main() {
  int t;
  scanf("%d", &t);
  FOR(q, t) {
    printf("Case #%d: ", q+1);
    solve();
  }
}
