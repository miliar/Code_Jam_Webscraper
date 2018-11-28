#include <iostream>
using namespace std;

int dx[] = { 1, 0, -1, -1 }, dy[] = { 1, 1, 1, 0 };
char grid[64][64], rgrid[64][64];

int main() {
  int t; cin >> t;
  for(int c = 1; c <= t; c++) {
    int N, K; cin >> N >> K;
    for(int i = 0; i < N; i++)
      scanf("%s", grid[i]);

    for(int i = 0; i < N; i++)
      for(int j = 0; j < N; j++)
        rgrid[i][j] = grid[N-1-j][i];

    /* printf("AFTER ROTATION\n");
    for(int i = 0; i < N; i++)
      printf("%s\n", rgrid[i]); */

    for(int j = 0; j < N; j++) {
      int k = N-1;
      for(int i = N-1; i >= 0; i--)
        if(rgrid[i][j] != '.')
          rgrid[k--][j] = rgrid[i][j];
      for(int i = k; i >= 0; i--)
        rgrid[i][j] = '.';
      rgrid[j][N] = 0;
    }

    /* printf("AFTER GRAVITY\n");
    for(int i = 0; i < N; i++)
      printf("%s\n", rgrid[i]); */

    bool rwin = false, bwin = false;
    for(int i = 0; i < N; i++)
      for(int j = 0; j < N; j++)
        for(int d = 0; d < 4; d++) {
          if(i+(K-1)*dx[d] < 0 || i+(K-1)*dx[d] >= N || j+(K-1)*dy[d] < 0 || j+(K-1)*dy[d] >= N) continue;
          bool crwin = true, cbwin = true;
          for(int k = 0; k < K; k++) {
            crwin = crwin && (rgrid[i+k*dx[d]][j+k*dy[d]] == 'R');
            cbwin = cbwin && (rgrid[i+k*dx[d]][j+k*dy[d]] == 'B');
          }
          rwin = rwin || crwin;
          bwin = bwin || cbwin;
        }

    printf("Case #%d: ", c);
    if(rwin && bwin) printf("Both\n");
    else if(rwin) printf("Red\n");
    else if(bwin) printf("Blue\n");
    else printf("Neither\n");
  }
  return 0;
}
