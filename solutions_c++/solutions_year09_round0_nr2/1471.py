#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
using namespace std;
FILE* fin = freopen("b.in", "r", stdin);
FILE* fout = freopen("b.out", "w", stdout);

int alt[104][104];
char label[104][104], l;
int T, W, H;

char trace(int y, int x) {
  if (label[y][x]) return label[y][x];
  int a = min(min(alt[y][x-1], alt[y][x+1]),
              min(alt[y-1][x], alt[y+1][x]));
  if (a >= alt[y][x]) {
    label[y][x] = l;
    l++;
  } else {
    if (alt[y-1][x] == a) label[y][x] = trace(y-1, x);
    else if (alt[y][x-1] == a) label[y][x] = trace(y, x-1);
    else if (alt[y][x+1] == a) label[y][x] = trace(y, x+1);
    else label[y][x] = trace(y+1, x);
  }
  return label[y][x];
}

int main() {
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    printf("Case #%d:\n", i+1);
    scanf("%d%d", &H, &W);
    memset(alt, 127, sizeof(alt));
    memset(label, 0, sizeof(label));
    for (int y = 1; y <= H; y++)
    for (int x = 1; x <= W; x++)
      scanf("%d", &alt[y][x]);
    l = 'a';
    for (int y = 1; y <= H; y++) {
      for (int x = 1; x <= W; x++) {
        printf("%c", trace(y, x));
        if (x < W) printf(" ");
      }
      printf("\n");
    }
  }
  fclose(fout);
  //while(1); // debug
}
