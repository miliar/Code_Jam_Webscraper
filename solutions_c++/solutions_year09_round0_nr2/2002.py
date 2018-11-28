#include <iostream>
#include <vector>

using namespace std;

const int MAX_ALT = 999999;

enum Dir {
  STOP,
  NORTH, WEST, EAST, SOUTH
};

struct Pos {
  int h, w;
  Pos(int _h, int _w): h(_h), w(_w) {}
  void walk(Dir d) {
    switch (d) {
      case NORTH: h --; break;
      case WEST: w --; break;
      case EAST: w ++; break;
      case SOUTH: h ++; break;
    }
  }
  bool outside(int H, int W) const {
    return (h<0) || (h>=H) || (w<0) || (w>=W);
  }
};

struct Map {
  int H,W;
  int alt[100][100];
  Dir down[100][100];
  char basin[100][100];
  Map(int _H, int _W) {
    H = _H, W= _W;
    // initialise basin marker
    for (int h=0; h<H; h++) {
      for (int w=0; w<W; w++) {
        basin[h][w] = '.';
      }
    }
  }
  ~Map() {
  }
  void set_height(int h, int w, int height) {
    alt[h][w] = height;
  }
  int rel_alt(int h, int w, Dir d) {
    Pos p(h,w);
    p.walk(d);
    if (p.outside(H,W)) return MAX_ALT;
    return alt[p.h][p.w];
  }
  void FindDown(int h, int w) {
    int min_alt = alt[h][w];
    down[h][w] = STOP;
    for (int dir = NORTH; dir <= SOUTH; dir++) {
      int neighbour_alt = rel_alt(h,w,(Dir)dir);
      if (neighbour_alt < min_alt) {
        down[h][w] = (Dir)dir;
        min_alt = neighbour_alt;
      }
    }
  }
  char& BasinLabel(int h, int w) {
    return basin[h][w];
  }
  char& BasinLabel(Pos p) {
    return basin[p.h][p.w];
  }
  void LabelBasin(int h, int w, char& next_basin) {
    Pos p(h,w);
    vector<Pos> trail;
    while (BasinLabel(p) == '.') {
      trail.push_back(p);
      Dir d = down[p.h][p.w];
      if (d == STOP) {
        // End loop by assigning a value to basin
        BasinLabel(p) = next_basin;
        next_basin ++;
      }
      p.walk(d);
      assert(!p.outside(H,W));
    }
    for (vector<Pos>::iterator i = trail.begin();
        i != trail.end();
        i ++)
    {
      BasinLabel(*i) = BasinLabel(p);
    }
  }
};

int T, H, W;

int main()
{
  cin >> T;
  
  for (int t = 0; t<T; t++) {
    // Read map
    cin >> H >> W;
    Map m(H,W);
    
    for (int h = 0; h<H; h++) {
      for (int w = 0; w<W; w++) {
        int height;
        cin >> height;
        m.set_height(h,w,height);
      }
    }
    
    // Generate down direction
    
    for (int h = 0; h<H; h++) {
      for (int w = 0; w<W; w++) {
        m.FindDown(h,w);
      }
    }
    
    // Label basins
    char basin = 'a';

    for (int h = 0; h<H; h++) {
      for (int w = 0; w<W; w++) {
        m.LabelBasin(h,w,basin);
      }
    }
    
    // Output result
    cout << "Case #"<<t+1<<": "<< endl;
    for (int h = 0; h<H; h++) {
      for (int w = 0; w<W; w++) {
        if (w>0) cout << ' ';
        cout << m.BasinLabel(h,w);
      }
      cout << endl;
    }
  }
}
