#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 110

int a[N][N], w, h;
char b[N][N], c;

int hp[N*N][2];
const int dx[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};
void trace(int x, int y)
{
  for(int i = 0; ; i++) {
    if(b[x][y]) {
      for(--i; i >= 0; --i)
        b[hp[i][0]][hp[i][1]] = b[x][y];
      break;
    }
    hp[i][0] = x; hp[i][1] = y;
    int hm = a[x][y], hc = -1;
    for(int j = 0; j < 4; j++) {
      if(x + dx[j][0] >= 0 && x + dx[j][0] < h && y + dx[j][1] >= 0 && y + dx[j][1] < w && a[x+dx[j][0]][y+dx[j][1]] < hm) {
        hm = a[x+dx[j][0]][y+dx[j][1]];
        hc = j;
      }
    }
    if( hc >= 0 ) {
      x += dx[hc][0]; y += dx[hc][1];
    } else {
      for(; i >= 0; --i)
        b[hp[i][0]][hp[i][1]] = c;
      ++c;
      break;
    }
  }
}

int main()
{
  int t, index;
  scanf("%d", &t);
  for(index = 1; index <= t; index++) {
    scanf("%d%d", &h, &w);
    for(int i = 0; i < h; i++)
      for(int j = 0; j < w; j++) {
        scanf("%d", &a[i][j]);
        b[i][j] = 0;
      }
    c = 'a';
    for(int i = 0; i < h; i++)
      for(int j = 0; j < w; j++)
        if(b[i][j] == 0)
          trace(i, j);
    printf("Case #%d:\n", index);
    for(int i = 0; i < h; i++)
      for(int j = 0; j < w; j++) {
        printf("%c", b[i][j]);
        if(j < w-1) printf(" ");
        else printf("\n");
      }
  }
  return 0;
}
