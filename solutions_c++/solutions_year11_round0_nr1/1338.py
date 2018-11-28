#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <iostream>
#include <map>
#include <cmath>
#include <set>
#include <queue>
#include <cstring>
#include <fstream>
using namespace std;
typedef long long LL;

#define INF 2000000000
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++)
#define FS first
#define SD second
#define MP make_pair
#define FF fflush(stdout);
#define MIN(a,b) a<b?a:b

queue<pair<int, int> > Q[2];
int P[2];
int cur,cur2;

void go(int a) {
  if (!Q[a].empty()) {
    pair<int,int> p = Q[a].front();
    if (p.FS != P[a]) {
      if (P[a] < p.FS) P[a]++;
      else P[a]--;
    }
    else {
      if (cur == p.second) {
        Q[a].pop();
        cur2 = cur + 1;
      }
    }
  }
}

int main() {
  int T;scanf("%d",&T);
  FORE(test,1,T) {
    int n;scanf("%d ",&n);
    FOR(i,0,n) {
      char c;int a;
      scanf("%c %d ", &c, &a);
      if (c == 'O') {
        Q[0].push(MP(a,i));
      }
      else {
        Q[1].push(MP(a,i));
      }
    }
    P[0] = P[1] = 1;
    int ret = 0;
    cur = 0;
    while (!Q[0].empty() || !Q[1].empty()) {
      cur2 = cur;
      go(0);go(1);
      cur = cur2;
      ret++;
    }
    printf("Case #%d: %d\n", test, ret);
  }
}
