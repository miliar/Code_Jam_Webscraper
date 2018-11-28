#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cassert>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define DEBUG(format, args...) do { fprintf(stderr, format, ## args); fflush(stderr); } while (0)
#define PRINT(format, args...) do { fprintf(stdout, format, ## args); DEBUG(format, ## args); } while (0)

#define SIZE(__c) (int)(__c).size()
#define FOREACH(__i, __c) for (typeof(__c.begin()) __i=__c.begin(); __i!=__c.end(); ++__i)

typedef signed long long int i64;

struct QueueItem {
  int y, x, m;
  QueueItem(int y, int x, int m): y(y), x(x), m(m) {}
};

const int INF=0x20202020;

int Y, X;
int fd[10];
int dp[10][6][1<<12];
int bn[10][6][1<<12];

int ToBinary(const char *rw);
int IsEmpty(int m, int x);
int GetTwoRows(int m1, int m2);

int main() {
  char bf[64];
  int i, m, M, dx, nx, y, rc, rn, F, A, t, T;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    scanf("%d %d %d", &Y, &X, &F);
    for (i=0; i<Y; i++) {
      scanf("%s", bf);
      fd[i]=ToBinary(bf);
    }
    A=INF;
    M=(1<<X)-1;
    m=GetTwoRows(fd[0], fd[1]);
    memset(dp, 0x20, sizeof dp);
    memset(bn, 0x00, sizeof bn);
    dp[0][0][m]=0;
    deque<QueueItem> dq;
    dq.push_front(QueueItem(0, 0, m));
    while (!dq.empty()) {
      QueueItem qi=dq.front();
      dq.pop_front();
      if (bn[qi.y][qi.x][qi.m])
        continue;
      bn[qi.y][qi.x][qi.m]=1;
      rc=qi.m&M;
      rn=(qi.m>>X)&M;
      for (dx=(-1); dx<=1; dx+=2) {
        nx=qi.x+dx;
        if (0<=nx && nx<X)
          if (IsEmpty(rc, nx)) {
            // go
            if (!IsEmpty(rn, nx))
              if (dp[qi.y][nx][qi.m]>dp[qi.y][qi.x][qi.m]) {
                dp[qi.y][nx][qi.m]=dp[qi.y][qi.x][qi.m];
                dq.push_front(QueueItem(qi.y, nx, qi.m));
              }
            if (IsEmpty(rn, nx)) {
              for (y=qi.y+2; y<Y && IsEmpty(fd[y], nx); y++)
                ;
              y--;
              if (y-qi.y<=F)
                if (y==Y-1)
                  A=min(A, dp[qi.y][qi.x][qi.m]);
                else if (y==qi.y+1) {
                  m=GetTwoRows(rn, fd[y+1]);
                  if (dp[y][nx][m]>dp[qi.y][qi.x][qi.m]) {
                    dp[y][nx][m]=dp[qi.y][qi.x][qi.m];
                    dq.push_front(QueueItem(y, nx, m));
                  }
                }
                else {
                  m=GetTwoRows(fd[y], fd[y+1]);
                  if (dp[y][nx][m]>dp[qi.y][qi.x][qi.m]) {
                    dp[y][nx][m]=dp[qi.y][qi.x][qi.m];
                    dq.push_front(QueueItem(y, nx, m));
                  }
                }
            }
            // dig
            if (!IsEmpty(rn, nx)) {
              m=GetTwoRows(rc, rn-(1<<nx));
              if (dp[qi.y][qi.x][m]>dp[qi.y][qi.x][qi.m]+1) {
                dp[qi.y][qi.x][m]=dp[qi.y][qi.x][qi.m]+1;
                dq.push_back(QueueItem(qi.y, qi.x, m));
              }
            }
          }
      }
    }
    if (A==INF)
      PRINT("Case #%d: No\n", t);
    else
      PRINT("Case #%d: Yes %d\n", t, A);
  }
  return 0;
}

int ToBinary(const char *rw) {
  int i, A=0;
  for (i=0; rw[i]; i++)
    if (rw[i]=='#')
      A|=(1<<i);
  return A;
}

int IsEmpty(int m, int x) {
  return (m&(1<<x))==0;
}

int GetTwoRows(int m1, int m2) {
  return m1|(m2<<X);
}
