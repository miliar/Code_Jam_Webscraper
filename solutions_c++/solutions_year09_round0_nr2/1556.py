#include <string>
#include <vector>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <numeric>
#include <complex>

using namespace std;

int H,W;
int altitudes[100][100];
char basins[26];
int edge[100][100];
char basin[100][100];

int min(int a, int b) {
  if(a < b) return a;
  return b;
}

void print_basins() 
{
  for(int h = 0; h < H; h++) {
    for(int w = 0; w < W; w++) {
      printf("%c", isalnum(basin[h][w]) ? basin[h][w] : '0');
      if(w < W-1) {
	printf(" ");
      } else {
	printf("\n");
      }
    }
  }
}

void print_edges()
{
  for(int h = 0; h < H; h++) {
    for(int w = 0; w < W; w++) {
      int e = edge[h][w];
      int w1 = e % 100;
      int h1 = (e - w1) / 100;
      printf("%d:%d,%d:%d", h,w,h1,w1);
      if(w < W-1) {
	printf(" ");
      } else {
	printf("\n");
      }
    }
  }
}

bool isbasin(int h, int w) {

  int m = 10001;

 if(h > 0) m = min(m,altitudes[h-1][w]);
 if(h < H-1) m = min(m,altitudes[h+1][w]);
 if(w > 0) m = min(m,altitudes[h][w-1]);
 if(w < W-1) m = min(m,altitudes[h][w+1]);

 if(m >= altitudes[h][w]) return true;
 return false;
}

int get_edge(int h, int w) {
  int m = 10001,s=100*h+w;
  int r;
  int q = altitudes[h][w];
  if(h > 0) {
    r = altitudes[h-1][w];
    if(r < m && r<q) { m = r; s = 100*(h-1)+w; }
  }
  if(w > 0) {
    r = altitudes[h][w-1];
    if(r < m && r<q) { m = r; s = 100*h+w-1; }
  }
  if(w < W-1) {
    r = altitudes[h][w+1];
    if(r < m && r<q) { m = r; s = 100*h+w+1; }
  }
  if(h < H-1) {
    r = altitudes[h+1][w];
    if(r < m && r<q) { m = r; s = 100*(h+1)+w; }
  }
  return s;
}

int main(void)
{
  int T;
  cin >> T;
  int h1,w1;

  for (int c = 1; c <= T; c++) {
    char bc = 'A', cb = 'a'; 
    for(int i = 0; i < 26; i++) {
      basins[i] = '0';
    }
    cin >> H >> W;
    for(int h = 0; h < H; h++) {
      for(int w = 0; w < W; w++) {
	cin >> altitudes[h][w];
	edge[h][w] = 0;
	basin[h][w] = '0';
      }
    }
    //printf("Got altitudes\n");

    for(int h = 0; h < H; h++) {
      for(int w = 0; w < W; w++) {
	edge[h][w] = get_edge(h,w);
      }
    }

    //printf("Got edges:\n"); print_edges();

    for(int h = 0; h < H; h++) {
      for(int w = 0; w < W; w++) {
	if(isbasin(h,w)) {
	  basin[h][w] = bc;
	  bc++;
	}
      }
    }

    //printf("Got basins:\n"); print_basins();

    for(int h = 0; h < H; h++) {
      for(int w = 0; w < W; w++) {
	h1 = h; w1 = w;
	int h2,w2;
	while(edge[h1][w1] != 100*h1 + w1) {
	  w2 = edge[h1][w1] % 100;
	  h2 = (edge[h1][w1] / 100);
	  w1 = w2; h1 = h2;
	}
	basin[h][w] = basin[h1][w1];
      }
    }
    //printf("Followed edges\n"); print_basins();
    
    for(int h = 0; h < H; h++) {
      for(int w = 0; w < W; w++) {
	if(basins[basin[h][w]-'A'] == '0') {
	  basins[basin[h][w]-'A'] = cb++;
	}
      }
    }

    //printf("Tabulated basins\n");

    for(int h = 0; h < H; h++) {
      for(int w = 0; w < W; w++) {
	basin[h][w] = basins[basin[h][w]-'A'];
      }
    }

    printf("Case #%d:\n", c);
    for(int h = 0; h < H; h++) {
      for(int w = 0; w < W; w++) {
	printf("%c", isalnum(basin[h][w]) ? basin[h][w] : '0');
	if(w < W-1) {
	  printf(" ");
	} else {
          printf("\n");
	}
      }
    }
  }
}
