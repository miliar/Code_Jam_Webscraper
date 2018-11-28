#include <iostream>
#include <string>
#include <stdlib.h>

using namespace std;

void setLabel(char **label, char **choice, char l, int h, int w, int H, int W){
  label[h][w] = l;
  if(h >  0  && label[h-1][w] == 4) setLabel(label, choice, l, h-1, w, H, W);
  if(w >  0  && label[h][w-1] == 3) setLabel(label, choice, l, h, w-1, H, W);
  if(w < W-1 && label[h][w+1] == 2) setLabel(label, choice, l, h, w+1, H, W);
  if(h < H-1 && label[h+1][w] == 1) setLabel(label, choice, l, h+1, w, H, W);
}

int main(void) {
  int T, H, W;
  cin >> T;
  for(int t = 1; t <= T; ++t) {
    cin >> H >> W;
    int elev[H][W];
    char *raw = (char *)malloc(sizeof(char) * H * W * 2);
    char **label = (char **)malloc(sizeof(char *) * H * 2), **choice = label + H, nextlabel = 'a';
    for(int h = 0; h < H; ++h) {
      label[h] = raw + h * W;
      choice[h]= raw + (H + h) * W;
    }
    for(int h = 0; h < H; ++h)
      for(int w = 0; w < W; ++w) {
        cin >> elev[h][w];
        label[h][w] = 0;
      }
    int a[5] = {0,0,0,0,0};
    for(int h = 0; h < H; ++h)
      for(int w = 0; w < W; ++w) {
        int minval = elev[h][w];
        label[h][w] = 0;
        if(h >  0  && elev[h-1][w]<minval){minval=elev[h-1][w];label[h][w]=1;}
        if(w >  0  && elev[h][w-1]<minval){minval=elev[h][w-1];label[h][w]=2;}
        if(w < W-1 && elev[h][w+1]<minval){minval=elev[h][w+1];label[h][w]=3;}
        if(h < H-1 && elev[h+1][w]<minval){minval=elev[h+1][w];label[h][w]=4;}
        ++a[label[h][w]];
      }
    for(int h = 0; h < H; ++h)
      for(int w = 0; w < W; ++w) {
        if(label[h][w] < 5) {
          int y = h, x = w;
          while(label[y][x]) {
            if(label[y][x] == 1) --y;
            if(label[y][x] == 2) --x;
            if(label[y][x] == 3) ++x;
            if(label[y][x] == 4) ++y;
          }
          setLabel(label, choice, nextlabel, y, x, H, W);
          ++nextlabel;
        }
      }
    printf("Case #%i:\n", t);
    for(int h = 0; h < H; ++h)
      for(int w = 0; w < W; ++w) {
        printf("%c ", label[h][w]);
        if(w == W-1) printf("\n");
        else printf(" ");
      }
    free(raw);
    free(label);
  }
}
