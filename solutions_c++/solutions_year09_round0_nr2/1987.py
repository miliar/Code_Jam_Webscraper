#include<iostream>
#include<cstring>

using namespace std;

const int MAX_H = 100;
const int MAX_W = 100;

int H, W;
int altitudes[MAX_H][MAX_W];

char cur;
char basin[MAX_H][MAX_W];

int dh[] = {-1, 0, 0, 1}, dw[] = {0, -1, 1, 0};

char go(int h, int w)
{
  if(basin[h][w])
    return basin[h][w];
  int bw = w, bh = h;
  for(int i = 0; i < 4; i++)
    {
      int nw = w+dw[i], nh = h+dh[i];
      if(nw >= 0 && nw < W && nh >= 0 && nh < H &&
         altitudes[nh][nw] < altitudes[bh][bw])
        bh = nh, bw = nw;
    }
  return basin[h][w] = bw == w && bh == h ? cur++ : go(bh, bw);
}

int main()
{
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++)
    {
      cur = 'a';
      memset(basin, 0, sizeof(basin));

      cin >> H >> W;
      for(int h = 0; h < H; h++)
        for(int w = 0; w < W; w++)
          cin >> altitudes[h][w];
      for(int h = 0; h < H; h++)
        for(int w = 0; w < W; w++)
          go(h, w);
      cout << "Case #" << t << ":" << "\n";
      for(int h = 0; h < H; h++)
        {
          for(int w = 0; w < W; w++)
            cout << basin[h][w] << (w < W-1 ? " " : "");
          cout << "\n";
        }
    }
}
