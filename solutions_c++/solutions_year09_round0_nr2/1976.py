#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string> 
#include <vector>
#include <stack>
#include <stdexcept>

using namespace std;



struct Ufs {
  vector<int> elem;

  Ufs (int n) :
    elem (n) {

    for(int i=0; i<n; i++) {
      elem[i]  = i;
    }
  }

  int find (int k)  {
    int pt = k;
    while( elem[pt] != pt ) pt = elem[pt];

    // path-compression
    int root = pt;
    for( pt=k; elem[pt]!=pt; pt=k ) {
      k = elem[pt];
      elem[pt] = root;
    }

    return root;
  }

  void unite (int r, int s ) {
    r = find (r);
    s = find (s);
      elem[r]  = s;
  }
};

int field[100][100];
int gx[] = {-1,0,0,1};
int gy[] = {0,-1,1,0};
int width,height;

bool inside (int x, int y) {
  return x>=0&&x<height&&y>=0&&y<width;
}
    


int main() {
  int num_cases;
  cin >> num_cases;
  
  for (int case_num = 1; case_num <= num_cases; ++case_num) {
    cin >> height >> width;

    for (int i = 0; i < height; ++i) {
      for (int j = 0; j < width; ++j) {
        cin >> field[i][j];
      }
    }
    Ufs ufs (height * width);
    
    
    for (int i = 0; i < height; ++i) {
      for (int j = 0; j < width; ++j) {
        int best = numeric_limits<int>::max();
        int bx = -1, by = -1;
        for (int k = 0; k < 4; ++k) {
          int nx = i + gx[k];
          int ny = j + gy[k];
          if (inside (nx,ny) && field[nx][ny] < best) {
            bx = nx;
            by = ny;
            best = field[nx][ny];
          }
        }
        if (best < field[i][j]) 
          ufs.unite (i*width + j, bx*width + by);
      }
    }
    map<int,char> sink_to_char;
    cout << "Case #" << case_num << ":\n";
    for (int i = 0; i < height; ++i) {
      for (int j = 0; j < width; ++j) {
        if (sink_to_char.find (ufs.find (i*width + j)) == sink_to_char.end()) {
          sink_to_char.insert (make_pair (ufs.find (i*width + j), sink_to_char.size() + 'a'));
        }

        if (j) cout << " ";
        cout << sink_to_char[ufs.find (i*width + j)];
      }
      cout << "\n";
    }
  }
  
}
