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

#define PRUSH(stream, format, args...) do { fprintf(stream, format, ## args); fflush(stream); } while (0)
#define DEBUG(format, args...) do { PRUSH(stderr, format, ## args); } while (0)
#define PRINT(format, args...) do { PRUSH(stdout, format, ## args); DEBUG(format, ## args); } while (0)

#define SIZE(__c) (int)(__c).size()
#define FOREACH(__i, __c) for (typeof(__c.begin()) __i=__c.begin(); __i!=__c.end(); ++__i)

typedef signed long long int i64;

const int INF=0x20202020;

const int DY[]={-1, 0, 1, 0};
const int DX[]={0, 1, 0, -1};

struct BoxConfig {
  int y, x, m, b;
  BoxConfig(int y, int x, int m, int b): y(y), x(x), m(m), b(b) {
  }
  bool operator<(const BoxConfig &o) const {
    if (y!=o.y) return y<o.y;
    if (x!=o.x) return x<o.x;
    return m<o.m;
  }
};

struct QueueItem {
  int y, x, d;
  BoxConfig bc;
  QueueItem(int y, int x, const BoxConfig &bc): y(y), x(x), d(INF), bc(bc) {}
  bool operator<(const QueueItem &o) const { return d>o.d; }
};

char fd[32][32];
int dt[32][32][64];
map<BoxConfig, int> mp[6];

void GenerateBoxConfigs();
void PlaceBox(int y, int x, int minY, int minX, int maxY, int maxX, int b, int B);

QueueItem GetBoxConfig(const char fd[][32], int y1, int x1, int y2, int x2, char c1, char c2);
int GetBoxConfigId(const BoxConfig &bc);

void DrawQueueItem(const QueueItem &qi, char c);

int GetDistance(const QueueItem &qi);
void SetDistance(const QueueItem &qi, int d);

bool inBounds(int y, int x, int Y, int X);

int main() {
  GenerateBoxConfigs();
  int y, x, ny, nx, d, Y, X, A, t, T;
  int y2, x2, ny2, nx2, d2;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    scanf("%d %d", &Y, &X);
    for (y=0; y<Y; y++)
      scanf("%s", fd[y]);
    QueueItem qs=GetBoxConfig(fd, 0, 0, Y-1, X-1, 'o', 'w');
    QueueItem qt=GetBoxConfig(fd, 0, 0, Y-1, X-1, 'x', 'w');
    DrawQueueItem(qs, '.');
    DrawQueueItem(qt, '.');
    memset(dt, ' ', sizeof dt);
    SetDistance(qs, qs.d=0);
    priority_queue<QueueItem> pq;
    pq.push(qs);
    while (!pq.empty()) {
      QueueItem qi=pq.top();
      pq.pop();
      if (GetDistance(qi)!=qi.d)
        continue;
      DrawQueueItem(qi, 'o');
      for (y=qi.y; y<qi.y+qi.bc.y; y++)
        for (x=qi.x; x<qi.x+qi.bc.x; x++)
          if (fd[y][x]=='o')
            for (d=0; d<4; d++)
              if (inBounds(y-DY[d], x-DX[d], Y, X) && fd[y-DY[d]][x-DX[d]]=='.' &&
                  inBounds(y+DY[d], x+DX[d], Y, X) && fd[y+DY[d]][x+DX[d]]=='.') {
                ny=y+DY[d];
                nx=x+DX[d];
                fd[y][x]='.';
                fd[ny][nx]='o';
                QueueItem q1=GetBoxConfig(fd,
                                          min(qi.y, ny),
                                          min(qi.x, nx),
                                          max(qi.y+qi.bc.y-1, ny),
                                          max(qi.x+qi.bc.x-1, nx),
                                          'o', 'o');
                if (GetBoxConfigId(q1.bc)>=0) {
                  if (GetDistance(qi)+1<GetDistance(q1)) {
                    SetDistance(q1, q1.d=GetDistance(qi)+1);
                    pq.push(q1);
                  }
                }
                else
                  for (y2=min(qi.y, ny); y2<=max(qi.y+qi.bc.y-1, ny); y2++)
                    for (x2=min(qi.x, nx); x2<=max(qi.x+qi.bc.x-1, nx); x2++)
                      if (fd[y2][x2]=='o')
                        for (d2=0; d2<4; d2++)
                          if (inBounds(y2-DY[d2], x2-DX[d2], Y, X) &&
                              inBounds(y2+DY[d2], x2+DX[d2], Y, X))
                            if (fd[y2-DY[d2]][x2-DX[d2]]=='.' &&
                                fd[y2+DY[d2]][x2+DX[d2]]=='.') {
                              ny2=y2+DY[d2];
                              nx2=x2+DX[d2];
                              fd[y2][x2]='.';
                              fd[ny2][nx2]='o';
                              QueueItem q2=GetBoxConfig(fd,
                                                        min(qi.y, min(ny, ny2)),
                                                        min(qi.x, min(nx, nx2)),
                                                        max(qi.y+qi.bc.y-1, max(ny, ny2)),
                                                        max(qi.x+qi.bc.x-1, max(nx, nx2)),
                                                        'o', 'o');
                              if (GetBoxConfigId(q2.bc)>=0)
                                if (GetDistance(qi)+2<GetDistance(q2)) {
                                  SetDistance(q2, q2.d=GetDistance(qi)+2);
                                  pq.push(q2);
                                }
                              fd[ny2][nx2]='.';
                              fd[y2][x2]='o';
                            }
                fd[ny][nx]='.';
                fd[y][x]='o';
              }
      DrawQueueItem(qi, '.');
    }
    A=GetDistance(qt);
    PRINT("Case #%d: %d\n", t, A==INF ? -1 : A);
  }
  return 0;
}

void GenerateBoxConfigs() {
  for (int b=1; b<=5; b++)
    PlaceBox(17, 17, 17, 17, 17, 17, 1, b);
}

void PlaceBox(int y, int x, int minY, int minX, int maxY, int maxX, int b, int B) {
  fd[y][x]='o';
  if (b==B) {
    QueueItem qi=GetBoxConfig(fd, minY, minX, maxY, maxX, 'o', 'o');
    BoxConfig &bc=qi.bc;
    if (!mp[bc.b].count(bc)) {
      mp[bc.b][bc]=1;
      mp[bc.b][bc]=SIZE(mp[bc.b])-1;
    }
  }
  else
    for (int i=0, ny, nx; i<4; i++) {
      ny=y+DY[i];
      nx=x+DX[i];
      if (fd[ny][nx]!='o')
        PlaceBox(ny, nx, min(minY, ny), min(minX, nx), max(maxY, ny), max(maxX, nx), b+1, B);
    }
  fd[y][x]='.';
}

QueueItem GetBoxConfig(const char fd[][32], int y1, int x1, int y2, int x2, char c1, char c2) {
  int y, x, B=0;
  int minY=INF, minX=INF;
  int maxY=000, maxX=000;
  for (y=y1; y<=y2; y++)
    for (x=x1; x<=x2; x++)
      if (fd[y][x]==c1 || fd[y][x]==c2) {
        minY=min(minY, y); minX=min(minX, x);
        maxY=max(maxY, y); maxX=max(maxX, x);
        B++;
      }
  int Y=maxY-minY+1;
  int X=maxX-minX+1;
  int M=0;
  for (y=minY; y<=maxY; y++)
    for (x=minX; x<=maxX; x++)
      if (fd[y][x]==c1 || fd[y][x]==c2)
        M|=(1<<((y-minY)*X+(x-minX)));
  return QueueItem(minY, minX, BoxConfig(Y, X, M, B));
}

int GetBoxConfigId(const BoxConfig &bc) {
  if (mp[bc.b].count(bc))
    return mp[bc.b][bc];
  else
    return -1;
}

void DrawQueueItem(const QueueItem &qi, char c) {
  int y, x;
  const BoxConfig &bc=qi.bc;
  for (y=0; y<qi.bc.y; y++)
    for (x=0; x<qi.bc.x; x++)
      if (bc.m&(1<<(y*qi.bc.x+x)))
        fd[qi.y+y][qi.x+x]=c;
}

int GetDistance(const QueueItem &qi) {
  return dt[qi.y][qi.x][GetBoxConfigId(qi.bc)];
}

void SetDistance(const QueueItem &qi, int d) {
  dt[qi.y][qi.x][GetBoxConfigId(qi.bc)]=d;
}

bool inBounds(int y, int x, int Y, int X) {
  return y>=0 && x<X && y<Y && x>=0;
}
