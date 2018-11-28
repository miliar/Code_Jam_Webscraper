#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

#define eprintf(...) fprintf(stderr, __VA_ARGS__)

#define sz(c) ((int) (c).size())
#define pb push_back
#define mp make_pair
#define f first
#define s second

int cc;
int n,M,S;
int a[6666][6666];
int col[6666][6666];
int kk[6666666];
bool ring=false;
bool bridge=false;
bool forkk=false;

int corner(int i, int j) {
  if (i==1 && j==1) return 1;
  if (i==1 && j==n) return 2;
  if (i==n && j==1) return 3;
  if (i==n && j==2*n-1) return 4;
  if (i==2*n-1 && j==n) return 5;
  if (i==2*n-1 && j==2*n-1) return 6;
  return 0;
}

int edge(int i,int j) {
  if (i == 1) return 1;
  if (j == 1) return 2;
  if (i == 2*n-1) return 3;
  if (j == 2*n-1) return 4;
  if (i-j == n-1) return 5;
  if (j-i == n-1) return 6;
  return 0;
}

bool inside(int i,int j) {
  return (i>=1 && i<=2*n-1 && j>=1 && j<=2*n-1 && i-j<=n-1 && j-i<=n-1);
}

bool move(int i,int j) {
  if (a[i][j]==-1 || a[i][j]>S)
    return false;
  return true;
}

void dfs1(int i,int j,int cc) {
  if (!inside(i,j) || move(i,j) || (col[i][j] & cc)>0) return;
  col[i][j]|=cc;
  dfs1(i+1,j,cc);
  dfs1(i+1,j+1,cc);
  dfs1(i,j+1,cc);
  dfs1(i-1,j,cc);
  dfs1(i-1,j-1,cc);
  dfs1(i,j-1,cc);
}

void dfs2(int i,int j,int cc) {
  if (!inside(i,j) || !move(i,j) || (col[i][j] & cc)>0) return;
  col[i][j]|=cc;
  dfs2(i+1,j,cc);
  dfs2(i+1,j+1,cc);
  dfs2(i,j+1,cc);
  dfs2(i-1,j,cc);
  dfs2(i-1,j-1,cc);
  dfs2(i,j-1,cc);
}

void check_ring() {
  ring=false;
  for (int i=1; i<=2*n-1; ++i)
    for (int j=1; j<=2*n-1; ++j)
      col[i][j]=0;
  for (int i=1; i<=2*n-1; ++i)
    for (int j=1; j<=2*n-1; ++j)
      if (inside(i,j) && !move(i,j) && edge(i,j)) {
        int e = edge(i,j);
        dfs1(i,j,1<<e);
      }
  for (int i=1; i<=2*n-1; ++i)
    for (int j=1; j<=2*n-1; ++j)
      if (inside(i,j) && !move(i,j) && col[i][j]==0) {
        ring=true;
        return;
      }
}

void check_bridge() {
  bridge=false;
  for (int i=1; i<=2*n-1; ++i)
    for (int j=1; j<=2*n-1; ++j)
      col[i][j]=0;
  for (int i=1; i<=2*n-1; ++i)
    for (int j=1; j<=2*n-1; ++j)
      if (inside(i,j) && move(i,j) && corner(i,j)) {
        int c = corner(i,j);
        dfs2(i,j,1<<c);
      }
  for (int i=1; i<=2*n-1; ++i)
    for (int j=1; j<=2*n-1; ++j)
      if (__builtin_popcount(col[i][j]) >= 2) {
        bridge=true;
        return;
      }
}

void check_fork() {
  forkk=false;
  for (int i=1; i<=2*n-1; ++i)
    for (int j=1; j<=2*n-1; ++j)
      col[i][j]=0;
  for (int i=1; i<=2*n-1; ++i)
    for (int j=1; j<=2*n-1; ++j)
      if (inside(i,j) && move(i,j) && !corner(i,j) && edge(i,j)) {
        int e = edge(i,j);
        dfs2(i,j,1<<e);
      }
  for (int i=1; i<=2*n-1; ++i)
    for (int j=1; j<=2*n-1; ++j)
      if (__builtin_popcount(col[i][j]) >= 3) {
        forkk=true;
        return;
      }
}

bool winning(int s) {
  S = s;
  check_ring();
  check_bridge();
  check_fork();
  if (ring || bridge || forkk)
    return true;
  return false;
}

void solve(int testcase) {
  printf("Case #%d: ", testcase);
  eprintf("Case #%d: ", testcase);
  scanf("%d%d", &n, &M);
  for (int i=1; i<=2*n-1; ++i)
    for (int j=1; j<=2*n-1; ++j)
      a[i][j]=-1;
  for (int i=0; i<M; ++i) {
    int x,y;
    scanf("%d%d", &x,&y);
    a[x][y]=i;
  }
  int l=0;
  while (l<M && !winning(l)) ++l;
  if (!winning(l)) {
    printf("none\n");
    eprintf("none\n");
    return;
  }
  string res;
  if (bridge)
    res += "bridge";
  if (forkk) {
    if (!res.empty()) res+="-";
    res += "fork";
  }
  if (ring) {
    if (!res.empty()) res+="-";
    res += "ring";
  }
  printf("%s in move %d\n", res.c_str(), l+1);
  eprintf("%s in move %d\n", res.c_str(), l+1);
}

int main() {
  int T;
  scanf("%d", &T);
  for (int i = 1; i <= T; ++i)
    solve(i);
  return 0;
}
