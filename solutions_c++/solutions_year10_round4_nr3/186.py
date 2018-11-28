#include <algorithm>
#include <cstdio>

using namespace std;

class Rec {
  public:
    Rec() {}
    Rec(int x1, int y1, int x2, int y2) :x1(x1), y1(y1), x2(x2), y2(y2) {}
    int x1, y1, x2, y2;
};

const int kMaxN = 1000 + 24;
const int kInf = 200000000;

int N;
Rec rec[kMaxN];
bool visited[kMaxN];

int st[kMaxN], sn;
int low, right;

bool Intersect(int l1, int r1, int l2, int r2) {
  return !(r1 < l2 - 1 || r2 < l1 - 1);
}

bool Intersect(const Rec& a, const Rec& b) {
  return Intersect(a.x1, a.x2, b.x1, b.x2) && Intersect(a.y1, a.y2, b.y1, b.y2);
}

void DFS(int i) {
  st[sn++] = i;
  visited[i] = true;
  low = max(low, rec[i].y2);
  right = max(right, rec[i].x2);
  for (int j = 0; j < N; ++j)
    if (j != i && Intersect(rec[i], rec[j]) && visited[j] == false)
      DFS(j);
}

int main() {
  int cases;
  scanf("%d", &cases);
  for (int e = 1; e <= cases; ++e) {
    printf("Case #%d: ", e);
    scanf("%d", &N);
    for (int i = 0; i < N; ++i)
      scanf("%d %d %d %d", &rec[i].x1, &rec[i].y1, &rec[i].x2, &rec[i].y2);
    fill(visited, visited + N, false);
    int totalmax = 0;
    for (int i = 0; i < N; ++i) 
      if (visited[i] == false) {
        sn = 0;
        low = -kInf;
        right = -kInf;
        DFS(i);
        //printf("%d %d\n", low, right);
        for (int j = 0; j < sn; ++j) {
          int k = st[j];
          //printf("%d %d\n", rec[k].x1, rec[k].y1);
          int t = right + low - (rec[k].x1 + rec[k].y1);
          totalmax = max(totalmax, t);
        }
      }
    printf("%d\n", totalmax + 1);
  }
  return 0;
}
