#include <iostream>
#include <map>

#define uint unsigned int
#define MAX_HW 100
using namespace std;

uint T;    // Number of maps.
uint H, W; // Dimensions of the maps.


uint alt_map[MAX_HW][MAX_HW];
uint mfset[MAX_HW*MAX_HW];

inline void MIN(uint x, uint y, uint &xr, uint &yr) {
  xr = x;
  yr = y;

  /* Min -> up. */
  if(y > 0 && alt_map[yr][xr] > alt_map[y-1][x] ){
    xr = x;
    yr = y-1;
  }

  /* Min -> left. */
  if(x > 0 && alt_map[yr][xr] > alt_map[y][x-1]) {
    xr = x - 1;
    yr = y;
  }

  /* Min -> right. */
  if(x < W-1 && alt_map[yr][xr] > alt_map[y][x+1]){
    xr = x + 1;
    yr = y;
  }

  /* Min -> down. */
  if(y < H-1 && alt_map[yr][xr] > alt_map[y+1][x]) {
    xr = x;
    yr = y + 1;
  }
}

inline uint rep(uint p) {
  while(mfset[p] != p)
    p = mfset[p];
  
  return p;
}

int main() {

  /* Read cases. */
  cin >> T; 

  for(uint t = 1; t <= T; ++t) {
    /* Read H and W. */
    cin >> H >> W;
    
    /* Init MF-set. */
    uint size = H*W;
    for(uint i = 0; i < size; ++i)
      mfset[i] = i;

    /* Read the Map. */
    for(uint h = 0; h < H; ++h)
      for(uint w = 0; w < W; ++w) {
	uint alt;
	cin >> alt;
	alt_map[h][w] = alt;
      }

    for(uint y = 0; y < H; ++y) {
      for(uint x = 0; x < W; ++x) {
	uint x_min, y_min;
	MIN(x, y, x_min, y_min);

	uint p = y * W + x;
	uint p_min = y_min * W + x_min;
	
	if (p != p_min) {
	  uint rep_p = rep(p);
	  uint rep_pmin = rep(p_min);
	  if(rep_pmin > rep_p) mfset[rep_pmin] = rep_p;
	  else mfset[rep_p] = rep_pmin;
	}
      }
    }

    map<uint, char> labels;
    char letter = 'a';
    for(uint i = 0; i < size; ++i)
      if( mfset[i] == i ){
	labels[i] = letter;
	++letter;
      }

    cout << "Case #" << t << ":" << endl;
    for(uint y = 0; y < H; ++y) {
      for(uint x = 0; x < W; ++x) {
	cout << labels[mfset[rep(y*W +x)]] << " ";
      }
      cout << endl;
    }
  }

  return 0;
}
