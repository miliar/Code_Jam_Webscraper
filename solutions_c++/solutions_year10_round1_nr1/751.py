#include <iostream>

using namespace std;

#define MAXN 55

#define NDIR 8
int dr[] = {-1,-1,0,+1,+1,+1,0,-1};
int dc[] = {0,+1,+1,+1,0,-1,-1,-1};

int i,j,k;
int r,c;
int N,K;
int nTests,test;
char T[MAXN][MAXN];
bool won[1000];
int r_,c_,dir;

int main() {
  scanf("%d",&nTests);
  for (test = 1; test <= nTests; ++test) {
    scanf("%d %d",&N,&K);
    for (c = N; c >= 1; --c) {
      for (r = 1; r <= N; ++r) {
        scanf(" %c",&T[r][c]);
      }
    }
    for (r = N; r >= 1; --r) {
      for (c = 1; c <= N; ++c) {
        if (T[r][c] != '.') {
          r_ = r;
          while (r_ < N && T[r_+1][c] == '.') {
            swap(T[r_][c],T[r_+1][c]);
            ++r_;
          }
        }
      }
    }
    won['B'] = won['R'] = false;
    for (r = 1; r <= N; ++r) {
      for (c = 1; c <= N; ++c) {
        if (T[r][c] != '.') {
          for (dir = 0; dir < NDIR; ++dir) {
            int cnt = 0;
            r_ = r;
            c_ = c;
            while (1 <= r_ && r_ <= N && 1 <= c_ && c_ <= N && T[r_][c_] == T[r][c]) {
              ++cnt;
              r_ += dr[dir];
              c_ += dc[dir];
            }
            if (cnt >= K) {
              won[T[r][c]] = true;
            }
          }
        }
      }
    }
    printf("Case #%d: ",test);
    if (!won['R'] && !won['B']) {
      printf("Neither\n");
    } else if (won['R'] && won['B']) {
      printf("Both\n");
    } else if (won['R']) {
      printf("Red\n");
    } else {
      printf("Blue\n");
    }
  }
  return 0;
}
