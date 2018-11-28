#include <cstring>
#include <iostream>
#include <set>
#include <vector>
#include <iterator>

int M[102][102];
int F[102][102];
char L[102][102];

static int enloc(int h, int w) { return 1000*h+w; }
static void deloc(int& h, int& w, int loc) { h = loc/1000; w = loc%1000; }
static void findSink(int& hs, int& ws, int h, int w)
{
  int hn, wn;
  deloc(hn, wn, F[h][w]);
  //std::cout << F[h][w] << std::endl;
  if(hn == h && wn == w) {
    hs = h;
    ws = w;
    //std::cout << "sink = " << hs << "," << ws << std::endl;
  } else {
    findSink(hs, ws, hn, wn);
  }
}

static void putLabel(int h, int w, char label)
{
  L[h][w] = label;
  int loc = enloc(h, w);
  if(F[h-1][w] == loc) putLabel(h-1, w, label);
  if(F[h][w-1] == loc) putLabel(h, w-1, label);
  if(F[h][w+1] == loc) putLabel(h, w+1, label);
  if(F[h+1][w] == loc) putLabel(h+1, w, label);
}

int main() {
  int T;
  std::cin >> T;
  for(int t = 1; t <= T; ++t) {
    int H, W;
    std::cin >> H >> W;
    memset(M, 0, sizeof(M));
    memset(F, 0, sizeof(F));
    memset(L, 0, sizeof(L));

    for(int w = 0; w <= W; ++w) {
      M[0][w] = 99999;
      M[H+1][w] = 99999;
    }
    
    for(int h = 1; h <= H; ++h) {
      M[h][0] = 99999;
      for(int w = 1; w <= W; ++w) {
	std::cin >> M[h][w];
      }
      M[h][W+1] = 99999;
    }
    for(int h = 1; h <= H; ++h) {
      for(int w = 1; w <= W; ++w) {
	int alt = M[h][w];
	F[h][w] = enloc(h, w);
	if(M[h-1][w] < alt) {
	  F[h][w] = enloc(h-1, w);
	  alt = M[h-1][w];
	}
	if(M[h][w-1] < alt) {
	  F[h][w] = enloc(h, w-1);
	  alt = M[h][w-1];
	}
	if(M[h][w+1] < alt) {
	  F[h][w] = enloc(h, w+1);
	  alt = M[h][w+1];
	}
	if(M[h+1][w] < alt) {
	  F[h][w] = enloc(h+1, w);
	  alt = M[h+1][w];
	}
      }
    }
    char label = 'a';
    for(int h = 1; h <= H; ++h) {
      for(int w = 1; w <= W; ++w) {
	if(L[h][w] != 0) continue;
	int i, j;
	findSink(i, j, h, w);
	//std::cout << i << "," << j << std::endl;
	putLabel(i, j, label);
	++label;
      }
    }
    std::cout << "Case #" << t << ":" << std::endl;
    for(int h = 1; h <= H; ++h) {
      std::copy(&L[h][1], &L[h][W], std::ostream_iterator<char>(std::cout, " "));
      std::cout << L[h][W] << std::endl;
    }
  }
}
