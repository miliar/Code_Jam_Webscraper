#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <queue>
#include <map>
#include <vector>
#include <algorithm>
#include <time.h>
#include <cmath>
#include <cassert>
using namespace std;

typedef long long ll;

#define MAXN 1100
char c[2] = {'O', 'B'};
char ch[MAXN];
int npos[MAXN];
int p[2];
int t[2];
int ans;

int main() {
#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  int tests; scanf("%d", &tests);
  for(int tt = 1; tt <= tests; tt++) {
    printf("Case #%d: ", tt);
    int n; scanf("%d", &n);
    for(int i = 0; i < n; i++) {
      string s; cin >> s; cin >> npos[i];
      ch[i] = s[0];
    }
    int turn = ch[0] == 'O' ? 0 : 1;
    t[0] = t[1] = 0;
    p[0] = p[1] = 1;
    int cur = 0;
    while(cur < n) {
      t[turn] = max(t[turn ^ 1], t[turn] + abs(npos[cur] - p[turn])) + 1;
      p[turn] = npos[cur++];
      while(cur < n && ch[cur] == c[turn]) {
	t[turn] += abs(npos[cur] - p[turn]) + 1;
	p[turn] = npos[cur];
	cur++;
      }
      turn ^= 1;
    }
    printf("%d\n", max(t[0], t[1]));
  }

}
