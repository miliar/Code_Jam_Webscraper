#include <cstdio>
#include <cstring>

int nextInt() { int tmp; scanf("%d", &tmp); return tmp; }

const int W = 1<<8;//1<<13;

int S;

int ved[1<<16];
int node[1<<16];

int coor(int x, int y)
{
  return y * W + x;
}

int root(int a)
{
  return node[a] >= 0 ? node[a] = root(node[a]) : a;
}

int same(int a, int b)
{
  return root(a) == root(b);
}

bool unite(int a, int b)
{
  a = root(a);
  b = root(b);
  if (a != b) {
    node[a] += node[b];
    node[b] = a;
  }
  return a != b;
}

void init()
{
  memset(ved, 0, sizeof(ved));
  memset(node, -1, sizeof(node));
  unite(coor(1, 1),         coor(S+1, 0));
  unite(coor(1, S),         coor(S+2, 0));
  unite(coor(S, 2*S-1),     coor(S+3, 0));
  unite(coor(2*S-1, 2*S-1), coor(S+4, 0));
  unite(coor(2*S-1, S),     coor(S+5, 0));
  unite(coor(S, 1),         coor(S+6, 0));
}

int corner(int x, int y)
{
  int res = 0;
  for (int i = 0; i < 6; ++i)
    if (same(coor(x, y), coor(S+i+1, 0)))
      res |= 1<<i;
  return res;
}

int edge(int x, int y)
{
  int res = 0;
  for (int i = 1; i < S-1; ++i) {
    if (same(coor(x, y), coor(1, 1+i)))
      res |= 1;
    if (same(coor(x, y), coor(1+i, S+i)))
      res |= 2;
    if (same(coor(x, y), coor(S+i, 2*S-1)))
      res |= 4;
    if (same(coor(x, y), coor(2*S-i, 2*S-1-i)))
      res |= 8;
    if (same(coor(x, y), coor(2*S-1-i, S-i)))
      res |= 16;
    if (same(coor(x, y), coor(S-i, 1)))
      res |= 32;
  }
  return res;
}

const int dx[6] = {-1, -1, 0, 1, 1, 0};
const int dy[6] = {-1, 0, 1, 1, 0, -1};

int open(int x, int y)
{
  int res = 0;

  ved[coor(x, y)] = 1;

  int corners = corner(x, y);
  int edges = edge(x, y);
  for (int i = 0; i < 6; ++i) {
    if (!ved[coor(x+dx[i], y+dy[i])]) continue;
    corners |= corner(x+dx[i], y+dy[i]);
    edges |= edge(x+dx[i], y+dy[i]);
  }

  int br = 0;
  for (int i = 0; i < 6; ++i)
    if (corners>>i & 1) ++br;
  if (br >= 2) res |= 1;

  int fk = 0;
  for (int i = 0; i < 6; ++i)
    if (edges>>i & 1) ++fk;
  if (fk >= 3) res |= 2;

  int rg = 0;
  for (int i = 0; i < 6; ++i) {
    if (same(coor(x+dx[i], y+dy[i]),
             coor(x+dx[(i+2)%6], y+dy[(i+2)%6])) &&
        !same(coor(x+dx[i], y+dy[i]),
              coor(x+dx[(i+1)%6], y+dy[(i+1)%6])) &&
        (!same(coor(x+dx[i], y+dy[i]),
               coor(x+dx[(i+3)%6], y+dy[(i+3)%6])) ||
         !same(coor(x+dx[i], y+dy[i]),
               coor(x+dx[(i+4)%6], y+dy[(i+4)%6])) ||
         !same(coor(x+dx[i], y+dy[i]),
               coor(x+dx[(i+5)%6], y+dy[(i+5)%6])))) {
      rg = 1;
    }
    if (same(coor(x+dx[i], y+dy[i]),
             coor(x+dx[(i+3)%6], y+dy[(i+3)%6])) &&
        (!same(coor(x+dx[i], y+dy[i]),
               coor(x+dx[(i+1)%6], y+dy[(i+1)%6])) ||
         !same(coor(x+dx[i], y+dy[i]),
               coor(x+dx[(i+2)%6], y+dy[(i+2)%6]))) &&
        (!same(coor(x+dx[i], y+dy[i]),
               coor(x+dx[(i+4)%6], y+dy[(i+4)%6])) ||
         !same(coor(x+dx[i], y+dy[i]),
               coor(x+dx[(i+5)%6], y+dy[(i+5)%6])))) {
      rg = 1;
    }
  }
  if (rg) res |= 4;

  for (int i = 0; i < 6; ++i)
    if (ved[coor(x+dx[i], y+dy[i])])
      unite(coor(x, y), coor(x+dx[i], y+dy[i]));

  return res;
}

int main()
{
  int T = nextInt();
  for (int t = 1; t <= T; ++t) {
    S = nextInt();
    int M = nextInt();

    init();
    for (int m = 1; m <= M; ++m) {
      int x = nextInt();
      int y = nextInt();
      int res = open(x, y);
      if (res) {
        printf("Case #%d: ", t);
        if (res&1) printf("bridge");
        if (res&1 && res&6) putchar('-');
        if (res&2) printf("fork");
        if (res&2 && res&4) putchar('-');
        if (res&4) printf("ring");
        printf(" in move %d\n", m);
        for (int dummy = m+1; dummy <= M; ++dummy)
          scanf("%*d%*d");
        goto succ;
      }
    }
    printf("Case #%d: none\n", t);
  succ:;
  }

  return 0;
}
